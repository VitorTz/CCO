#ifndef __WORKER_GATE_H__
#define __WORKER_GATE_H__

#include <pthread.h>
#include "student.h"

typedef struct worker_gate
{
    
    pthread_t thread; // A thread do funcionário que fica na catraca.

} worker_gate_t;


/**
 * @brief Inicia o funcionário que fica na catraca.
 * 
 * @param self 
 */
extern void worker_gate_init(worker_gate_t *self);

/**
 * @brief Finaliza a thread do funcionário que fica na catraca.
 * 
 * @param self 
 */
extern void worker_gate_finalize(worker_gate_t *self);

/**
 * @brief Thread do funcionário que fica na catraca.
 * 
 * @return void* 
 */
extern void* worker_gate_run();

/**
 * @brief Caso existam estudantes na fila esperando para entrar então
 *       faz um wait em semBuffetsLivres para poder liberar um estudante para
 *       ir para os buffets. Um estudante é liberado quando um post é feito
 *       em seu semaforo semPodeEntrarRu.
 * 
 */
extern void worker_gate_remove_queue_student();

/**
 * @brief Insere um novo estudante na fila usando o mutex da fila
 * 
 */
extern void worker_gate_insert_queue_buffet(student_t *student);

#endif