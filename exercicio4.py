
#Exercício 4: 
#Criar um sistema de simulação bancária onde diferentes tipos de contas compartilham algumas operações comuns,mas também têm regras específicas. 
#Defina uma classe abstrata ContaBancaria com métodos abstratos para depositar, sacar e calcular saldo. 
#Crie duas subclasses concretas, ContaCorrente e ContaPoupanca. 
#A ContaCorrente deve permitir um saldo negativo até um certo limite (cheque especial). 
#A ContaPoupanca não deve permitir saldo negativo e deve calcular juros sobre o saldo atual.
#Implementar métodos para exibir informações da conta.
#As contas devem ter atributos como número da conta, titular e saldo.
#A função sacar de ContaPoupanca deve recusar a operação se o saldo ficar negativo.


# Classe base para Conta Bancária
class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        raise NotImplementedError("implementar depositar")

    def sacar(self, valor):
        raise NotImplementedError("implementar sacar")

    def calcular_saldo(self):
        raise NotImplementedError("implementar calcular_saldo")

    def exibir_informacoes(self):
        return f"Conta Número: {self.numero}\nTitular: {self.titular}\nSaldo: R${self.saldo:.2f}"

# Classe para Conta Corrente
class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo=0, limite_cheque_especial=500):
        super().__init__(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f}")
        else:
            print("O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and self.saldo - valor >= -self.limite_cheque_especial:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f}")
        else:
            print("Saldo insuficiente.")

    def calcular_saldo(self):
        return self.saldo

# Classe para Conta Poupança
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular, saldo=0, taxa_juros=0.01):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f}")
        else:
            print("O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f}")
        else:
            print("Saldo insuficiente.")

    def calcular_saldo(self):
        self.saldo += self.saldo * self.taxa_juros
        return self.saldo

# Exemplo de uso
cc = ContaCorrente(numero="12345", titular="Enzo", saldo=100)
cp = ContaPoupanca(numero="67890", titular="Flavio", saldo=100)

# Operações na Conta Corrente
print("\n--- Conta Corrente ---")
print(cc.exibir_informacoes())
cc.depositar(50)
cc.sacar(200)  
print(cc.exibir_informacoes())

# Operações na Conta Poupança
print("\n--- Conta Poupança ---")
print(cp.exibir_informacoes())
cp.depositar(100)
cp.sacar(50)
cp.calcular_saldo() 
print(conta_poupanca.exibir_informacoes())