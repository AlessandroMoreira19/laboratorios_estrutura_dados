# Sistema de Gerenciamento de Pedidos com Max-Heap em Python

Este projeto implementa um sistema de gerenciamento de pedidos cuja fila de prioridades é gerenciada internamente por uma estrutura de dados do tipo **Max-Heap**. A implementação foi construída manualmente usando um vetor dinâmico e aritmética de índices para simular a árvore, respeitando estritamente a exigência de não usar a biblioteca `heapq`.

## 🛠️ Instruções para Execução

1. Certifique-se de ter o Python 3.x instalado.
2. Clone este repositório via terminal:
   `git clone <link-do-repositorio>`
3. Navegue até o diretório:
   `cd <nome-do-diretorio>`
4. Execute o programa:
   `python pedidos_heap.py` (ou `python3 pedidos_heap.py`).

## ⚙️ Descrição das Operações do Heap

O funcionamento do vetor baseia-se na propriedade onde o maior valor deve estar na raiz. Para um elemento no índice `i`, as regras são: `pai = (i - 1) // 2`, `esquerdo = 2 * i + 1`, `direito = 2 * i + 2`.

*   **`inicializar_heap`**: Configura o Max-Heap definindo sua capacidade inicial e pré-alocando o vetor de dados com espaços nulos. 
*   **`inserir`**: Adiciona o pedido na última posição disponível do vetor e verifica se sua capacidade excedeu. Em seguida, troca o novo elemento com o seu `pai` recursivamente para cima até restaurar a propriedade da árvore.
*   **`remover`**: Extrai e retorna o pedido na raiz (posição 0, de maior prioridade). O último elemento do vetor é movido para a raiz, e então empurrado recursivamente para baixo (`max_heapfy`) até estabilizar a árvore.
*   **`max_heapfy`**: Compara um nó com seus filhos esquerdos e direitos. Se um dos filhos possuir prioridade maior, ele troca de posição com o pai e chama a função novamente para a nova posição.
*   **`construir`**: Dado um vetor não-ordenado de pedidos, aplica a função `max_heapfy` de baixo para cima (partindo do último nó que possui filhos até a raiz), garantindo complexidade ótima na montagem do Heap (O(n)).
*   **`print_heap`**: Percorre o estado real do vetor do índice 0 ao último ocupado, exibindo a disposição linear da árvore no array.

## 🎮 Exemplos de Execução

Ao iniciar o programa com um lote inicial via opção 5, a operação `construir` organizará as prioridades:

```text
===== SISTEMA DE PEDIDOS =====
[...]
Escolha: 5

--- CONSTRUIR HEAP (LOTE INICIAL) ---
Heap construído com sucesso a partir do lote de 5 pedidos!
ID: 4 | Prioridade: 8 | Descrição: Pedido D
ID: 2 | Prioridade: 5 | Descrição: Pedido B
ID: 3 | Prioridade: 3 | Descrição: Pedido C
ID: 1 | Prioridade: 2 | Descrição: Pedido A
ID: 5 | Prioridade: 1 | Descrição: Pedido E

Escolha: 2

--- ATENDIMENTO ---
Pedido atendido:
ID: 4
Descrição: Pedido D
Prioridade: 8

Pedidos restantes no Heap:
ID: 2 | Prioridade: 5 | Descrição: Pedido B
ID: 1 | Prioridade: 2 | Descrição: Pedido A
ID: 3 | Prioridade: 3 | Descrição: Pedido C
ID: 5 | Prioridade: 1 | Descrição: Pedido E