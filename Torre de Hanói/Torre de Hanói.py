class No:
    def __init__(self, disco):
        self.disco = disco
        self.proximo = None

class Pilha:
    def __init__(self):
        self.inicializar_pilha()

    def inicializar_pilha(self):
        self._topo = None
        self.quantidade = 0

    def empilhar(self, disco):
        novo_no = No(disco)
        novo_no.proximo = self._topo
        self._topo = novo_no
        self.quantidade += 1

    def desempilhar(self):
        if self._topo is None:
            return None
        removido = self._topo
        self._topo = self._topo.proximo
        self.quantidade -= 1
        return removido.disco

    def topo(self):
        if self._topo is None:
            return None
        return self._topo.disco

    def imprimir(self):
        """
        Retorna uma representação visual da pilha.
        Como é uma pilha, a iteração vai do topo para a base.
        """
        if self._topo is None:
            return "[ Vazia ]"
        
        elementos = []
        atual = self._topo
        while atual is not None:
            elementos.append(str(atual.disco))
            atual = atual.proximo
            
        # Retorna do topo (esquerda) para a base (direita)
        return "Topo -> " + " | ".join(elementos) + " <- Base"

def exibir_estado(torres):
    print("\n" + "="*30)
    print("ESTADO DAS TORRES:")
    for i in range(3):
        print(f"Torre {i + 1}: {torres[i].imprimir()}")
    print("="*30 + "\n")

def jogar():
    while True:
        # Inicializa o jogo com 3 pilhas
        torres = [Pilha(), Pilha(), Pilha()]
        movimentos = 0
        total_discos = 4

        # Empilha os discos na Torre 1 (do maior para o menor)
        # Ordem de inserção: 4, 3, 2, 1 (1 fica no topo)
        for disco in range(total_discos, 0, -1):
            torres[0].empilhar(disco)

        print("\n*** BEM-VINDO À TORRE DE HANÓI ***")
        print("Mova todos os discos para a Torre 3.")
        print("Regras: Mova 1 disco por vez. Discos maiores não podem ficar sobre menores.")

        jogando = True
        while jogando:
            exibir_estado(torres)
            print(f"Movimentos realizados: {movimentos}")
            print("\nOpções: [1-3] Selecionar Torre | [0] Reiniciar Jogo | [9] Sair")
            
            try:
                origem_input = int(input("Torre de ORIGEM (1, 2 ou 3): "))
                if origem_input == 9:
                    print("Encerrando o jogo...")
                    return
                if origem_input == 0:
                    print("Reiniciando a partida...")
                    break # Quebra o loop atual para iniciar um novo jogo
                
                if origem_input not in [1, 2, 3]:
                    print("[!] Torre de origem inválida.")
                    continue

                destino_input = int(input("Torre de DESTINO (1, 2 ou 3): "))
                if destino_input not in [1, 2, 3]:
                    print("[!] Torre de destino inválida.")
                    continue

                origem_idx = origem_input - 1
                destino_idx = destino_input - 1

                # Validações de movimento
                if torres[origem_idx].quantidade == 0:
                    print("\n[!] MOVIMENTO INVÁLIDO: A torre de origem está vazia!")
                    continue

                disco_movido = torres[origem_idx].topo()
                disco_destino = torres[destino_idx].topo()

                if disco_destino is not None and disco_movido > disco_destino:
                    print("\n[!] MOVIMENTO INVÁLIDO: Um disco maior não pode ser colocado sobre um menor!")
                    continue

                # Movimento válido: Desempilha da origem e empilha no destino
                disco = torres[origem_idx].desempilhar()
                torres[destino_idx].empilhar(disco)
                movimentos += 1
                print(f"\n[V] Sucesso: Disco {disco} movido da Torre {origem_input} para a Torre {destino_input}.")

                # Verifica condição de vitória (Torre 3 tem todos os discos)
                if torres[2].quantidade == total_discos:
                    exibir_estado(torres)
                    print(f"\n🏆 PARABÉNS! Você venceu o jogo em {movimentos} movimentos! 🏆")
                    
                    resp = input("Deseja jogar novamente? (S/N): ").upper()
                    if resp == 'S':
                        break # Reinicia
                    else:
                        print("Obrigado por jogar!")
                        return

            except ValueError:
                print("\n[!] Entrada inválida. Por favor, digite apenas números.")

if __name__ == "__main__":
    jogar()