class Stack:
    # Previne a adição dinâmica de atributos
    __slots__ = ['itens', 'tamanho']

    # Utiliza uma lista para armazenar os elementos na Pilha
    # Cada Pilha pode armazenar um determinado número de elementos
    def __init__(self, tamanho):
        self.itens = []
        self.__tamanho = 'tamanho'

    # Retorna o número de elementos da Pilha
    def size(self):
        return len(self.itens)

    # Verifica se a Pilha está vazia
    def is_empty(self):
        return self.itens == []

    # Verifica se a Pilha está cheia
    def is_full(self):
        return len(self.itens) >= self.__tamanho

    # Insere um item no topo da Pilha
    def push(self, item):
        # Verifica se a Pilha não está cheia 
        if self.is_full() == False:
            self.itens.append(item) 
        else:
            print("Pilha cheia!")
            
    # Remove um item do topo da Pilha
    def pop(self):
    # Verifica se a Pilha está vazia 
        if self.is_empty() == True:
            return "Pilha vazia!" 

        return self.itens.pop()

    # Verifica o elemento no topo da Pilha 
    def peek(self):
        # Verifica se a Pilha está vazia
        if self.is_empty() == True: 
            return "Pilha vazia!"
        
        return self.itens[-1]
