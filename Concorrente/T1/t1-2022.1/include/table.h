#ifndef __TABLE_H__
#define __TABLE_H__

typedef struct table_t
{
        int _id;                         /* ID da mesa */
        int _empty_seats;               /* Quantidade de lugares vazios */
        int _max_seats;                 /* Capacidade máxima de cada mesa*/
} table_t; 


/**
 * @brief Cada mesa tem um mutex especifico. Percorre todas as mesas 
 *        fazendo um lock e unlock nelas até que encontre uma mesa com lugar vago.
 *        Ao encontrar irá decrementar o número de lugares vagos na mesa
 *        e irá retornar a mesa.
 * 
 * @param tables 
 * @return table_t* 
 */
extern table_t* encontra_mesa(table_t* tables); 

/**
* @brief Inicia uma mesa.
* 
* @param self 
*/

extern table_t *table_init(int number_of_tables, int seats_per_table);

#endif