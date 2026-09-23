#Matheus Mattos Silva Wanderley/ Matrícula 262032510
import math
#Definindo o input das palavras e estabelecendo os gabaritos. Foi estabelecida uma string por não poder tratar separadamente os caracteres.
#Depois os contadores são estabelecidos (n1 e n2) para contar vogais e consoantes, bem como um terceiro para agregar letras da primeira metade do alfabeto
palavra = input("Digite uma palavra de referência: \n ").lower()
v = "aeiou" 
c = "bcdfghjklmnpqrstvwxyz"
na_vogal = 0 #número de vogais
na_consoante = 0 #número de consoantes
na_metade = 0 #conjunto de letras até a primeira metade
for letra in palavra: #Aqui tem início o primeiro laço para identificar as letras dentro das palavras.
    if letra in v: #Para cada repetição e identificação da letra, o contador aumenta em um número o contador para cada identidade
        na_vogal += 1
    elif letra in c:
        na_consoante += 1
    if "a" <= letra <= "m":
        na_metade += 1
norma_a = math.sqrt(na_vogal**2 + na_consoante**2 + na_metade**2)
similaridade = 0.0
for i in range (1,11): #Range estabelecido para pegar 10 palavras, usando 11 para incluir o último termo
nb_vogal = 0 #numeros de vogais do espaço amostral
nb_consoante = 0 #número de consoantes do espaço amostral
nb_metade = 0 #intervalo de letras do espaço amostral
    for letra in palavra_amostral:
        palavra_amostral = input("Digite a palavra amostral: \n").lower() #Diferente do input anterior, este fica dentro do laço para pedir uma nova palavra a cada rodada.
        if letra in v: 
            nb_vogal += 1
        elif letra in c:
            nb_consoante += 1
        if "a" <= letra <= "m":
            nb_metade += 1
        produto_escalar = (na_vogal*nb_vogal)+(na_consoante*nb_consoante)+(na_metade*nb_metade)
        norma_b = math.sqrt(nb_vogal**2 + nb_consoante**2 + nb_metade**2)
        similaridade = produto_escalar/(norma_a*norma_b)
        distancia = 1.0-similaridade