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

  tamanho = 240
  n = 4

  t.up()
  t.down()
  t.pensize(2)

  for i in range(3):
    koch(t, 3, tamanho)
    t.right(120)

  t.hideturtle()
  screen.exitonclick()


