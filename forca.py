def jogar():
    print ("********************************")
    print ("***Bem vindo ao jogo de Forca***")
    print ("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #enquanto não enforcou e não acertou 
    while(not enforcou and not acertou ):

        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1 

        print(letras_acertadas)
        
    print ("fim de jogo")
    
if(__name__ == "__main__"):
    jogar()