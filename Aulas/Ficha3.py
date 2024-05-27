#Ficha3
#Exercicio1
idade=int(input("Insira a sua idade: "))
if idade>=18:
    print("Pode Conduzir")
else:
    print("Não pode conduzir")

#Exercicio2
num=int(input("Insira um número"))
if num >0:
    print("O número é positivo")
elif num==0:
    print("O número é zero")
else:
    print("O número é negativo")

#Exercicio3
num=int(input("Insira um número"))
if num%2==0:
    print(num,"é par")
else:
    print(num,"é impar")

#Exercicio4
letra=input("Insira uma letra")
if letra== a or e or i or o or u:
    print("A letra é vogal")
else:
    print("A letra é consoante")

#Exercicio5
idade=int(input("Insira a sua idade: "))
if idade <12:
    print("O bilhete custa 5 euros")
elif idade>=12 and idade <=18:
    print("O bilhete custa 7 euros")
else:
    print("O bilhete custa 10 euros")

#Exercicio6
peso=float(input("Insira o seu peso: "))
altura=float(input("Insira a sua altura: "))
imc=peso/(altura*altura)
if imc < 18.5:
    print("Você está a baixo do peso")
elif imc >=18.5 and imc <=24.9:
    print("Você está no intervalo normal de peso")
elif imc>=25 and imc <=29.9:
    print("Você está com sobrepeso")
elif imc>=30 and imc<=34.9:
    print("Você tem obesidade classe I ")
elif imc>=35 and imc<=39.9:
    print("Você tem obesidade classe II ")
elif imc>=40:
    print("Você tem obesidade classe III ")

#Exercicio7
num1=int(input("Insira um número inteiro: "))
num2=int(input("Insira outro número inteiro: "))
num3=int(input("Insira outro número inteiro: "))

if num1 > num2 and num1>num3:
    print(num1)
elif num2 > num1 and num2>num3:
    print(num2)
elif num3 > num1 and num1>num2:
    print(num3)

#Exercicio8
num1=int(input("Insira um número inteiro: "))
num2=int(input("Insira outro número inteiro: "))

adicao="+"
subtracao="-"

decisao=input("Se quiser adicionar coloque um (+) se quiser subtrair coloque um (-): ")
if decisao== "+":
    print("A soma dos número é",num1+num2) 
elif decisao== "-":
    print("A subtração dos número é",num1-num2)

import random
from random import randrange
#Exercicio9
print("Jogo do Pedra Papel ou Tesoura!!!!!!")
jogada_utilizador=int(input("Para escolher Pedra(1), Papel(2), Tesoura(3): "))
jogadapc = random.randrange(1,3)
pedra=1
papel=2
tesoura=3
if jogadapc==pedra and jogada_utilizador==tesoura:
    print("O computador escolheu Pedra")
    print("Ganhou o computador")
elif jogadapc==pedra and jogada_utilizador==pedra:
    print("O computador escolheu Pedra")
    print("Empate")
elif jogadapc==pedra and jogada_utilizador==papel:
    print("O computador escolheu Pedra")
    print("Você ganhou!!")
elif jogadapc==papel and jogada_utilizador==pedra:
    print("O computador escolheu Papel")
    print("Ganhou o computador")
elif jogadapc==papel and jogada_utilizador==papel:
    print("O computador escolheu Papel")
    print("Empate")
elif jogadapc==papel and jogada_utilizador==tesoura:
    print("O computador escolheu Papel")
    print("Você ganhou!!")
elif jogadapc==tesoura and jogada_utilizador==pedra:
    print("O computador escolheu Tesoura")
    print("Você ganhou!!")
elif jogadapc==tesoura and jogada_utilizador==papel:
    print("O computador escolheu Tesoura")
    print("Ganhou o computador")
elif jogadapc==tesoura and jogada_utilizador==tesoura:
    print("O computador escolheu Tesoura")
    print("Empate")

#Exercicio10