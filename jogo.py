import random
print("##########################")
print("# jogo de adivinhação    #")
print("#  ianzinho moedas       #")
print("##########################")
print("#      🐝🐻👨🏿‍🏫🐒🇷        #")

numeroSecreto= random.randrange(0,100)
totalTentativas = 0
pontos = 100

print("Qual os níveis de dificuldade? ")
print("(1)- Facil (2)- Médio (3)- Dificil ")

nivel = int(input("Escolha um nível:"))

if(nivel == 1):
     print("KKKKKK MUITO FACIL")
     totalTentativas = 20
elif(nivel == 2):
     print("É, DA PRA BRINCAR UM POUCO")   
     totalTentativas = 9  
elif(nivel == 3):
     print("TEM CORAJEM viu...3")
     totalTentarivas = 3

     for rodada in range (1, totalTentativas +1):
          print("Tentativa {} de {}".format(rodada,totalTentarivas))

          chute_str = input("Digite um número entre 1 e 100: ")
          chute = int(chute_str)

          if(chute < 1 or > 100):
             print("Número invalido")
             continue
 
          acertou = chute == numeroSecreto
          maior = chute > numeroSecreto
          menor = chute < numeroSecreto

          if(acertou)
              print(f"Você acertou e fez {pontos}! ")
              break
          else:
               if(maior):
                    print("Você errou! Seu chute foi maior que o número secreto")
               elif(menor):
                    print("Você errou! Seu chute foi menor que o número secreto")

                    pontosPerdidos = abs(numeroSecreto - chute)
                    pontos = pontos - pontosPerdidos

print("Fim de jogo ! O número era ",numeroSecreto)

