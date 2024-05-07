#ifndef __GLOBALS_H__
#define __GLOBALS_H__

#include "queue.h"
#include "table.h"
#include "buffet.h"


/**
 * @brief Inicia algumas variáveis globais
 * 
 */
extern void globals_init();

/**
 * @brief Inicia a quantidade de mesas, lugares por mesa, semaforo com
 *        tokens para cada lugar vago nas mesas do RU e os mutex 
 *        especificos de cada mesa. Cada mesa possui um mutex.
 * 
 */
extern void globals_init_table();


/**
 * @brief Retorna a quantidade total de mesas no RU
 * 
 * @return int 
 */
extern int globals_get_qtd_mesas();

/**
 * @brief Retorna o mutex que protege a fila para entrar no RU
 * 
 * @return pthread_mutex_t* 
 */
extern pthread_mutex_t* globals_get_mutex_fila_estudantes();

/**
 * @brief Retorna o mutex especifico que protege alterações em uma mesa
 *        Cada mesa tem seu mutex
 * 
 * @param idMesa 
 * @return pthread_mutex_t* 
 */
extern pthread_mutex_t* globals_get_mutex_mesa(int idMesa);

/**
 * @brief Retorna o semaforo com os tokens para os buffets livres para entrar
 *        Cada lado de cada buffet é um token
 * @return sem_t* 
 */
extern sem_t* globals_get_sem_buffets_livres();

/**
 * @brief Retorna o semaforo com os tokens dos lugares vagos para sentar
 * 
 * @return sem_t* 
 */
extern sem_t* globals_get_sem_lugares_vagos();

/**
 * @brief Retorna o tempo de espera usado em msleep nas threads
 *        buffet, student e chef
 * 
 * @return int 
 */
extern int globals_get_sleep_time();

/**
 * @brief Retorna a quantidade total de buffets
 * 
 * @return int 
 */
extern int globals_get_qtd_buffets();

/**
 * @brief Verifica se todos os estudantes já entraram
 * 
 * @return int 
 */
extern int globals_get_todos_entraram();

/**
 * @brief Verifica se todos os estudantes já se serviram
 * 
 * @return int 
 */
extern int globals_get_todos_serviram();

/**
 * @brief Verifica se todos os estudantes já sairam
 * 
 * @return int 
 */
extern int globals_get_todos_sairam();

/**
 * @brief Incrementa de forma segura (usando um mutex especifico) a 
 *        quantidede de estudantes que entraram no RU
 *        É chamada unicamente pela thread worker gate
 * 
 */
extern void globals_incrementa_qtd_entraram();

/**
 * @brief Incrementa de forma segura (usando um mutex especifico) a 
 *        quantidede de estudantes que se serviram nos buffets
 *        É chamada por todas as threads de alunos quando estes saem do RU
 * 
 */
extern void globals_incrementa_qtd_serviram();

/**
 * @brief Incrementa de forma segura (usando um mutex especifico) a 
 *        quantidede de estudantes que sairam
 *        É chamada por todas as threads de alunos quando estes saem do RU
 * 
 */
extern void globals_incrementa_qtd_sairam();

/**
 * @brief Inicia uma fila (de modo global)
 * 
 * @param queue 
 */
extern void globals_set_queue(queue_t *queue);

/**
 * @brief Retorna uma fila (de modo global)
 * 
 * @return queue_t* 
 */
extern queue_t *globals_get_queue();

/**
 * @brief Insere o número de alunos (de modo global)
 * 
 */
extern void globals_set_students(int number);

/**
 * @brief Retorna o número de alunos (de modo global)
 * 
 * @return int 
 */

extern int globals_get_students();

/**
 * @brief Inicia um array de mesas (de modo global).
 * 
 * @param t 
 */
extern void globals_set_table(table_t *t);

/**
 * @brief Retorna um array de mesas (de modo global)
 * 
 * @return table_t* 
 */
extern table_t *globals_get_table();


/**
 * @brief Finaliza todas as variáveis globais.
 * 
 */
extern void globals_finalize();

/**
 * @brief Inicia um array de buffets (de modo global)
 * 
 */
extern void globals_set_buffets(buffet_t *buffets_ref);

/**
 * @brief Retorna um array de buffets (de modo global)
 * 
 * @return buffet_t* 
 */
extern buffet_t *globals_get_buffets();

#endif