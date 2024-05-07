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


// Avalia se o prod_escalar é o produto escalar dos vetores a e b. Assume-se
// que ambos a e b sejam vetores de tamanho size.
void avaliar(double* a, double* b, int size, double prod_escalar);


typedef struct Vetores Vetores;
struct Vetores {
    double* vetorA;
    double* vetorB;
    double* vetorResultante;
};

// Será passado para as threads.
typedef struct Operacao Operacao;
struct Operacao {
    int comeco, fim, n_thread;
    Vetores* vets;
};

// Cada thread calcula uma parcela do produto escalar 
void* produtoEscalar(void* operacao) {
    Operacao* op = (Operacao*) operacao;
    op->vets->vetorResultante[op->n_thread] = 0.0;  // n_thread é único para cada thread
    for (int i = op->comeco; i < op->fim; i++) {
        op->vets->vetorResultante[op->n_thread] += op->vets->vetorA[i] * op->vets->vetorB[i];
    }
    pthread_exit(NULL);
}


int main(int argc, char* argv[]) {
    srand(time(NULL));

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

    // ## =====================================  Solução  ===================================== ##
    /*
        Para n = número de threads
        1 - Criar um array de tamanho n chamado vetorResultante.
        2 - Criar n threads, cada thread irá calcular uma parcela do 
        produto escalar e armazenar o valor em uma posição única dentro do vetorResultante.
        3 - Somar os valores em vetorResultante para obter o produto escalar total.
    */

    // Define um limite para o número de threads
    if (n_threads > a_size) {
        n_threads = a_size;   
    }
    // Define quantas multiplicações cada thread precisa fazer
    int qtdMultiplicacoesPorThread = a_size / n_threads;
    
    // Vetor que recebe o produto escalar de cada parcela calculada por cada thread
    double* vetorResultante = (double*) malloc(sizeof(double)*n_threads);

    pthread_t* threads = (pthread_t*) malloc(sizeof(pthread_t)*n_threads);
    // Armazena as informações necessárias para cada parcela do produto escalar
    Operacao* operacoes = (Operacao*) malloc(sizeof(Operacao)*n_threads);
    // Vetores usados para calcular o produto escalar
    Vetores vetores = {a, b, vetorResultante};

    for (int i = 0; i < n_threads; i++) {
        // Identifica a posição no vetorResultante onde a thread deve armazenar o valor de sua parcela do produto escalar 
        operacoes[i].n_thread = i; 
        // Define os vetores para o calculo do produto escalar
        operacoes[i].vets = &vetores;
        // Define o começo e fim da parcela do produto escalar que a thread irá calcular
        operacoes[i].comeco = i * qtdMultiplicacoesPorThread;
        if (i + 1 == n_threads) {
            operacoes[i].fim = a_size;
        } else {
            operacoes[i].fim = operacoes[i].comeco + qtdMultiplicacoesPorThread;
        }
    }

    for (int i = 0; i < n_threads; i++) {
        pthread_create(&threads[i], NULL, produtoEscalar, &operacoes[i]);
    }

    for (int i = 0; i < n_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    // Calcula o total de forma sequencial
    double result = 0.0;
    for (int i = 0; i < n_threads; i++) {
        result += vetorResultante[i];
    }
    
    // avaliar(a, b, a_size, result);

    //Libera memória
    free(a);
    free(b);
    free(vetorResultante);
    free(threads);
    free(operacoes);
    return 0;
}
