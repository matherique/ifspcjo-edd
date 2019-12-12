class Deck:
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

    # Insere um item no inicio do deque
    def add_front(self, item):
        # Verifica se o Deque não esta cheio
        if self.is_full() == False:
            self.itens.append(item)
        else:
            print("Deque cheio!")

    # Insere um item no final do deque
    def add_back(self, item):
        # Verifica se o deque não esta cheio
        if self.is_full() == False:
            self.itens.insert(0, item)
        else:
            print("Deque cheio!")

    # Remove um item no inicio do deque
    def remove_front(self):
        # Verifica se o deque não esta cheio
        if self.is_empty() == False:
            self.itens.pop()
        else:
            print("Deque fazio!")

    # Remove um item no final do deque
    def remove_back(self):
        # Verifica se o deque não esta cheio
        if self.is_empty() == False:
            self.itens.pop(0)
        else:
            print("Deque fazio!")

    # Verifica um item no inicio do deque
    def peek_front(self):
        # Verifica se o deque não esta cheio
        if self.is_empty() == True:
            return "Deque fazio!"

        return self.itens[-1]

    # Verifica um item no final do deque
    def peek_back(self):
        # Verifica se o deque não esta cheio
        if self.is_empty() == True:
            return "Deque fazio!"

        return self.itens[0]
