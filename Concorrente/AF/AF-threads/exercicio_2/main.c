#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <pthread.h>

// Lê o conteúdo do arquivo filename e retorna um vetor E o tamanho dele
// Se filename for da forma "gen:%d", gera um vetor aleatório com %d elementos
//
// +-------> retorno da função, ponteiro para vetor malloc()ado e preenchido
// | 
// |         tamanho do vetor (usado <-----+
// |         como 2o retorno)              |
// v                                       v
double* load_vector(const char* filename, int* out_size);


// Avalia o resultado no vetor c. Assume-se que todos os ponteiros (a, b, e c)
// tenham tamanho size.
void avaliar(double* a, double* b, double* c, int size);

// Guarda os vetores 
typedef struct Vetores Vetores;
struct Vetores {
    double* vetorA;
    double* vetorB;
    double* vetorResultado;
};

// Guarda os arrays a, b e c e os intervalos onde a thread poderá operar neles
typedef struct InfoThread InfoThread;
struct InfoThread {
    int comeco, fim;
    Vetores* vets;
};

// Faz a thread somar os valores de a e b em um determinado intervalo
void* operacaoThread(void* arg) {
    InfoThread* info = (InfoThread*) arg;
    // Cada thread acessa um intervalor único dentro de vetorResultado
    for (int i = info->comeco; i < info->fim; i++) {
        info->vets->vetorResultado[i] = info->vets->vetorA[i] + info->vets->vetorB[i];
    }
    pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
    // Gera um resultado diferente a cada execução do programa
    // Se **para fins de teste** quiser gerar sempre o mesmo valor
    // descomente o srand(0)
    srand(time(NULL)); //valores diferentes
    //srand(0);        //sempre mesmo valor

    //Temos argumentos suficientes?
    if(argc < 4) {
        printf("Uso: %s n_threads a_file b_file\n"
               "    n_threads    número de threads a serem usadas na computação\n"
               "    *_file       caminho de arquivo ou uma expressão com a forma gen:N,\n"
               "                 representando um vetor aleatório de tamanho N\n",
               argv[0]);
        return 1;
    }
  
    //Quantas threads?
    int n_threads = atoi(argv[1]);
    if (!n_threads) {
        printf("Número de threads deve ser > 0\n");
        return 1;
    }
    //Lê números de arquivos para vetores alocados com malloc
    int a_size = 0, b_size = 0;
    double* a = load_vector(argv[2], &a_size);
    if (!a) {
        //load_vector não conseguiu abrir o arquivo
        printf("Erro ao ler arquivo %s\n", argv[2]);
        return 1;
    }
    double* b = load_vector(argv[3], &b_size);
    if (!b) {
        printf("Erro ao ler arquivo %s\n", argv[3]);
        return 1;
    }
    
    //Garante que entradas são compatíveis
    if (a_size != b_size) {
        printf("Vetores a e b tem tamanhos diferentes! (%d != %d)\n", a_size, b_size);
        return 1;
    }
    //Cria vetor do resultado 
    double* c = malloc(a_size*sizeof(double));

    // ## =====================================  Solução  ===================================== ##
 
    // Limita o número de threads para o tamanho dos vetores a e b
    if (n_threads > a_size) {
        n_threads = a_size;
    }

    // Define a quantidade de operações que cada thread irá fazer. 
    const int qtdSomasPorThread = a_size / n_threads;

    pthread_t* threads = (pthread_t*) malloc(sizeof(pthread_t)*n_threads);
    // Informação que cada thread terá para calcular uma parcela da soma
    InfoThread* infoThreads = (InfoThread*) malloc(sizeof(InfoThread)*n_threads);  
    // Guarda os vetores a serem operados.
    Vetores vetores = {a, b, c};

    // Define o intervalo em que cada thread poderá acessar os arrays a, b e c
    for (int i = 0; i < n_threads; i++) {
        infoThreads[i].vets = &vetores;
        infoThreads[i].comeco = i * qtdSomasPorThread;
        if (i + 1 == n_threads) {
            infoThreads[i].fim = a_size;
        } else {
            infoThreads[i].fim = infoThreads[i].comeco + qtdSomasPorThread;
        }
    }

    for (int i = 0; i < n_threads; i++) {
       pthread_create(&threads[i], NULL, operacaoThread, &infoThreads[i]);
    }

    for (int i = 0; i < n_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    // avaliar(a, b, c, a_size);

    //Importante: libera memória
    free(a);
    free(b);
    free(c);
    free(threads);
    free(infoThreads);
    return 0;
}
