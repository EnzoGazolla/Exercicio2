#Exercício 2:
#Crie classes Motor, Pneu, Veiculo, onde Veiculo herda tanto de Motor quanto de Pneu. Ambas as classes base (Motor e Pneu) devem ter um método chamado status() que retorna uma string. A classe Veiculo deve também ter um método status() que chama os métodos status() das classes base. Implemente a herança de modo que a classe Veiculo resolva o método status() de maneira correta.


class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def status(self):
        return f"Motor com {self.potencia} CV"

class Pneu:
    def __init__(self, pressao):
        self.pressao = pressao
    
    def status(self):
        return f"Pneus com {self.pressao} libras"

class Veiculo(Motor, Pneu):
    def __init__(self, nome, potencia, pressao):
        Motor.__init__(self, potencia)
        Pneu.__init__(self, pressao)
        self.nome = nome
    
    def status(self):
        status_motor = Motor.status(self)
        status_pneu = Pneu.status(self)
        return f"Status do {self.nome}:\n{status_motor}\n{status_pneu}"

meu_carro = Veiculo("Fusca", 65, 32)
print(meu_carro.status())