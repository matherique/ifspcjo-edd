#!/usr/bin/env python3 
import turtle

def koch(tartaruga, n, tamanho):
  if n == 0:
    tartaruga.forward(tamanho)
  else:
    koch(tartaruga, n - 1, tamanho/3)
    tartaruga.left(60)
    koch(tartaruga, n - 1, tamanho/3)
    tartaruga.right(120)
    koch(tartaruga, n - 1, tamanho/3)
    tartaruga.left(60)
    koch(tartaruga, n - 1, tamanho/3)



if __name__ == "__main__":

  screen = turtle.Screen()
  t = turtle.Turtle()
  t.shape("turtle")
  t.speed(0)

  tamanho = 140
  n = 4

  t.up()
  t.back(tamanho * 2.25)
  t.down()
  t.pensize(2)

  for i in range(n):
    koch(t, i, tamanho)
    t.up()
    t.forward(20)
    t.down()


  t.hideturtle()

  screen.exitonclick()


