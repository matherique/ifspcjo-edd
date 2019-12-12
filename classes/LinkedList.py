class Node:
    # Previne a adição dinamica de atributos
    __slots__ = ['item', 'proximo']

    # Função para inicializar o objeto Node
    def __init__(self, item):
        self.item = item
        self.proximo = None


class LinkedList:
    # Previne a adição dinamica de atributos
    __slots__ = ['inicio']

    # Função para inicializar o objeto LinkedList
    def __init__(self):
        self.inicio = None
    
    # Exibe todos os itens armazenados na lista
    def display(self):
        
        # Posiciona-se no primeiro nó da lista
        temp = self.inicio

        # Enquanto houver elementos dentro da lista
        while (temp):
            print(temp.item, end=" ")

            # Avança para o proximo elemento
            temp = temp.proximo


    def push(self, item):
        # Aloca espaço para o Nó dentro da lista 
        # Insere o item dentro do Nó
        novo_node = Node(item)

        # Atualiza o ponteiro do novo Nó, fazendo ele apontar 
        # para o primeiro elemento já existente dentro da lista
        novo_node.proximo = self.inicio

        # Faz com que o INICIO aponte para o novo Nó, transformando ele no novo primeiro elemento da lista
        self.inicio = novo_node
       
    def insert_after(self, node_anterior, item):
        pass
    
    def append(self, item):
        pass
    
    def size(self):
        pass
    
    def search(self, item):
        pass
    
    def index(self, item):
        pass

    def is_empty(self, item):
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove_node(self):
        pass

    def remove_position(self):
        pass
