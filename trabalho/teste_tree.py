#!/usr/bin/env python3
from tree import Node
from random import randint, seed 

seed(10)

itens = [randint(0, 20) for x in range(10)]
first = itens[0]

n = Node(first)

print(itens)


for i in itens[1:]:
    n.insert(i)

n.debug()

