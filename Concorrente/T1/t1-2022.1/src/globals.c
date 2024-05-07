#include <stdlib.h>
#include "globals.h"

queue_t *students_queue = NULL;
table_t *table = NULL;
buffet_t *buffets_ref = NULL;

pthread_mutex_t mutexFilaEstudantes;
pthread_mutex_t* mutexMesa = NULL;
sem_t semBuffetsLivres;
sem_t semLugaresVagos;

pthread_mutex_t mutexQtdSairam;
pthread_mutex_t mutexQtdServiram;
int students_number = 0;
int qtdMesas = 0;
int qtdLugaresPorMesa = 0;
int qtdBuffets = 0;
int qtdEntraram = 0;
int qtdServiram = 0;
int qtdSairam = 0;
int todosEntraram = 0;
int todosServiram = 0;
int todosSairam = 0;
int sleepTime = 10;

void globals_init(int qtd_buffets)
{
    qtdBuffets = qtd_buffets;
    pthread_mutex_init(&mutexFilaEstudantes, NULL);
    pthread_mutex_init(&mutexQtdServiram, NULL);
    pthread_mutex_init(&mutexQtdSairam, NULL);
    sem_init(&semBuffetsLivres, 0, qtdBuffets * 2);
}

void globals_init_table(int qtd_mesas, int qtd_lugares)
{
    qtdMesas = qtd_mesas;
    qtdLugaresPorMesa = qtd_lugares;
    sem_init(&semLugaresVagos, 0, qtd_lugares * qtd_mesas);
    mutexMesa = malloc(sizeof(pthread_mutex_t)*qtd_mesas);
    for (int i = 0u; i < qtdMesas; i++)
        pthread_mutex_init(&mutexMesa[i], NULL);
}

void globals_finalize()
{
    pthread_mutex_destroy(&mutexFilaEstudantes);
    pthread_mutex_destroy(&mutexQtdServiram);
    pthread_mutex_destroy(&mutexQtdSairam);
    sem_destroy(&semBuffetsLivres);
    sem_destroy(&semLugaresVagos);
    for (int i = 0u; i < qtdMesas; i++)
        pthread_mutex_destroy(&mutexMesa[i]);
    free(table);
}


pthread_mutex_t* globals_get_mutex_mesa(int idMesa)
{
    return &mutexMesa[idMesa];
}

sem_t* globals_get_sem_lugares_vagos()
{
    return &semLugaresVagos;
}

sem_t* globals_get_sem_buffets_livres()
{
    return &semBuffetsLivres;
}

pthread_mutex_t* globals_get_mutex_fila_estudantes()
{
    return &mutexFilaEstudantes;
}

int globals_get_qtd_mesas()
{
    return qtdMesas;
}


int globals_get_sleep_time()
{
    return sleepTime;
}

void globals_incrementa_qtd_entraram()
{
    qtdEntraram += 1;
}

void globals_incrementa_qtd_serviram()
{
    pthread_mutex_lock(&mutexQtdServiram);
    qtdServiram += 1;
    if (qtdServiram == students_number) 
        todosServiram = 1;
    pthread_mutex_unlock(&mutexQtdServiram);
}

void globals_incrementa_qtd_sairam()
{
    pthread_mutex_lock(&mutexQtdSairam);
    qtdSairam += 1;
    if (qtdSairam == students_number) 
        todosSairam = 1;
    pthread_mutex_unlock(&mutexQtdSairam);
}


int globals_get_qtd_buffets()
{
    return qtdBuffets;
}

int globals_get_todos_entraram()
{
    return todosEntraram;
}

int globals_get_todos_serviram()
{
    return todosServiram;
}

int globals_get_todos_sairam()
{
    return todosSairam;
}
void globals_set_queue(queue_t *queue)
{
    students_queue = queue;
}

queue_t *globals_get_queue()
{
    return students_queue;
}

void globals_set_table(table_t *t)
{
    table = t;
}

table_t *globals_get_table()
{
    return table;
}


void globals_set_students(int number)
{
    students_number = number;
}

int globals_get_students()
{
    return students_number;
}

void globals_set_buffets(buffet_t *buffets)
{
    buffets_ref = buffets;
}

buffet_t *globals_get_buffets()
{
    return buffets_ref;
}

