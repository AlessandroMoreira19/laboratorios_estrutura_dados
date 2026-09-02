#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>


typedef struct No {
    char cor[20];
    struct No* proximo;
} No;


typedef struct Fila {
    No* inicio;
    No* fim;
    int quantidade;
} Fila;


void inicializar_fila(Fila* f) {
    f->inicio = NULL;
    f->fim = NULL;
    f->quantidade = 0;
}

void enfileirar(Fila* f, const char* cor) {
    No* novo_no = (No*)malloc(sizeof(No));
    if (novo_no == NULL) {
        printf("Erro de alocacao de memoria.\n");
        exit(1);
    }
    strcpy(novo_no->cor, cor);
    novo_no->proximo = NULL;

    if (f->inicio == NULL) {
        f->inicio = novo_no;
    } else {
        f->fim->proximo = novo_no;
    }
    f->fim = novo_no;
    f->quantidade++;
}

void desenfileirar(Fila* f, char* corSaida) {
    if (f->inicio == NULL) {
        corSaida[0] = '\0';
        return;
    }
    No* no_remover = f->inicio;
    strcpy(corSaida, no_remover->cor);
    
    f->inicio = f->inicio->proximo;
    if (f->inicio == NULL) {
        f->fim = NULL;
    }
    f->quantidade--;
    free(no_remover);
}

void frente(Fila* f, char* corFrente) {
    if (f->inicio == NULL) {
        corFrente[0] = '\0';
        return;
    }
    strcpy(corFrente, f->inicio->cor);
}

void imprimir(Fila* f) {
    No* atual = f->inicio;
    while (atual != NULL) {
        printf("%s", atual->cor);
        if (atual->proximo != NULL) {
            printf(" -> ");
        }
        atual = atual->proximo;
    }
    printf("\n");
}


void para_maiusculo(char* str) {
    for (int i = 0; str[i]; i++) {
        str[i] = toupper((unsigned char)str[i]);
    }
}

void limpar_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}


void jogar() {
    Fila fila;
    inicializar_fila(&fila);
    
    const char* cores_disponiveis[] = {"VERDE", "VERMELHO", "AZUL", "AMARELO"};
    int pontuacao = 0;
    int jogando = 1;

    srand((unsigned int)time(NULL));

    while (jogando) {
        int indice_cor = rand() % 4;
        enfileirar(&fila, cores_disponiveis[indice_cor]);

        printf("\n--- Rodada %d ---\n", pontuacao + 1);
        printf("Memorize a sequencia:\n");
        imprimir(&fila);
        
        printf("\nPressione ENTER quando estiver pronto para digitar a sequencia...");
        getchar();    
        system("cls");

        printf("Sua vez! Digite a sequencia na ordem correta.\n");
        printf("Opcoes validas: VERDE, VERMELHO, AZUL, AMARELO\n\n");

        int errou = 0;
        int qtd_atual = fila.quantidade;
        char resposta[50];
        char cor_esperada[20];
        char lixo_saida[20];

        for (int i = 0; i < qtd_atual; i++) {
            frente(&fila, cor_esperada);
            desenfileirar(&fila, lixo_saida);

            if (!errou) {
                printf("%d cor: ", i + 1);
                scanf("%49s", resposta);
                limpar_buffer();
                para_maiusculo(resposta);

                if (strcmp(resposta, cor_esperada) != 0) {
                    errou = 1;
                }
            }

            enfileirar(&fila, cor_esperada);
        }

        if (errou) {
            printf("\n[X] Sequencia Incorreta!\n");
            printf("Fim de jogo. Pontuacao final: %d\n", pontuacao);
            jogando = 0;
        } else {
            pontuacao++;
            printf("\n[V] Correto! Pontuacao atual: %d\n", pontuacao);
        }
    }

    char lixo[20];
    while (fila.quantidade > 0) {
        desenfileirar(&fila, lixo);
    }
}

void menu() {
    char opcao[10];
    
    while (1) {
        printf("\n=== JOGO GENIUS ===\n");
        printf("1. Iniciar nova partida\n");
        printf("2. Sair\n");
        printf("Escolha uma opcao: ");
        
        scanf("%9s", opcao);
        limpar_buffer();

        if (strcmp(opcao, "1") == 0) {
            system("cls");
            jogar();
            printf("\nPressione ENTER para retornar ao menu...\n");
            getchar();
            system("cls");
        } else if (strcmp(opcao, "2") == 0) {
            printf("Encerrando o jogo...\n");
            break;
        } else {
            printf("Opcao invalida, tente novamente.\n");
        }
    }
}

int main() {
    system("cls");
    menu();
    return 0;
}