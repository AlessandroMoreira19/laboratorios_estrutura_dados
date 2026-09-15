# Torre de Hanói em Python - Pilha Dinâmica

Este repositório contém a implementação do clássico jogo **Torre de Hanói**, desenvolvida em **Python**. A estrutura de dados base do projeto é uma **Pilha Dinâmica Encadeada** criada do zero, utilizando o conceito de orientação a objetos (nós e referências) e obedecendo estritamente ao princípio LIFO (Last In, First Out). 

Nenhuma estrutura de lista nativa (`list`, `deque`) foi utilizada para armazenar a mecânica principal das torres.

## 🛠️ Instruções para Execução

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone o repositório utilizando:
   `git clone <link-do-repositorio>`
3. Navegue até o diretório do projeto:
   `cd <nome-do-diretorio>`
4. Execute o programa via terminal:
   `python hanoi.py` (ou `python3 hanoi.py`, dependendo do seu sistema).

## ⚙️ Operações da Pilha Implementadas

A lógica das torres depende inteiramente das seguintes operações manuais:

*   **`inicializar_pilha`**: Define o estado inicial da torre, configurando a referência do topo como nula (`None`) e a quantidade de discos para `0`.
*   **`empilhar` (Push)**: Instancia um novo nó contendo o disco, aponta o referencial `proximo` para o nó atual do topo e atualiza o novo nó como o topo da pilha.
*   **`desempilhar` (Pop)**: Remove e retorna o disco localizado no topo da pilha, deslocando a referência de topo para o próximo nó inferior (`self._topo.proximo`).
*   **`topo` (Peek)**: Retorna o valor (tamanho) do disco localizado no topo da pilha sem removê-lo, essencial para as validações de regra do jogo.
*   **`imprimir`**: Percorre a pilha a partir do topo até a base para exibir graficamente os discos na tela.

## 🎮 Exemplo de Execução

```text
*** BEM-VINDO À TORRE DE HANÓI ***
Mova todos os discos para a Torre 3.
Regras: Mova 1 disco por vez. Discos maiores não podem ficar sobre menores.

==============================
ESTADO DAS TORRES:
Torre 1: Topo -> 1 | 2 | 3 | 4 <- Base
Torre 2: [ Vazia ]
Torre 3: [ Vazia ]
==============================

Movimentos realizados: 0

Opções: [1-3] Selecionar Torre | [0] Reiniciar Jogo | [9] Sair
Torre de ORIGEM (1, 2 ou 3): 1
Torre de DESTINO (1, 2 ou 3): 3

[V] Sucesso: Disco 1 movido da Torre 1 para a Torre 3.