class Pedido:
    def __init__(self, id_pedido, descricao, prioridade):
        self.id = id_pedido
        self.descricao = descricao
        self.prioridade = prioridade

class MaxHeap:
    def __init__(self, capacidade_inicial=10):
        self.inicializar_heap(capacidade_inicial)
        
    def inicializar_heap(self, capacidade):
        self.capacidade = capacidade
        self.tamanho = 0
        self.dados = [None] * self.capacidade

    def _pai(self, i):
        return (i - 1) // 2

    def _esquerdo(self, i):
        return 2 * i + 1

    def _direito(self, i):
        return 2 * i + 2

    def _redimensionar(self):
        # Dobra a capacidade do vetor dinamicamente
        nova_capacidade = self.capacidade * 2
        novos_dados = [None] * nova_capacidade
        for i in range(self.tamanho):
            novos_dados[i] = self.dados[i]
        self.dados = novos_dados
        self.capacidade = nova_capacidade

    def inserir(self, pedido):
        if self.tamanho == self.capacidade:
            self._redimensionar()
            
        # Insere inicialmente no final do vetor
        i = self.tamanho
        self.dados[i] = pedido
        self.tamanho += 1
        
        # Realiza trocas (Bubble Up) para restaurar a propriedade Max-Heap
        while i != 0 and self.dados[self._pai(i)].prioridade < self.dados[i].prioridade:
            pai = self._pai(i)
            self.dados[i], self.dados[pai] = self.dados[pai], self.dados[i]
            i = pai

    def max_heapfy(self, i):
        esquerdo = self._esquerdo(i)
        direito = self._direito(i)
        maior = i

        # Verifica se o filho esquerdo é maior que o nó atual
        if esquerdo < self.tamanho and self.dados[esquerdo].prioridade > self.dados[maior].prioridade:
            maior = esquerdo

        # Verifica se o filho direito é maior que o maior até agora
        if direito < self.tamanho and self.dados[direito].prioridade > self.dados[maior].prioridade:
            maior = direito

        # Se o maior não for o nó atual, troca e continua verificando descendo a árvore
        if maior != i:
            self.dados[i], self.dados[maior] = self.dados[maior], self.dados[i]
            self.max_heapfy(maior)

    def remover(self):
        if self.tamanho == 0:
            return None
        if self.tamanho == 1:
            self.tamanho -= 1
            return self.dados[0]

        # Armazena a raiz (maior prioridade)
        raiz = self.dados[0]
        
        # Substitui a raiz pelo último elemento
        self.dados[0] = self.dados[self.tamanho - 1]
        self.dados[self.tamanho - 1] = None
        self.tamanho -= 1
        
        # Restaura a propriedade do Heap
        self.max_heapfy(0)
        
        return raiz

    def construir(self, vetor_pedidos):
        self.inicializar_heap(max(len(vetor_pedidos) * 2, 10))
        self.tamanho = len(vetor_pedidos)
        
        for i in range(self.tamanho):
            self.dados[i] = vetor_pedidos[i]
            
        # Aplica o max_heapfy de baixo para cima, partindo do último nó com filhos
        for i in range((self.tamanho // 2) - 1, -1, -1):
            self.max_heapfy(i)

    def print_heap(self):
        if self.tamanho == 0:
            print("Nenhum pedido aguardando atendimento.")
            return
            
        for i in range(self.tamanho):
            p = self.dados[i]
            print(f"ID: {p.id} | Prioridade: {p.prioridade} | Descrição: {p.descricao}")


# --- INTERFACE E MENU ---

def exibir_menu():
    print("\n===== SISTEMA DE PEDIDOS =====")
    print("1 - Cadastrar pedido")
    print("2 - Atender pedido (Remover e Atender)")
    print("3 - Exibir pedidos (Estado do Heap)")
    print("4 - Exibir quantidade de pedidos aguardando")
    print("5 - Construir Heap a partir de um lote inicial")
    print("0 - Sair")

def capturar_dados_pedido():
    try:
        id_pedido = int(input("ID: "))
        descricao = input("Descrição: ")
        prioridade = int(input("Prioridade: "))
        return Pedido(id_pedido, descricao, prioridade)
    except ValueError:
        print("\n[!] Erro: ID e Prioridade devem ser números inteiros.")
        return None

def main():
    heap = MaxHeap(capacidade_inicial=5)
    
    while True:
        exibir_menu()
        try:
            escolha = int(input("\nEscolha: "))
        except ValueError:
            print("Opção inválida.")
            continue

        if escolha == 1:
            print("\n--- NOVO PEDIDO ---")
            p = capturar_dados_pedido()
            if p:
                heap.inserir(p)
                print("Pedido cadastrado com sucesso e reposicionado no Max-Heap!")
                
        elif escolha == 2:
            print("\n--- ATENDIMENTO ---")
            p_atendido = heap.remover()
            if p_atendido:
                print("Pedido atendido:")
                print(f"ID: {p_atendido.id}")
                print(f"Descrição: {p_atendido.descricao}")
                print(f"Prioridade: {p_atendido.prioridade}")
                
                print("\nPedidos restantes no Heap:")
                heap.print_heap()
            else:
                print("Nenhum pedido para atender. A fila está vazia.")
                
        elif escolha == 3:
            print("\n--- ESTADO ATUAL DO HEAP ---")
            heap.print_heap()
            
        elif escolha == 4:
            print(f"\nQuantidade de pedidos aguardando atendimento: {heap.tamanho}")
            
        elif escolha == 5:
            print("\n--- CONSTRUIR HEAP (LOTE INICIAL) ---")
            lote = [
                Pedido(1, "Pedido A", 2),
                Pedido(2, "Pedido B", 5),
                Pedido(3, "Pedido C", 3),
                Pedido(4, "Pedido D", 8),
                Pedido(5, "Pedido E", 1)
            ]
            heap.construir(lote)
            print("Heap construído com sucesso a partir do lote de 5 pedidos!")
            heap.print_heap()
            
        elif escolha == 0:
            print("Encerrando o sistema...")
            break
            
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()