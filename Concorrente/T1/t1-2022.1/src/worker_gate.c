#include <stdlib.h>

#include "worker_gate.h"
#include "globals.h"
#include "config.h"


void worker_gate_remove_student()
{
    queue_t* q = globals_get_queue();
    pthread_mutex_t* mutex = globals_get_mutex_fila_estudantes();
    // Retira o primeiro estudante da fila 
    pthread_mutex_lock(mutex);
    if (q->_length > 0 && q->_first != NULL)
    {
        student_t* student = queue_remove(q);
        pthread_mutex_unlock(mutex);
        // Espera até que existam lugares vagos nos buffets
        sem_wait(globals_get_sem_buffets_livres());
        // Libera o estudante para procurar um buffet para entrar
        sem_post(&student->semPodeEntrarRu);
        globals_incrementa_qtd_entraram();
    }
    pthread_mutex_unlock(mutex);
}


void *worker_gate_run(void *arg)
{
    // Executa enquanto todos ainda não sairam
    while (globals_get_todos_sairam() == FALSE)
    {
        if (globals_get_todos_serviram() == FALSE)
            worker_gate_remove_student();
    }
    printf("Fechando o RU\n");
    pthread_exit(NULL);
}

void worker_gate_init(worker_gate_t *self)
{
    int number_students = globals_get_students();
    pthread_create(&self->thread, NULL, worker_gate_run, &number_students);
}

void worker_gate_finalize(worker_gate_t *self)
{
    pthread_join(self->thread, NULL);
    free(self);
}

void worker_gate_insert_queue_buffet(student_t *student)
{
    pthread_mutex_t* mutex = globals_get_mutex_fila_estudantes();
    pthread_mutex_lock(mutex);
    queue_insert(globals_get_queue(), student);
    pthread_mutex_unlock(mutex);    
}