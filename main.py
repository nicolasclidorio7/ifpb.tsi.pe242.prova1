def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

    """
    numero = input("Digite um número: ")
    if numero == numero[::-1]:
        print("True")
    else:
        print("False")
        
    pass


def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    """

    nRomano = input("Digite um número romano: ")
    nRomano = nRomano.upper()
    nArabico = 0

    for i in range(len(nRomano)):
        if nRomano[i] == "I":
            nArabico += 1
        elif nRomano[i] == "V":
            nArabico += 5
            if i > 0 and nRomano[i - 1] == "I":
                nArabico -= 2
        elif nRomano[i] == "X":
            nArabico += 10
            if i > 0 and nRomano[i - 1] == "I":
                nArabico -= 2
        elif nRomano[i] == "L":
            nArabico += 50
            if i > 0 and nRomano[i - 1] == "X":
                nArabico -= 20
        elif nRomano[i] == "C":
            nArabico += 100
            if i > 0 and nRomano[i - 1] == "X":
                nArabico -= 20
        elif nRomano[i] == "D":
            nArabico += 500
            if i > 0 and nRomano[i - 1] == "C":
                nArabico -= 200
        elif nRomano[i] == "M":
            nArabico += 1000
            if i > 0 and nRomano[i - 1] == "C":
                nArabico -= 200
                
    print(nArabico)

    pass


def q3():
    """
    Faça um programa que calcula a quantidade de divisores de um número (incluindo 1 e o próprio número) que são divisíveis por 3.

    """

    numero = int(input("Digite um número"))

    divisores = 0

    for i in range(1,numero + 1):
        if numero % i == 0 and i % 3 == 0:
            divisores += 1 
        if divisores == 0:
            print("o numero não possui divizores multiplos de 3")    
        else:
            print("Quantidade de divisores divididos por 3:")

            pass


def q4():
    """
Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos.

    """
numero1 = int(input(""))
numero2 = int(input(""))

soma = 0

if numero1 < numero2:
    for i in range(numero1, numero2 + 1):
        if i > 0:
            soma += i
        else:
            for i in range(numero2, numero1 + 1):
              if i > 0:    
                  soma += i

        print(soma)
        
        pass

    


