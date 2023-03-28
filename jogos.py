import forca
import adivinhacao

print ("********************************")
print ("********Escolha seu jogo********")
print ("********************************")

print ("(1) Forca (2) Adivinhação")

jogo = int (input("Qual jogo?"))
            
if(jogo == 1):
    print("jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando advinhação")
    adivinhacao.jogar()