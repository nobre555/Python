#Ficha de Atividades 2
#Exercicio 1:
nome_do_utilizador=input("Insira o seu nome:")
print("Olá,",nome_do_utilizador)

#Exercicio 2:
float=0,5
String=Diogo
int=3
boolean=True

#Exercicio 3
PI=3,14
numero=6
resultado = PI*numero
print(resultado)

#Exercicio 4 
num1=int(input("Insira um número "))
num2=int(input("Insira outro numero "))

subtracao=num1-num2
soma=num1+num2
multiplicacao= num1*num2
divisao=num1/num2
print(num1,"+" , num2, "=" ,soma)
print(num1,"-" , num2, "=" ,subtracao)
print(num1,"*" , num2, "=" ,multiplicacao)
print(num1,"/" , num2, "=" ,divisao)

#Exercicio5
num=int(input("Insira um número: "))
quadrado=num*num
cubo=quadrado*num
print("Quadrado do número: ",quadrado)
print("Cubo do número: ",cubo)

#Exercicio6
num1=int(input("Insira um número: "))
num2=int(input("Insira outro número: "))
soma=num1+num2
if soma >= 100:
    print("A soma é maior que 100")
else:
    print("A soma não é maior que 100")

#Exercicio7
peso=float(input("Insira o seu peso: "))
altura=float(input("Insira a sua altura: "))
imc=peso/(altura*altura)
print("O seu IMC é de ",imc)

#Exercicio8
ano=int(input("Qual o ano atual? "))
idade=int(input("Qual é a sua idade? "))
ano_de_nascimento=ano-idade
ano_pretendido=ano_de_nascimento+18
print("Fez/Fará 18 anos em ",ano_pretendido)

#Exercicio9
graus=float(input("Insira um valor em graus: "))
Fahrenheit=(graus*9/5)+32
print(graus,"graus equivalem a",Fahrenheit,"Fahrenheit")

#Exercicio10
num=(int(input("Insira um número entre -10 e 10: ")))
while(num<-10 or num>10 ):
    num=(int(input("O número que inseriu não cumpre os requisitos, insira um número entre -10 e 10: ")))
if(num>0):
    print("O número é positivo.")
elif(num==0):
    print("O número é igual a 0")
else:
    print("O número é negativo")

