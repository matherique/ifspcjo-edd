#!/usr/bin/env python3
import turtle

count = 0

def quadrado_espiral(tur, tamanho, c=count):
    c += 1
    if tamanho > 0:

        tur.forward(tamanho)
        tur.left(90)

        if c % 4 == 0:
            x, y = tur.position()

            tur.up()
            tur.setpos(x + 10, y + 10)
            tur.down()

            quadrado_espiral(tur, tamanho - 20, c)
        else:
            quadrado_espiral(tur, tamanho, c)

if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.shape('turtle')
    quadrado_espiral(t, 200)
    screen.exitonclick()
