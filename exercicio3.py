#Exercício 3: 
#Implemente uma classe Ponto com um construtor que aceita coordenadas x e y como atributos. Utilize o objeto ponto como parâmetro para o comando goto() da Turtle. 

import turtle


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def desenhar_circulo(ponto):
    turtle.penup()
    turtle.goto(ponto.x, ponto.y)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()


def main():
    turtle.speed(1)
    turtle.title("Desenhando um Círculo em um Ponto")


    ponto = Ponto(100, 100)


    desenhar_circulo(ponto)

    turtle.done()

if __name__ == "__main__":
    main()