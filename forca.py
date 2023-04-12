import random


def jogar():
   
    imprime_mesagem_abertudo()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto não enforcou e não acertou 
    while(not enforcou and not acertou ):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1 
        else:
            erros += 1
            print("Você errou {} de {} ".format(erros,6))

        enforcou = erros == 6
        #enquanto _ não tiver em letras acertadas a condição de acertou continua false
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)\

    if (acertou):
        print("Você ganhou!") 
    else:
        print("Você perdeu!")
    print ("fim de jogo")
    
def imprime_mesagem_abertudo():
    print ("********************************")
    print ("***Bem vindo ao jogo de Forca***")
    print ("********************************")

def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    #para cada linha dentro do arquivo
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
                            #len devolve o tamanho da lista (palavras)
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    #vai ler e retornar a palavra secreta
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    #usa _ para cada letra na palavra secreta (list comprehensions)
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()