class No:
    def __init__(self, chave):
        self.chave = chave
        self.proximo = None

class TabelaHash:
    def __init__(self, tamanho=7):
        self.tamanho = tamanho
        self.tabela = [None] * self.tamanho
        self.quantidade = 0

    def _hash(self, chave):
        """Função de espalhamento: h(k) = k mod 7"""
        return chave % self.tamanho

    def inserir(self, chave):
        indice = self._hash(chave)
        novo_no = No(chave)
        
        # Encadeamento Externo
        if self.tabela[indice] is None:
            self.tabela[indice] = novo_no
        else:
            atual = self.tabela[indice]
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
            
        self.quantidade += 1

    def remover(self, chave):
        indice = self._hash(chave)
        atual = self.tabela[indice]
        anterior = None
        
        while atual is not None:
            if atual.chave == chave:
                if anterior is not None:
                    anterior.proximo = atual.proximo # Remove do meio/fim
                else:
                    self.tabela[indice] = atual.proximo # Remove do início
                self.quantidade -= 1
                return True
            anterior = atual
            atual = atual.proximo
            
        return False # Chave não encontrada

    def imprimir(self):
        for i in range(self.tamanho):
            print(f"[{i}] -> ", end="")
            atual = self.tabela[i]
            while atual is not None:
                print(f"{atual.chave} -> ", end="")
                atual = atual.proximo
            print("NULL")

# --- TESTE DA IMPLEMENTAÇÃO ---
if __name__ == "__main__":
    chaves = [190, 322, 172, 89, 13, 4, 769, 61, 15, 76]
    hash_table = TabelaHash(7)
    
    print("Inserindo chaves...")
    for chave in chaves:
        hash_table.inserir(chave)
        
    hash_table.imprimir()
    print(f"Fator de carga: {hash_table.quantidade / hash_table.tamanho:.2f}")