#ifndef __buffet_H__
#define __buffet_H__

#include <pthread.h>
#include "queue.h"


typedef struct buffet
{
    int _id;
    int _meal[5];

    int queue_left[5];
    int queue_right[5];
    pthread_mutex_t mutexComida[5];
    pthread_mutex_t mutexFilaEsquerda;
    pthread_mutex_t mutexFilaDireita;
    pthread_t thread; /* Thread do buffet   */
} buffet_t;


/**
 * @brief Coloca o estudante em um lado de algum buffet.
 *          A entrada de estudantes no RU é limitada pelos tokens
 *        no semaforo semBuffetsLivres. Este semaforo é iniciado
 *        com o número de entradas livres nos buffets, que é
 *        igual a qtdBuffets * 2 (uma entrada em cada lado dos buffets). 
 *          Apenas o worker gate faz um wait em semBuffetsLivres,
 *        deste modo, o worker gate permite que o primeiro da fila só entre
 *        se existe um lugar vago no inicio de algum buffet. 
 *          Ao entrar o irá procurar por um buffet livre.
 *          Após encontrar irá entrar na fila e tornará o buffet inválido
 *        para receber novos estudantes. Quando passar da posição
 *        0 para a posição 1 (dentro do buffet) irá fazer um post em 
 *        semBuffetsLivres indicando que existe mais uma entrada de buffet livre.
 *        O estudante sabe que pode entrar no RU quando recebe um post em 
 *        seu semaforo binário semPodeEntrarRu iniciado com valor 0.
 *        O post em semPodeEntrarRu é feito apenas por worker gate e após
 *        fazer um wait em semBuffetsLivres       
 *        O papel desta função é encontrar um buffet para o estudante que 
 *        recebeu permissão para entra no RU e se servir
 * 
 * @param student 
 */
extern void entra_buffet(student_t* student);

/**
 * @brief Retorna FALSE caso falhe em pegar a comida que deseja
 *        TRUE nos outros casos (não quer pegar a comida ou pegou a comida)
 *        Cada bacia de cada buffet possui um mutex especifico
 *        A função fará uso desse mutex para pegar a comida caso seja 
 *        necessário.
 * @param buffet 
 * @param student 
 * @return int 
 */
extern int pega_comida(buffet_t* buffet, student_t* student);

/**
 * @brief Thread do buffet.
 * 
 * @return void* 
 */
extern void* buffet_run();

/**
 * @brief Inicia o buffet
 * 
 */
extern void buffet_init(buffet_t *self, int number_of_buffets);

/**
 * @brief Encerra o buffet
 * 
 */
extern void buffet_finalize(buffet_t *self, int number_of_buffets);

/**
 * @brief Faz o estudante andar na fila do buffet. Aqui, quando o estudante 
 *        passa da posição 0 para a posição 1 então é feito um post em semBUffetsLivres
 *        indicando que existe mais um buffet livre para entrar
 * 
 * @param self 
 * @param student 
 */
extern void buffet_next_step(buffet_t *self, student_t *student);

/**
 * @brief Retorna TRUE quando inseriu um estudante com sucesso no fim da fila do buffet. 
 *        Retorna FALSE, caso contrário.
 * 
 */
extern int buffet_queue_insert(buffet_t *self, student_t *student, char lado);

/**
 * @brief Referências para funções privadas ao arquivo.
 * 
 * @param self 
 */
void _log_buffet(buffet_t *self);

#endif