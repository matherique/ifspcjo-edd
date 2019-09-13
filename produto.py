#!/usr/bin/env python3 

x = 5
y = 3

def produto(y, total):
    return total+y

total = 0
for _ in range(x):
    total = produto(y, total)

print(total)
