#include <stdlib.h>
#include "buffet.h"
#include "config.h"
#include "globals.h"


void *buffet_run(void *arg)
{   
    buffet_t *self = (buffet_t*) arg;
    
    // Roda enquanto existem estudantes se servindo
    while (globals_get_todos_serviram() == FALSE) 
    {
        _log_buffet(self);
        msleep(globals_get_sleep_time());
    }

    pthread_exit(NULL);
}

void buffet_init(buffet_t *self, int number_of_buffets)
{
    globals_init(number_of_buffets);
    int i = 0, j = 0;
    for (i = 0; i < number_of_buffets; i++)
    {
        /*A fila possui um ID*/
        self[i]._id = i;
        // Inicia os mutex que protegem a fila esquerda e direita do buffet
        pthread_mutex_init(&self[i].mutexFilaDireita, NULL);
        pthread_mutex_init(&self[i].mutexFilaEsquerda, NULL);

        /* Inicia com 40 unidades de comida em cada bacia */
        for(j = 0; j < 5; j++)
        {
            self[i]._meal[j] = 40;
            // Inicia os mutex que protegem o acesso a cada bacia de comida
            pthread_mutex_init(&self[i].mutexComida[j], NULL);
        }
        

        for(j= 0; j< 5; j++)
        {
             /* A fila esquerda do buffet possui cinco posições. */
            self[i].queue_left[j] = 0;
            /* A fila esquerda do buffet possui cinco posições. */
            self[i].queue_right[j] = 0;
        }

        pthread_create(&self[i].thread, NULL, buffet_run, &self[i]);
    }
}


int buffet_queue_insert(buffet_t *self, student_t *student, char lado)
{
    int* queue = lado == 'L' ? self->queue_left : self->queue_right;
    pthread_mutex_t* mutex = lado == 'L' ? &self->mutexFilaEsquerda : &self->mutexFilaDireita;
    pthread_mutex_lock(mutex);
    if (queue[0] == 0) 
    {
        queue[0] = student->_id;
        pthread_mutex_unlock(mutex);
        student->left_or_right = lado;
        student->_buffet_position = 0;
        student->_id_buffet = self->_id;
        return TRUE;
    }
    pthread_mutex_unlock(mutex);
    return FALSE;
}

void entra_buffet(student_t* student)
{
    buffet_t* buffets = globals_get_buffets();
    int qtdBuffets = globals_get_qtd_buffets();
    while (1) 
    {
        for (int i = 0; i < qtdBuffets; i++) 
        {
            buffet_t* b = &buffets[i];
            if (
                buffet_queue_insert(b, student, 'L') ||
                buffet_queue_insert(b, student, 'R')
            ) return;
        }
    }
}

int pega_comida(buffet_t* buffet, student_t* student)
{
    int pos = student->_buffet_position;
    if (student->_wishes[pos] == 1)
    {
        pthread_mutex_t* mutex = &buffet->mutexComida[pos];
        pthread_mutex_lock(mutex);
        if (buffet->_meal[pos] == 0) 
        {
            pthread_mutex_unlock(mutex);
            return FALSE;    
        }
        buffet->_meal[pos] -= 1;
        pthread_mutex_unlock(mutex);
        student->_wishes[pos] = 0;
    }
    return TRUE;
}

void buffet_next_step(buffet_t *self, student_t *student)
{
    buffet_t* buffet = &self[student->_id_buffet];
    int* queue = student->left_or_right == 'L' ? buffet->queue_left : buffet->queue_right;
    int* pos = &student->_buffet_position;
    if (pega_comida(buffet, student) == FALSE) 
        return;

    if (*pos == 4) 
    {
        queue[*pos] = 0;
        *pos += 1;
    } 
    else if (queue[*pos+1] == 0) 
    {
        if (*pos == 0) sem_post(globals_get_sem_buffets_livres());
        queue[*pos] = 0;
        *pos += 1;
        queue[*pos] = student->_id;
    }
}

/* --------------------------------------------------------- */
/* ATENÇÃO: Não será necessário modificar as funções abaixo! */
/* --------------------------------------------------------- */

void buffet_finalize(buffet_t *self, int number_of_buffets)
{
    /* Espera as threads se encerrarem...*/
    for (int i = 0; i < number_of_buffets; i++)
    {
        pthread_join(self[i].thread, NULL);
        // Alterações feitas para finalizar os mutex criados dentro de buffet_t
        pthread_mutex_destroy(&self[i].mutexFilaDireita);
        pthread_mutex_destroy(&self[i].mutexFilaEsquerda);
        for (int j = 0u; j < 5; j++) 
        {
            pthread_mutex_destroy(&self[i].mutexComida[j]);
        }
    }
    
    /*Libera a memória.*/
    free(self);
}


void _log_buffet(buffet_t *self)
{
    /* Prints do buffet */
    int *ids_left = self->queue_left; 
    int *ids_right = self->queue_right; 

    printf(
        "\n\n\u250F\u2501 Queue left: [ %d %d %d %d %d ]\n", 
        ids_left[0],
        ids_left[1],
        ids_left[2],
        ids_left[3],
        ids_left[4]
    );
    fflush(stdout);
    printf(
        "\u2523\u2501 BUFFET %d = [RICE: %d/40 BEANS:%d/40 PLUS:%d/40 PROTEIN:%d/40 SALAD:%d/40]\n",
        self->_id, 
        self->_meal[0], 
        self->_meal[1], 
        self->_meal[2], 
        self->_meal[3], 
        self->_meal[4]
    );
    fflush(stdout);
    printf(
        "\u2517\u2501 Queue right: [ %d %d %d %d %d ]\n", 
        ids_right[0],
        ids_right[1],
        ids_right[2],
        ids_right[3],
        ids_right[4]
    );
    fflush(stdout);
}