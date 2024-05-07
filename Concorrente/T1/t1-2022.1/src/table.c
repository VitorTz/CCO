#include <stdlib.h>
#include "table.h"
#include "globals.h"


table_t* encontra_mesa(table_t* tables)
{
    while (1)
    {
        for (int i = 0u; i < globals_get_qtd_mesas(); i++)
        {
            table_t* t = &tables[i];
            pthread_mutex_t* mutex = globals_get_mutex_mesa(t->_id);
            pthread_mutex_lock(mutex);
            if (t->_empty_seats > 0)
            {
                t->_empty_seats -= 1;
                pthread_mutex_unlock(mutex);
                return t;
            }
            pthread_mutex_unlock(mutex);
        }
    }
}

/* --------------------------------------------------------- */
/* ATENÇÃO: Não será necessário modificar as funções abaixo! */
/* --------------------------------------------------------- */

table_t *table_init(int number_of_tables, int seats_per_table)
{
    globals_init_table(number_of_tables, seats_per_table);
    table_t *new_tables = malloc(sizeof(table_t) * number_of_tables);
    for (int i = 0; i < number_of_tables; i++)
    {
        new_tables[i]._id = i;
        new_tables[i]._empty_seats = seats_per_table;
        new_tables[i]._max_seats = seats_per_table;
    }

    return new_tables;
}