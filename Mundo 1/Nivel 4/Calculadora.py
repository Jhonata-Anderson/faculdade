class Calculadora:
    def __init__(self):
        self.__valorA = 0
        self.__valorB = 0
        self.__operacao = ''

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self):
        if self.operacao in ['+', '-', '*', '/']:
            return True
        else:
            return False

    def calcular(self):
        if not self.validarOperacao():
            print("Operação inválida.")
            return None

        if self.operacao == '+':
            return self.valorA + self.valorB
        elif self.operacao == '-':
            return self.valorA - self.valorB
        elif self.operacao == '*':
            return self.valorA * self.valorB
        elif self.operacao == '/':
            if self.valorB == 0:
                print("Não é possível dividir por zero.")
                return None
            else:
                return self.valorA / self.valorB

    def mostrarResultado(self):
        resultado = self.calcular()
        if resultado is not None:
            print(f"{self.valorA} {self.operacao} {self.valorB} = {resultado}")
