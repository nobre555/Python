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
def contar_palavras(frase):
    for palavras in frase():
        return palavras
contar_palavras("Olá jão tudo bem")