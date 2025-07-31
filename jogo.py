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
     print("É DA PRA BRINCAR UM POUCO")   
     totalTentativas = 9  
elif(nivel == 3):
     print("TEM CORAJEM")
     totalTentarivas = 3