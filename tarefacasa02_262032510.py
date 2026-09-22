#Matheus Mattos Silva Wanderley/ Matrícula 262032510
import math
#Definindo o input das palavras e estabelecendo os gabaritos. Foi estabelecida uma string por não poder tratar separadamente os caracteres.
#Depois os contadores são estabelecidos (n1 e n2) para contar vogais e consoantes, bem como um terceiro para agregar letras da primeira metade do alfabeto
palavra = input("Digite uma palavra de referência: \n ").lower()
v = "aeiou" 
c = "bcdfghjklmnpqrstvwxyz"
n_vogal = 0 #número de vogais
n_consoante = 0 #número de consoantes
metade = 0 #conjunto de letras até a primeira metade
for letra in palavra: #Aqui tem início o primeiro laço para identificar as letras dentro das palavras.
    if letra in v: #Para cada repetição e identificação da letra, o contador aumenta em um número o contador para cada identidade
        n_vogal += 1
    elif letra in c:
        n_consoante += 1
    if "a" <= letra <= "m":
        metade += 1
  
for i in range (1,11):