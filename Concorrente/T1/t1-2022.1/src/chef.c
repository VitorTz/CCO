#include <stdlib.h>

#include "chef.h"
#include "config.h"
#include "globals.h"

void *chef_run()
{
    // Executa enquanto existem estudantes se servindo
    while (globals_get_todos_serviram() == FALSE)
    {
        chef_check_food();
        msleep(globals_get_sleep_time());
    }
    
    pthread_exit(NULL);
}

void chef_check_food()
{
    buffet_t* buffets = globals_get_buffets();
    if (buffets != NULL) 
    {
        for (int i = 0u; i < globals_get_qtd_buffets(); i++) 
        {
            buffet_t* buffet = &buffets[i];
            for (int j = 0u; j < 5; j++) 
            {
                if (buffet->_meal[j] == 0)
                    buffet->_meal[j] = 40;
            }
        }
    }
}

/* --------------------------------------------------------- */
/* ATENÇÃO: Não será necessário modificar as funções abaixo! */
/* --------------------------------------------------------- */

void chef_init(chef_t *self)
{
    pthread_create(&self->thread, NULL, chef_run, NULL);
}

void chef_finalize(chef_t *self)
{
    pthread_join(self->thread, NULL);
    free(self);
}