saida = ""

def adicao(n1, n2):
    return (n1 + n2)

def subracao(n1,  n2):
    return (n1 - n2)

def multiplicacao(n1, n2):
    return (n1 + n2)

def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        print("Não foi possivel realizar a divisão por 0")
        return ("Não há resultados")
    else:
        return (n1 / n2)

def calculadora(n1, n2, operacao):
    if operacao == "+" or operacao == "adicao":
        resultado = adicao(n1, n2)
        return resultado
    elif operacao == "-" or operacao == "subtracao":
        resultado = subracao(n1, n2)
        return resultado
    elif operacao == "*" or operacao == "multiplicacao":
        resultado = multiplicacao(n1, n2)
        return resultado
    elif operacao == "/" or operacao == "divisao":
        resultado = divisao(n1, n2)
        return resultado
    else:
        resultado = "Opção Inválida"
        return resultado

while saida != "n":
    n1 = eval(input("Digite um número: "))
    n2 = eval(input("Digite outro número: "))
    operacao = input("Digite a operação matématica desejada: ").lower()
    resultado = calculadora(n1, n2, operacao)
    print(f"Resultado da operação metemática: {resultado}")
    while True:
        saida = input("Deseja continuar S/N: ").lower().strip()
        if saida == "s":
            break
        elif saida == "n":
            break
        else:
            print("Opção inválida, tente novamente")

print("Encerrando o programa!")