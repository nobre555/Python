opcoes=["pedra","papel","tesoura"]
escolha_computador= random.choice(opcoes)
escolha_usuario=input("Escolha pedra,papel,tesoura: ").lower()
print("O computador escolheu: {escolha_computador}")
if(escolha_usuario==escolha_computador):
    print("Empate")
elif (escolha_usuario== "pedra" and escolha_computador=="tesoura") or (escolha_usuario=="papel" and escolha_computador=="pedra") or (escolha_usuario=="tesoura" and escolha_computador=="papel"):
    print("Voce venceu")
elif escolha_usuario in opcoes:
    print("Perdeu")
else:
    print("Escolha inválida. Por favor, escolha entre pedra,papel ou tesoura")
    