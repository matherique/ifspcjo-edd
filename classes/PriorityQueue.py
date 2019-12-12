class NewEntry:
    def __init__(self, item, prioridade):
        self.item = item
        self.prioridade = prioridade

    def __str__(self):
        return self.item


class PriorityQueue:
    # Previne a adição dinâmica de atributos
    __slots__ = ['itens', '__tamanho']
    
    # Utiliza uma lista para armazenar os elementos na Fila
    # Cada Fila pode armazenar um determinado número de elementos
    def __init__(self, tamanho):
        self.itenss = []
        self.__tamanho = tamanho
    
    # Retorna o número de elementos da Fila
    def size(self):
        return len(self.itens)
    
    # Verifica se a Fila está vazia
    def is_empty(self):
        return self.itens == []
    
    # Verifica se a Fila está cheia
    def is_full(self):
        return len(self.itens) >= self.__tamanho

    # Insere um item no final da Fila 
    def enqueue(self, item, prioridade):
        # Verifica se a Fila não está cheia 
        if self.is_full() == False:
            # Cria uma nova instância para a classe de armazenamento
            # Armazena essa instância no final da Fila de Prioridades
            entrada = NewEntry(item, prioridade)
            self.itens.append(entrada)
        else:
            print("Fila Cheia!")

    # Remove um item do início da Fila
    def dequeue(self):
        # Verifica se a Fila está vazia 
        if self.is_empty() == True:
            return "Fila vazia!" 
        
        # Encontra o índice do item com maior prioridade
        indice = self.__find_item()
        # remove o item coma maior prioridade
        return self.itens.pop(indice)
    
    # Verifica o elemento no início da Fila
    def peek(self):
        # Verifica se a Fila está vazia
        if self.is_empty() == True:
            return "Fila vazia!"
        
        # Encontra o índice do item com a maior prioridade
        indice = self.__find_item()
        # Retorna o item com a maior prioridade
        return self.itens[indice]

    # Encontra o índice do elemento que possui a maior prioridade
    def __find_item(self):
        # Utiliza a primeira entrada da Fila como sendo o item que possui a maior prioridade para sair
        maior_prioridade = self.itens[0].prioridade
        
        # Índice do primeiro elemento da lista
        indice = 0

        # Percorre todas as entradas da Fila de Prioridade
        for i, entrada in enumerate(self.itens  ):
            # Encontra o índice  do item com a maior prioridade
            if entrada.prioridade < maior_prioridade:
                maior_prioridade = entrada.prioridade
                indice = i

        # Retorna o índice do elemento que possui a maior prioridade
        return indice
