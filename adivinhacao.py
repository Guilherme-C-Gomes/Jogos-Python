print ("********************************")
print ("Bem vindo ao jogo de adivinhação")
print ("********************************")

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1) :
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str= input("Digite o seu numero: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto 
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")  
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o numero secreto")  
        elif (menor):
            print("Você errou! O seu chute foi menor que o numero secreto")

print ("fim de jogo")