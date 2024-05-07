#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>



//       (pai)      
//         |        
//    +----+----+
//    |         |   
// filho_1   filho_2


// ~~~ printfs  ~~~
// pai (ao criar filho): "Processo pai criou %d\n"
//    pai (ao terminar): "Processo pai finalizado!\n"
//  filhos (ao iniciar): "Processo filho %d criado\n"

// Obs:
// - pai deve esperar pelos filhos antes de terminar!


void processoFilho(const pid_t pid_filho) {
    printf("Processo filho %d criado\n", pid_filho);
    exit(0);
}

void processoPai(const pid_t pid_filho) {
    printf("Processo pai criou %d\n", pid_filho);
}

void criaFilho(const pid_t pid_pai) {
    pid_t pid_filho = fork();
    if (pid_filho >= 0) {
        if (pid_filho == 0) {
            processoFilho(getpid());
        } else {
            processoPai(pid_filho);
        }
    }
    while(wait(NULL) >= 0);
}

void criaFilhos(const pid_t pid_pai, const int qtdFilhos) {
    for (int i = 0; i < qtdFilhos; i++) {
        criaFilho(pid_pai);
    }
} 

int main(int argc, char** argv) {

    // ....

    /*************************************************
     * Dicas:                                        *
     * 1. Leia as intruções antes do main().         *
     * 2. Faça os prints exatamente como solicitado. *
     * 3. Espere o término dos filhos                *
     *************************************************/
    criaFilhos(getpid(), 2);
    printf("Processo pai finalizado!\n");
    return 0;
}
