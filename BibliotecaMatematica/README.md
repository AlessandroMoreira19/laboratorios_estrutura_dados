# Análise de Dados com Arrays e Vetores em C

Este repositório contém a implementação em **C** de uma aplicação capaz de armazenar e manipular vetores de números reais utilizando Arrays como estrutura de dados. A aplicação foi desenvolvida do zero, sem o uso de bibliotecas numéricas externas para a estrutura, e implementa cálculos algébricos avançados conforme as orientações do exercício "Fei - 4° Semestre".

## 🛠️ Instruções para Compilação e Execução

Como o código faz uso da biblioteca matemática padrão do C (`math.h`) para calcular a raiz quadrada na função `norma()`, é necessário vinculá-la durante a compilação.

1. Certifique-se de ter um compilador C instalado (como `gcc` no Linux/Mac ou `MinGW` no Windows).
2. Clone o repositório utilizando:
   `git clone <link-do-repositorio>`
3. Navegue até o diretório do projeto:
   `cd <nome-do-diretorio>`
4. Compile o código executando no terminal:
   `gcc vetores_app.c -o vetores_app -lm`
   *(A flag `-lm` é obrigatória em sistemas baseados em Unix, como Linux e macOS, para compilar a biblioteca `math.h`)*.
5. Execute o programa:
   - **No Linux/Mac:** `./vetores_app`
   - **No Windows:** `vetores_app.exe`

## 🎮 Exemplos de Execução

Abaixo, um exemplo de fluxo de execução pelo menu interativo da aplicação, demonstrando a criação de vetores e o cálculo da similaridade de cosseno com os valores solicitados no enunciado:

```text
=== ANALISE DE DADOS COM VETORES ===
1. Criar novo vetor
2. Exibir vetores armazenados
3. Multiplicar vetor por escalar
4. Somar dois vetores
5. Calcular produto escalar
6. Calcular norma de um vetor
7. Calcular similaridade de cosseno
8. Encontrar vetor mais similar a uma consulta
9. Buscar elemento em um vetor (Estrutura Array)
10. Remover elemento de um vetor (Estrutura Array)
0. Sair
Escolha uma opcao: 1

Informe o tamanho (dimensao) do vetor: 4
Informe o valor da posicao 0: 0.8
Informe o valor da posicao 1: 0.2
Informe o valor da posicao 2: 0.5
Informe o valor da posicao 3: 0.9
Vetor 0 criado com sucesso!

=== ANALISE DE DADOS COM VETORES ===
[...]
Escolha uma opcao: 1

Informe o tamanho (dimensao) do vetor: 4
Informe o valor da posicao 0: 0.7
Informe o valor da posicao 1: 0.1
Informe o valor da posicao 2: 0.6
Informe o valor da posicao 3: 0.8
Vetor 1 criado com sucesso!

=== ANALISE DE DADOS COM VETORES ===
[...]
Escolha uma opcao: 7

ID do vetor A: 0
ID do vetor B: 1
Similaridade de Cosseno: 0.9876