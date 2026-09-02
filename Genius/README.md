# Jogo Genius em C - Fila Dinâmica

Este repositório contém a implementação em **C** do clássico jogo Genius. A estrutura de dados base do projeto é uma Fila Dinâmica Encadeada, criada do zero utilizando `structs` e manipulação explícita de ponteiros, respeitando o princípio FIFO (First In, First Out).

## 🛠️ Instruções para Compilação e Execução

1. Certifique-se de ter um compilador C instalado (como `gcc` no Linux/Mac ou `MinGW` no Windows).
2. Clone o repositório utilizando:
   `git clone <link-do-repositorio>`
3. Navegue até o diretório do projeto:
   `cd <nome-do-diretorio>`
4. Compile o código-fonte via terminal executando:
   `gcc genius_fila.c -o genius`
5. Execute o jogo:
   - **No Linux/Mac:** `./genius`
   - **No Windows:** `genius.exe`

## 🎮 Exemplo de Execução

```text
=== JOGO GENIUS ===
1. Iniciar nova partida
2. Sair
Escolha uma opcao: 1

--- Rodada 1 ---
Memorize a sequencia:
VERDE

(Após 3 segundos a tela é limpa)
Sua vez! Digite a sequencia na ordem correta.
Opcoes validas: VERDE, VERMELHO, AZUL, AMARELO

1ª cor: VERDE

[V] Correto! Pontuacao atual: 1

--- Rodada 2 ---
Memorize a sequencia:
VERDE -> AZUL

(Após 3 segundos a tela é limpa)
Sua vez! Digite a sequencia na ordem correta.
Opcoes validas: VERDE, VERMELHO, AZUL, AMARELO

1ª cor: VERDE
2ª cor: VERMELHO

[X] Sequencia Incorreta!
Fim de jogo. Pontuacao final: 1