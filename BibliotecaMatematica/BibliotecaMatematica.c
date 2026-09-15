#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_VETORES 50

/* --- ESTRUTURA DE DADOS: ARRAY --- */

typedef struct {
    float *elementos;
    int capacidade;
    int tamanho;
} Array;

void inicializar_array(Array *arr, int capacidade) {
    arr->elementos = (float *)malloc(capacidade * sizeof(float));
    if (arr->elementos == NULL) {
        printf("Erro de alocacao de memoria.\n");
        exit(1);
    }
    arr->capacidade = capacidade;
    arr->tamanho = 0;
}

int inserir(Array *arr, float valor) {
    if (arr->tamanho < arr->capacidade) {
        arr->elementos[arr->tamanho] = valor;
        arr->tamanho++;
        return 1; 
    }
    return 0; 
}

void imprimir(Array *arr) {
    printf("[");
    for (int i = 0; i < arr->tamanho; i++) {
        printf("%.4f", arr->elementos[i]);
        if (i < arr->tamanho - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}

int buscar(Array *arr, float valor) {
    for (int i = 0; i < arr->tamanho; i++) {
        if (arr->elementos[i] == valor) {
            return i; 
        }
    }
    return -1; 
}

int remover(Array *arr, int indice) {
    if (indice < 0 || indice >= arr->tamanho) {
        return 0; 
    }
    for (int i = indice; i < arr->tamanho - 1; i++) {
        arr->elementos[i] = arr->elementos[i + 1];
    }
    arr->tamanho--;
    return 1; 
}

void liberar_array(Array *arr) {
    if (arr->elementos != NULL) {
        free(arr->elementos);
        arr->elementos = NULL;
    }
    arr->tamanho = 0;
    arr->capacidade = 0;
}


/* --- OPERAÇÕES MATEMÁTICAS --- */

Array multiplicar_escalar(Array *A, float k) {
    Array B;
    inicializar_array(&B, A->tamanho);
    for (int i = 0; i < A->tamanho; i++) {
        inserir(&B, A->elementos[i] * k);
    }
    return B;
}

Array somar_vetores(Array *A, Array *B, int *sucesso) {
    Array C;
    if (A->tamanho != B->tamanho) {
        *sucesso = 0;
        return C;
    }
    *sucesso = 1;
    inicializar_array(&C, A->tamanho);
    for (int i = 0; i < A->tamanho; i++) {
        inserir(&C, A->elementos[i] + B->elementos[i]);
    }
    return C;
}

float produto_escalar(Array *A, Array *B, int *sucesso) {
    if (A->tamanho != B->tamanho) {
        *sucesso = 0;
        return 0.0f;
    }
    *sucesso = 1;
    float soma = 0.0f;
    for (int i = 0; i < A->tamanho; i++) {
        soma += A->elementos[i] * B->elementos[i];
    }
    return soma;
}

float norma(Array *A) {
    float soma = 0.0f;
    for (int i = 0; i < A->tamanho; i++) {
        soma += A->elementos[i] * A->elementos[i];
    }
    return sqrt(soma);
}

float similaridade_cosseno(Array *A, Array *B, int *sucesso) {
    if (A->tamanho != B->tamanho) {
        *sucesso = 0; 
        return 0.0f;
    }
    float norm_A = norma(A);
    float norm_B = norma(B);
    
    if (norm_A == 0.0f || norm_B == 0.0f) {
        *sucesso = -1; 
        return 0.0f;
    }
    
    *sucesso = 1;
    int p_sucesso;
    float prod = produto_escalar(A, B, &p_sucesso);
    return prod / (norm_A * norm_B);
}

/* --- INTERFACE E SISTEMA --- */

void limpar_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main() {
    Array vetores[MAX_VETORES];
    int qtd_vetores = 0;
    int opcao = -1;

    while (opcao != 0) {
        printf("\n=== ANALISE DE DADOS COM VETORES ===\n");
        printf("1. Criar novo vetor\n");
        printf("2. Exibir vetores armazenados\n");
        printf("3. Multiplicar vetor por escalar\n");
        printf("4. Somar dois vetores\n");
        printf("5. Calcular produto escalar\n");
        printf("6. Calcular norma de um vetor\n");
        printf("7. Calcular similaridade de cosseno\n");
        printf("8. Encontrar vetor mais similar a uma consulta\n");
        printf("9. Buscar elemento em um vetor (Estrutura Array)\n");
        printf("10. Remover elemento de um vetor (Estrutura Array)\n");
        printf("0. Sair\n");
        printf("Escolha uma opcao: ");
        
        if (scanf("%d", &opcao) != 1) {
            limpar_buffer();
            continue;
        }

        if (opcao == 1) {
            if (qtd_vetores >= MAX_VETORES) {
                printf("Capacidade maxima de vetores atingida!\n");
                continue;
            }
            int tam;
            printf("Informe o tamanho (dimensao) do vetor: ");
            scanf("%d", &tam);
            
            inicializar_array(&vetores[qtd_vetores], tam);
            
            for (int i = 0; i < tam; i++) {
                float valor;
                printf("Informe o valor da posicao %d: ", i);
                scanf("%f", &valor);
                inserir(&vetores[qtd_vetores], valor);
            }
            printf("Vetor %d criado com sucesso!\n", qtd_vetores);
            qtd_vetores++;

        } else if (opcao == 2) {
            printf("\n--- Vetores Armazenados ---\n");
            for (int i = 0; i < qtd_vetores; i++) {
                printf("Vetor %d: ", i);
                imprimir(&vetores[i]);
            }
            if (qtd_vetores == 0) printf("Nenhum vetor armazenado.\n");

        } else if (opcao == 3) {
            int id;
            float k;
            printf("ID do vetor (0 a %d): ", qtd_vetores - 1);
            scanf("%d", &id);
            printf("Valor do escalar: ");
            scanf("%f", &k);
            
            if (id >= 0 && id < qtd_vetores) {
                Array res = multiplicar_escalar(&vetores[id], k);
                printf("Resultado: ");
                imprimir(&res);
                liberar_array(&res); 
            } else {
                printf("ID invalido.\n");
            }

        } else if (opcao == 4) {
            int id1, id2, sucesso;
            printf("ID do vetor A: "); scanf("%d", &id1);
            printf("ID do vetor B: "); scanf("%d", &id2);
            
            if (id1 >= 0 && id1 < qtd_vetores && id2 >= 0 && id2 < qtd_vetores) {
                Array res = somar_vetores(&vetores[id1], &vetores[id2], &sucesso);
                if (sucesso) {
                    printf("Soma (A + B): ");
                    imprimir(&res);
                    liberar_array(&res);
                } else {
                    printf("Erro: Vetores de dimensoes diferentes nao podem ser somados.\n");
                }
            }

        } else if (opcao == 5) {
            int id1, id2, sucesso;
            printf("ID do vetor A: "); scanf("%d", &id1);
            printf("ID do vetor B: "); scanf("%d", &id2);
            
            if (id1 >= 0 && id1 < qtd_vetores && id2 >= 0 && id2 < qtd_vetores) {
                float res = produto_escalar(&vetores[id1], &vetores[id2], &sucesso);
                if (sucesso) {
                    printf("Produto escalar: %.4f\n", res);
                } else {
                    printf("Erro: Dimensoes incompativeis.\n");
                }
            }

        } else if (opcao == 6) {
            int id;
            printf("ID do vetor: "); scanf("%d", &id);
            if (id >= 0 && id < qtd_vetores) {
                printf("Norma Euclidiana: %.4f\n", norma(&vetores[id]));
            }

        } else if (opcao == 7) {
            int id1, id2, sucesso;
            printf("ID do vetor A: "); scanf("%d", &id1);
            printf("ID do vetor B: "); scanf("%d", &id2);
            
            if (id1 >= 0 && id1 < qtd_vetores && id2 >= 0 && id2 < qtd_vetores) {
                float res = similaridade_cosseno(&vetores[id1], &vetores[id2], &sucesso);
                if (sucesso == 1) {
                    printf("Similaridade de Cosseno: %.4f\n", res);
                } else if (sucesso == -1) {
                    printf("Erro: Operacao invalida. Um dos vetores e nulo.\n");
                } else {
                    printf("Erro: Dimensoes incompativeis.\n");
                }
            }

        } else if (opcao == 8) {
            if (qtd_vetores < 2) {
                printf("Erro: E necessario pelo menos 2 vetores para esta operacao.\n");
                continue;
            }
            int id_consulta;
            printf("ID do vetor de consulta: "); scanf("%d", &id_consulta);
            
            if (id_consulta >= 0 && id_consulta < qtd_vetores) {
                int max_id = -1;
                float max_sim = -2.0f;
                
                for (int i = 0; i < qtd_vetores; i++) {
                    if (i == id_consulta) continue;
                    int sucesso;
                    float sim = similaridade_cosseno(&vetores[id_consulta], &vetores[i], &sucesso);
                    if (sucesso == 1 && sim > max_sim) {
                        max_sim = sim;
                        max_id = i;
                    }
                }
                
                if (max_id != -1) {
                    printf("Vetor mais similar: %d (Similaridade: %.4f)\n", max_id, max_sim);
                    printf("Valores do vetor: ");
                    imprimir(&vetores[max_id]);
                } else {
                    printf("Nao foi possivel encontrar um vetor similar (vetores incompativeis ou nulos).\n");
                }
            }

        } else if (opcao == 9) {
            int id;
            float valor;
            printf("ID do vetor: "); scanf("%d", &id);
            if (id >= 0 && id < qtd_vetores) {
                printf("Valor a buscar: "); scanf("%f", &valor);
                int indice = buscar(&vetores[id], valor);
                if (indice != -1) {
                    printf("Valor encontrado no indice %d do vetor.\n", indice);
                } else {
                    printf("Valor nao encontrado.\n");
                }
            }

        } else if (opcao == 10) {
            int id, idx_remover;
            printf("ID do vetor: "); scanf("%d", &id);
            if (id >= 0 && id < qtd_vetores) {
                printf("Indice a ser removido (0 a %d): ", vetores[id].tamanho - 1); 
                scanf("%d", &idx_remover);
                int sucesso = remover(&vetores[id], idx_remover);
                if (sucesso) {
                    printf("Elemento removido. Novo estado do vetor: ");
                    imprimir(&vetores[id]);
                } else {
                    printf("Indice invalido.\n");
                }
            }
        }
    }

    for (int i = 0; i < qtd_vetores; i++) {
        liberar_array(&vetores[i]);
    }
    printf("Sistema encerrado.\n");
    return 0;
}