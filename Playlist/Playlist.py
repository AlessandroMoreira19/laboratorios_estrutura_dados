class Musica:
    def __init__(self, id_musica, titulo, artista, album, duracao):
        self.id = id_musica
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

class No:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicializar_lista()
        
    def inicializar_lista(self):
        self.primeiro = None
        self.quantidade = 0

    def inserir(self, musica, posicao):
        if posicao < 0 or posicao > self.quantidade:
            return False
            
        novo_no = No(musica)
        
        if posicao == 0:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            for _ in range(posicao - 1):
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
            
        self.quantidade += 1
        return True

    def imprimir(self):
        atual = self.primeiro
        if atual is None:
            print("A playlist está vazia.")
            return
            
        pos = 0
        while atual is not None:
            m = atual.musica
            print(f"[{pos}] ID: {m.id} | {m.titulo} - {m.artista} (Álbum: {m.album}) | {m.duracao} seg")
            atual = atual.proximo
            pos += 1

    def buscar(self, id_musica):
        atual = self.primeiro
        while atual is not None:
            if atual.musica.id == id_musica:
                return atual
            atual = atual.proximo
        return None

    def remover(self, id_musica):
        atual = self.primeiro
        anterior = None
        
        while atual is not None and atual.musica.id != id_musica:
            anterior = atual
            atual = atual.proximo
            
        if atual is None:
            return False
            
        if anterior is None:
            self.primeiro = atual.proximo
        else:
            anterior.proximo = atual.proximo
            
        self.quantidade -= 1
        return True


# --- FUNCIONALIDADES COMPLEMENTARES DO SISTEMA ---

def buscar_por_artista(playlist, artista_busca):
    atual = playlist.primeiro
    encontrados = 0
    
    print(f"\nResultados para o artista '{artista_busca}':")
    while atual is not None:
        if atual.musica.artista.lower() == artista_busca.lower():
            m = atual.musica
            print(f"ID: {m.id} | {m.titulo} (Álbum: {m.album}) | {m.duracao} seg")
            encontrados += 1
        atual = atual.proximo
        
    if encontrados == 0:
        print("Nenhuma música encontrada.")

def calcular_duracao_total(playlist):
    atual = playlist.primeiro
    total_segundos = 0
    while atual is not None:
        total_segundos += atual.musica.duracao
        atual = atual.proximo
    return total_segundos

def capturar_dados_musica():
    try:
        id_musica = int(input("ID: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        duracao = int(input("Duração (segundos): "))
        return Musica(id_musica, titulo, artista, album, duracao)
    except ValueError:
        print("Erro: ID e Duração devem ser números inteiros.")
        return None


# --- INTERFACE E MENU ---

def main():
    playlist = Lista()
    opcao = -1

    while opcao != 0:
        print("\n=== GERENCIADOR DE PLAYLIST ===")
        print("1. Exibir playlist")
        print("2. Inserir música no INÍCIO")
        print("3. Inserir música no FINAL")
        print("4. Inserir música em POSIÇÃO ESPECÍFICA")
        print("5. Buscar música por ID")
        print("6. Buscar músicas por ARTISTA")
        print("7. Remover música por ID")
        print("8. Informações da playlist (Qtd e Duração)")
        print("0. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue

        if opcao == 1:
            print("\n--- PLAYLIST ATUAL ---")
            playlist.imprimir()
            
        elif opcao == 2:
            print("\n--- NOVA MÚSICA (INÍCIO) ---")
            m = capturar_dados_musica()
            if m and playlist.inserir(m, 0):
                print("Inserida com sucesso!")
                
        elif opcao == 3:
            print("\n--- NOVA MÚSICA (FINAL) ---")
            m = capturar_dados_musica()
            if m and playlist.inserir(m, playlist.quantidade):
                print("Inserida com sucesso!")
                
        elif opcao == 4:
            print("\n--- NOVA MÚSICA (POSIÇÃO) ---")
            try:
                pos = int(input(f"Posição desejada (0 a {playlist.quantidade}): "))
                if 0 <= pos <= playlist.quantidade:
                    m = capturar_dados_musica()
                    if m and playlist.inserir(m, pos):
                        print(f"Inserida na posição {pos} com sucesso!")
                else:
                    print("Posição inválida.")
            except ValueError:
                print("Posição inválida.")
                
        elif opcao == 5:
            try:
                id_busca = int(input("\nID da música: "))
                res = playlist.buscar(id_busca)
                if res is not None:
                    print(f"\nMúsica encontrada: {res.musica.titulo} - {res.musica.artista}")
                else:
                    print("\nMúsica não encontrada (Inexistente).")
            except ValueError:
                print("ID inválido.")
                
        elif opcao == 6:
            artista_busca = input("\nNome do artista: ")
            buscar_por_artista(playlist, artista_busca)
            
        elif opcao == 7:
            try:
                id_rem = int(input("\nID da música para remover: "))
                if playlist.remover(id_rem):
                    print("Música removida com sucesso!")
                else:
                    print("Erro: Música inexistente ou playlist vazia.")
            except ValueError:
                print("ID inválido.")
                
        elif opcao == 8:
            print("\n--- ESTATÍSTICAS ---")
            print(f"Quantidade de músicas: {playlist.quantidade}")
            total_seg = calcular_duracao_total(playlist)
            print(f"Duração total: {total_seg} segundos ({total_seg // 60} min e {total_seg % 60} seg)")
            
        elif opcao != 0:
            print("Opção inválida.")

    print("Programa encerrado.")

if __name__ == "__main__":
    main()