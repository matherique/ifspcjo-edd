#!/usr/bin/env python3
n_pecas = 3
QTD = n_pecas * 2 + 1

t1 = [i for i in range(1, QTD)][::2][::-1]
t2, t3 = [], []

def movimento(n, t1, t3, t2):
  if n > 0:
    movimento(n - 1, t1, t2, t3)
    
    t3.append(t1.pop())
    exibir()

    movimento(n - 1, t2, t3, t1)


def exibir():
  pipe = "|"
  print(f"{pipe:^10}  {pipe:^10}  {pipe:^10}")
  
  for i in reversed(range(QTD//2)):
    d1 = "*" * t1[i] if i <= len(t1) - 1 else "|"
    d2 = "*" * t2[i] if i <= len(t2) - 1 else "|"
    d3 = "*" * t3[i] if i <= len(t3) - 1 else "|"
    
    print(f"{d1:^10}  {d2:^10}  {d3:^10}")

  print("=" * 34)
  print()

exibir()
movimento(len(t1), t1, t3, t2)
