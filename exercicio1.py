#Exercício 1: 
#Crie uma classe base Forma com um método desenhar() que desenha uma forma qualquer utilizando a biblioteca Turte. Em seguida, crie subclasses Círculo e Quadrado que herdam de Forma e sobrescrevem desenhar() para desenhar as formas específicas.

import turtle


class Forma:
    def desenhar(self):
        raise NotImplementedError


class Circulo(Forma):
    def desenhar(self):
        turtle.penup()
        turtle.goto(0, -50)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()


class Quadrado(Forma):
    def desenhar(self):
        turtle.penup()
        turtle.goto(-50, -50)  #
        turtle.pendown()
        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()


def main():
    turtle.speed(1)
    turtle.title("Desenhando Formas")


    circulo = Circulo()
    quadrado = Quadrado()


    circulo.desenhar()
    turtle.clear()
    quadrado.desenhar()

    turtle.done()

import turtle


class Forma:
    def desenhar(self):
        raise NotImplementedError("O método desenhar deve ser sobrescrito.")


class Circulo(Forma):
    def desenhar(self):
        turtle.penup()
        turtle.goto(0, -50)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()


class Quadrado(Forma):
    def desenhar(self):
        turtle.penup()
        turtle.goto(-50, -50)  #
        turtle.pendown()
        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()


def main():
    turtle.speed(1)
    turtle.title("Desenhando Formas")


    circulo = Circulo()
    quadrado = Quadrado()


    circulo.desenhar()
    turtle.clear()
    quadrado.desenhar()

    turtle.done()

if __name__ == "__main__":
    main()
