#include <time.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

#include "student.h"
#include "config.h"
#include "worker_gate.h"
#include "globals.h"

void* student_run(void *arg)
{
    student_t *self = (student_t*) arg;
    table_t *tables  = globals_get_table();
    // Inicia o semáforo binário que controla o acesso aos buffets
    sem_init(&self->semPodeEntrarRu, 0, 0);
    // Insere no final da fila para entrar no RU
    worker_gate_insert_queue_buffet(self);
    // Espera que o worker gate permita a entrada
    sem_wait(&self->semPodeEntrarRu);
    
    student_serve(self);
    student_seat(self, tables);
    student_leave(self, tables);

    pthread_exit(NULL);
};

void student_seat(student_t *self, table_t *table)
{
    // Espera até que existam lugares vagos
    sem_wait(globals_get_sem_lugares_vagos());
    // Senta em uma mesa.
    // encontra_mesa() decrementa de forma segura o 
    // número de lugares vagos na mesa que o estudante escolheu
    self->_id_mesa = encontra_mesa(table)->_id;
    // Come
    msleep(rand() % 500);
}

void student_serve(student_t *self)
{
    // Escolhe de forma segura um buffet livre para entrar
    entra_buffet(self);
    // Se serve
    while (self->_buffet_position < 5)
    {
        msleep(globals_get_sleep_time());
        buffet_next_step(globals_get_buffets(), self);
    }
    globals_incrementa_qtd_serviram();
}

void student_leave(student_t *self, table_t *table)
{
    // Incrementa de forma segura os lugares vagos na mesa em que estava sentado
    pthread_mutex_t* mutex = globals_get_mutex_mesa(self->_id_mesa);
    pthread_mutex_lock(mutex);
    table[self->_id_mesa]._empty_seats += 1;
    pthread_mutex_unlock(mutex);
    // Adiciona um token ao semaforo que controla o número de lugares vagos no RU
    sem_post(globals_get_sem_lugares_vagos());
    // Incrementa (de forma segura) estudantes que sairam do ru
    globals_incrementa_qtd_sairam();
}

/* --------------------------------------------------------- */
/* ATENÇÃO: Não será necessário modificar as funções abaixo! */
/* --------------------------------------------------------- */

student_t *student_init()
{
    student_t *student = malloc(sizeof(student_t));
    student->_id = rand() % 1000;
    student->_buffet_position = -1;
    int none = TRUE;
    for (int j = 0; j <= 4; j++)
    {
        student->_wishes[j] = _student_choice();
        if(student->_wishes[j] == 1) none = FALSE;
    }

    if(none == FALSE){
        /* O estudante só deseja proteína */
        student->_wishes[3] = 1;
    }

    return student;
};

void student_finalize(student_t *self){
    sem_destroy(&self->semPodeEntrarRu);
    free(self);
};


pthread_t students_come_to_lunch(int number_students)
{
    pthread_t lets_go;
    pthread_create(&lets_go, NULL, _all_they_come, &number_students);
    return lets_go;
}

/**
 * @brief Função (privada) que inicializa as threads dos alunos.
 * 
 * @param arg 
 * @return void* 
 */
void* _all_they_come(void *arg)
{
    int number_students = globals_get_students();
    
    student_t *students[number_students];

    for (int i = 0; i < number_students; i++)
    {
        students[i] = student_init();                                               /* Estudante é iniciado, recebe um ID e escolhe o que vai comer*/
    }

    for (int i = 0; i < number_students; i++)
    {
        pthread_create(&students[i]->thread, NULL, student_run, students[i]);       /*  Cria as threads  */
    }

    for (int i = 0; i < number_students; i++)
    {
        pthread_join(students[i]->thread, NULL);                                    /*  Aguarda o término das threads   */
    }

    for (int i = 0; i < number_students; i++)
    {
        student_finalize(students[i]);                                              /*  Libera a memória de cada estudante  */
    }

    pthread_exit(NULL);
}

/**
 * @brief Função que retorna as escolhas dos alunos, aleatoriamente (50% para cada opção)
 *        retornando 1 (escolhido) 0 (não escolhido). É possível que um aluno não goste de nenhuma opção
 *         de comida. Nesse caso, considere que ele ainda passa pela fila, como todos aqueles que vão comer.
 * @return int 
 */
int _student_choice()
{
    float prob = (float)rand() / RAND_MAX;
    return prob > 0.51 ? 1 : 0;
}