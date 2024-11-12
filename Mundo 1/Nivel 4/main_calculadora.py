from Calculadora import Calculadora

calc = Calculadora()

# Entrada de dados pelo usuário
calc.valorA = float(input("Digite o primeiro número: "))
calc.valorB = float(input("Digite o segundo número: "))
calc.operacao = input("Digite a operação (+, -, *, /): ")

# Mostrando o resultado
calc.mostrarResultado()