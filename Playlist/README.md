# Gerenciador de Playlist Dinâmica em Python - Lista Encadeada

Este repositório contém a implementação em **Python** de um sistema de gerenciamento de músicas. A estrutura de dados base do projeto é uma Lista Dinâmica Encadeada, criada do zero a partir de objetos (`class No`, `class Lista`) para estabelecer a referência explícita do encadeamento sem o uso das estruturas de dados prontas do Python (como `list[]`).

## 🛠️ Instruções para Execução

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone o repositório utilizando:
   `git clone <link-do-repositorio>`
3. Navegue até o diretório do projeto:
   `cd <nome-do-diretorio>`
4. Execute o programa via terminal:
   - **No Linux/Mac/Windows:** `python playlist.py` (ou `python3 playlist.py`)

## 🎮 Exemplo de Execução

```text
=== GERENCIADOR DE PLAYLIST ===
1. Exibir playlist
2. Inserir música no INÍCIO
3. Inserir música no FINAL
4. Inserir música em POSIÇÃO ESPECÍFICA
5. Buscar música por ID
6. Buscar músicas por ARTISTA
7. Remover música por ID
8. Informações da playlist (Qtd e Duração)
0. Sair
Escolha uma opção: 3

--- NOVA MÚSICA (FINAL) ---
ID: 101
Título: Starman
Artista: David Bowie
Álbum: Ziggy Stardust
Duração (segundos): 256
Inserida com sucesso!

=== GERENCIADOR DE PLAYLIST ===
[...]
Escolha uma opção: 1

--- PLAYLIST ATUAL ---
[0] ID: 101 | Starman - David Bowie (Álbum: Ziggy Stardust) | 256 seg