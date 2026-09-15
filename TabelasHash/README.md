# Tabela Hash - Encadeamento Externo

Este repositório contém a implementação e a análise de uma Tabela Hash em **Python**, desenvolvida como resolução do exercício proposto no arquivo Fei - 4° Semestre. O projeto demonstra o funcionamento da função de espalhamento (hash) e o tratamento de colisões utilizando listas encadeadas (encadeamento externo).

## 🧮 1. Cálculos da Função Hash

A função de espalhamento definida é **h(k) = k mod 7**. Abaixo estão os índices calculados para o conjunto de chaves `{190, 322, 172, 89, 13, 4, 769, 61, 15, 76}`:

*   **h(190)** = 190 mod 7 = **1**
*   **h(322)** = 322 mod 7 = **0**
*   **h(172)** = 172 mod 7 = **4**
*   **h(89)** = 89 mod 7 = **5**
*   **h(13)** = 13 mod 7 = **6**
*   **h(4)** = 4 mod 7 = **4**
*   **h(769)** = 769 mod 7 = **6**
*   **h(61)** = 61 mod 7 = **5**
*   **h(15)** = 15 mod 7 = **1**
*   **h(76)** = 76 mod 7 = **6**

## 🗺️ 2. Tabela Hash Resultante

Com os cálculos aplicados e as colisões tratadas inserindo os novos elementos no final da lista encadeada de cada índice, a estrutura final da tabela em memória é a seguinte:

| Índice | Estado da Lista Encadeada (Nós) |
| :---: | :--- |
| **0** | `322 -> NULL` |
| **1** | `190 -> 15 -> NULL` |
| **2** | `NULL` *(Vazio)* |
| **3** | `NULL` *(Vazio)* |
| **4** | `172 -> 4 -> NULL` |
| **5** | `89 -> 61 -> NULL` |
| **6** | `13 -> 769 -> 76 -> NULL` |

## ⚙️ 3. Simulação de Operações

*   **Inserção (Exemplo: Chave 15):** 
    Calcula-se `15 mod 7 = 1`. O sistema acessa o índice `1`. Como o índice já contém a chave `190`, ocorre uma colisão. O algoritmo percorre a lista encadeada até o fim e atualiza o ponteiro do nó `190` para apontar para o novo nó `15`.
*   **Remoção (Exemplo: Chave 172):**
    Calcula-se `172 mod 7 = 4`. O sistema acessa o índice `4`. O primeiro nó verificado já é o `172`. Sendo ele a cabeça da lista, o ponteiro do vetor no índice `4` é atualizado diretamente para o próximo nó (a chave `4`), e a memória do nó `172` é liberada.

## 📊 4. Análise do Fator de Carga

O Fator de Carga ($\alpha$) mede o nível de ocupação e probabilidade de colisões na tabela.
Fórmula: $\alpha = \frac{n}{m}$ (onde *n* = chaves inseridas, *m* = tamanho da tabela).

*   **n** = 10 elementos.
*   **m** = 7 posições.
*   **$\alpha$ = 10 / 7 $\approx$ 1.43**

**Conclusão:** O fator de carga de `1.43` indica que a tabela possui, em média, mais de 1 elemento por posição (sobrecarga). Apesar das colisões frequentes (como visto no índice 6, que possui 3 chaves), o **encadeamento externo** foi eficiente para evitar perda de dados, embora a complexidade de busca comece a se degradar de $O(1)$ para $O(n)$ no comprimento das listas.

---

## 🚀 5. Instruções de Execução

O código foi implementado em **Python** utilizando Orientação a Objetos para recriar as listas encadeadas explicitamente.

1. Clone o repositório em sua máquina.
2. Certifique-se de possuir o Python 3.x instalado.
3. No terminal, navegue até a pasta do projeto e execute:
   ```bash
   python tabela_hash.py