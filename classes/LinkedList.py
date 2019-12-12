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

        # Faz com que o INICIO aponte para o novo Nó, transformando 
        # ele no novo primeiro elemento da lista
        self.inicio = novo_node
       
    # Insere um nó, apos um nó ja existente dentro da lista
    def insert_after(self, node_anterior, item):
        if node_anterior is None:
            print("Erro: o Nó anterior não está armazenado dentro da lista!")
            return 
        
        # Cria o novo nó e insere o item dentro dele
        novo_node = Node(item)
        
        # Atualiza o ponteiro de novo nó, fazendo ele aponta para onde o nó 
        # anteior aponta
        novo_node.proximo = node_anterior.proximo

        # Atualiza o ponteiro do nó anterior, faezndo ele apontar 
        # para o novo nó que foi inserido
        node_anterior.proximo = novo_node

    # Insere um novo nó, no final da lista
    def append(self, item):
        # Cria o novo nó e insere o item dentro dele
        # Faz ele apontar para um valor nulo
        novo_node = Node(item)

        # Se a lista está vazia, faz com que o INICIO
        # aponta para o novo nó, transformanddo ele no 
        # primeiro elemento da lista
        
        if self.inicio is None:
            self.inicio = novo_node
            return

        # Caso contrario, caminhe até o ultimo nó armazenado na lista
        ultimo_node = self.inicio
        while (ultimo_node.proximo):
            ultimo_node = ultimo_node.proximo
        
        # Faz com que o ultimo nó armazenado na lista aponte para o novo 
        # nó que foi inserido
        ultimo_node.proximo = novo_node

    # Retorna o numero de nos existente na lista
    def size(self):
        # Aponta o ponteiro auxiliar para o inicio da lista
        temp = self.inicio
        # Contador para o total de nós
        total = 0
        # Loop para percorrer os nós da lista
        while (temp):
            total += 1
            temp = temp.proximo
        # Retorna o numero de nos
        return total

    # Verifica se um item esta armazenado na lista
    def search(self, item):
       # Aponta o pointeiro auxiliar para o inicio da listaa
       temp = self.inicio

       # Loop para percorrer os nós da lista
       while temp != None:
           # Encontrou o item
           if temp.item == item:
               return True

           # Avança para o proximo nó
           temp = temp.proximo

        # Não encontrou o item
        return False
    # Retorna a posição de um item armazenado dentro da lista
    def index(self, item):
        # Aponta o ponteiro auxiliar para o inicio da lista
        temp = self.inicio
        
        # Contador da posição do item
        posicao = 1

        # Loop para percorrer o nós da lista
        while temp != None:
            # Encontrou o item
            if temp.item == item:
                return posicao
            
            # Avança para o proximo nó
            temp = temp.proximo

            # Contador da posicao do item
            posicao += 1

        # Não encontrou o item
        return -1
    
    # Verifica se uma lista esta vazia
    def is_empty(self, item):
        # Verifica para onde o inicio da lista aponta
        return self.inicio is None:
    
    # Remove o nó armazenado na primeira posicao da lista
    def remove_first(self):
        # Verifica se a lista esta vazia
        if self.inicio == None:
            return False

        # Aponta o ponteiro auxiliar para o inicio da lista
        temp = self.inicio
        
        # Atualiza os ponteiros
        self.inicio = temp.proximo

        # Remove o ponteiro auxiliar
        temp = None
        
        # Retrna, informando que o nó foi removido
        return True

    # remove o nó armazenado na ultima posicao da lista
    def remove_last(self):
        # Verifica se a lista esta vazia 
        if self.inicio == None:
            return False

        # Aponta o ponteiro auxiliar para o inicio da lista
        temp = self.inicio

        # Verifica se a lista só possui um nó
        if temp.proximo == None:
            self.inicio = None
            return True
            
        # Loop para percorrer os nós da lista 
        while (temp.proximo is not None):
            anterior = temp
            temp = temp.proximo
    
            # Atualiza o ponteiro do penultimo nó, removendo 
            # o ultimo nó da lista
            anterior.proximo = None
            
            # Removendo o ponteiro auxiliar
            temp = None
            
            # Retorna, informando que o no foi removido 
            return True

    # Remove um nó contendo um determinado item
    def remove_node(self):
        pass

    # Remove um Nó armazenado em determinada
    # posição da lista
    def remove_position(self, position):
        # Verifica se a lista está vazia
        if self.inicio == None:
            return False
        # Aponta o ponteiro auxiliar para o início da lista
        temp = self.inicio

        # Verifica se o primeiro Nó é quem deve ser removido
        if (position-1) == 0:
            # Atualiza os ponteiros
            self.inicio = temp.proximo
            # Remove o ponteiro auxiliar
            temp = None
            # Retorna, infaormando que o Nó foi removido
            return True

        # Procura pelo Nó a ser removido, mantendo um registro do Nó
        # anterior, para poder realizar a alteração dos ponteiros
        for i in range(position-1):
            # Atualiza os ponteiros
            anterior = temp
            temp = temp.proximo

            # Verifica se chegou no final da lista
            if temp is None:
                break
        # Se o item não foi encontrado, retorna Falso
        if(temp == None):
            return False

        # Caso contrário, atualiza os ponteiros, o que irá remover o Nó
        # armazenado na lista
        anterior.proximo = temp.proximo
        # Remove o ponteiro auxiliar
        temp = None
        # Retorna, informando que o Nó foi removido
        return True
