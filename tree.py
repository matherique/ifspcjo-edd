#!/usr/bin/env python3 
import turtle 


def tree(t, galho):
  if galho > 5:
    t.forward(galho)
    t.right(20)
    tree(t, galho - 10)
    t.left(40)
    tree(t, galho - 10)
    t.right(20)
    t.backward(galho)
    t.color('brown')

  else:
    t.color('green')


if __name__ == '__main__':
  screen = turtle.Screen()
  t = turtle.Turtle()
  t.shape('turtle')
  t.speed(10)
  t.left(90)
  t.up()
  t.backward(300)
  t.down()
  t.pensize(2)
  t.color('brown')

  tree(t, 100)
  t.color('black')
  screen.exitonclick()
