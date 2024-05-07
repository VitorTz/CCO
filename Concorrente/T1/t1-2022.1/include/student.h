#ifndef __STUDENT_H__
#define __STUDENT_H__

#include <pthread.h>
#include <semaphore.h>
#include "table.h"

typedef struct student
{
    int _id;                                /* Id do aluno */
    int _wishes[5];                         /* salada, arroz, feijão, acompanhamento, proteína */
    int _buffet_position;                   /* Posição na fila do buffet*/
    int _id_buffet;                         /* Qual buffet o estudante está alocado?*/
    int _id_mesa;
    char left_or_right;                     /* Fila da esquerda(L) ou da direita(R)*/
    sem_t semPodeEntrarRu;
    pthread_t thread;                       /* A thread */
} student_t;

/**
* @brief Inicializa um estudente.
* 
* @return student_t* 
*/
student_t *student_init();

/**
* @brief Libera o espaço em memória de um estudante
* 
* @param self 
*/
extern void student_finalize (student_t *self);

/**
* @brief Thread com a lógica para cada aluno.
* 
* @param arg 
* @return void* 
*/
extern void *student_run(void *arg);

/**
* @brief Função que chama a criação das threads dos alunos. 
* 
* @param number_students 
* @return pthread_t 
*/
extern pthread_t students_come_to_lunch(int number_students);

/**
* @brief Aqui, o estudante já se serviu e agora está fazendo um wait em semLugaresVagos
*        a espera de um lugar vago para se sentar. Ao passar pelo wait o estudante
*        tem certeza que existe pelo menos uma mesa com lugar vago e vai a procura dela.
*        A procura é feita executando a função encontra_mesa(), está função irá percorrer
*        todas as mesas até encontrar uma com lugar vago.
* @param self 
* @param table 
*/
extern void student_seat (student_t *self, table_t *table);

/**
* @brief Todos os estudantes estão fazendo um wait em seus respectivos semaforos
*         semPodeEntrarRu. O worker gate verifica se um estudante pode entrar no RU, caso sim
*         retira o primeiro estudante da fila e faz um post em seu semPodeEntrarRu.
*         Após o post feito pelo worker gate permitindo que o estudante entre está 
*         função será executada. Aqui, o estudante irá procurar e entrar em um
*         buffet é o percorrerá até o fim.
* @param self 
*/
extern void student_serve (student_t *self);


/**
* @brief Estudante incrementa o número de lugares vagos na mesa em que estava 
*        sentado e o número de estudantes que sairam do RU e então deixa o restaurante.
*        Também faz um post em semLugaresVagos
* 
* @param self 
*/
extern void student_leave (student_t *self, table_t *table);

/**
 * @brief Referências para funções privadas ao arquivo.
 * 
 * @param self 
 */
void* _all_they_come(void *arg);
int _student_choice();

#endif /*__STUDENT_H__*/