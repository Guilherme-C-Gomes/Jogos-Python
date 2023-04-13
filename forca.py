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

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
            
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        #enquanto _ não tiver em letras acertadas a condição de acertou continua false
        acertou = "_" not in letras_acertadas or palavra_secreta == chute

        print(letras_acertadas)\

    if (acertou):
        imprime_mensagem_vencedor ()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

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

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1 

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    jogar()
