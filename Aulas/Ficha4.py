#Exercicio1
def imprimir_linhas(num):
    contador=1
    while contador<=num:
        print(contador)
        contador=contador+1

#Exercicio2
def desenhar_retangulo(largura,altura):
    print("#" * largura)
    for x in range(altura-2):
        print("#" + " " * (largura-2) + "#")
    print("#" * largura)

#Exercicio3
def desenhar_triangulo(altura):
    contador=1
    for x in range(altura):
        print( "#"*contador)
        contador=contador+1

#Exercicio4
def triangulo_asteriscos(altura):
    contador=1
    for x in range(altura):
        print( "#"*contador)
        contador=contador+1  

#Exercicio5
def contar_palavras():
    frase=input("Insira uma frase. ")
    palavras=frase.split()
    contagem=len(palavras)
    return contagem
        
print(contar_palavras())

#Exercicio6
def calcular(num1,num2,operador):
    if operador == "-":
        return num1-num2
    elif operador == "+":
        return num1+num2
    elif operador == "/":
        return num1/num2
    elif operador=="*":
        return num1*num2

#Exercicio7
def primos(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return false
        else:
            return true

#Exercicio8
def area(largura,comprimento):
    return largura*comprimento

