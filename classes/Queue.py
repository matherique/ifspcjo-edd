class Queue:
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
    def enqueue(self, item):
        # Verifica se a Fila não está cheia 
        if self.is_full() == False:
            self.itens.insert(0, item) 
        else:
            print("Fila cheia!")

    # Remove um item do início da Fila
    def dequeue(self):
        # Verifica se a Fila está vazia 
        if self.is_empty() == True:
            return "Fila vazia!" 

        return self.itens.pop()
    
    # Verifica o elemento no início da Fila
    def peek(self):
        # Verifica se a Fila está vazia
        if self.is_empty() == True:
            return "Fila vazia!"

        return self.itens[-1]
