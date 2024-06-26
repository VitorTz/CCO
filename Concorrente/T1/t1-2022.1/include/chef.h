#ifndef __chef_H__
#define __chef_H__

#include <pthread.h>

typedef struct chef
{
    pthread_t thread;
} chef_t;


/**
* @brief Inicializa a thread do chef.
* 
* @param  none
*/
extern void chef_init(chef_t *self);                           

/**
 * @brief Finaliza a thread do chef.
 * 
 * @param self 
 */
extern void chef_finalize(chef_t *self);

/**
* @brief Função de thread do chef.
* 
* @param  none
*/
extern void* chef_run();

/**
* @brief Passa por todos os buffets e faz a reposição das bacias sem comida.
* 
* @param  none
*/                  
extern void chef_check_food();


#endif