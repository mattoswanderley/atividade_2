#Matheus Mattos Silva Wanderley/ Matrícula 262032510
import math
#Definindo o input das palavras e estabelecendo os gabaritos. Foi estabelecida uma string por não poder tratar separadamente os caracteres.
#Depois os contadores são estabelecidos (n1 e n2) para contar vogais e consoantes, bem como um terceiro para agregar letras da primeira metade do alfabeto
palavra = input("Digite uma palavra de referência: \n ").lower() #Redução das entradas para padronização
while not palavra.isalpha(): #validação para não inserir dados que não alfabeticos
    print ("Digitação incorreta. Digite uma palavra de 'a' a 'z' ")
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
soma_similaridade = 0.0
for i in range (1,11): #Range estabelecido para pegar 10 palavras, usando 11 para incluir o último termo
#Diferente do input anterior, este fica dentro do laço para pedir uma nova palavra a cada rodada.
    palavra_amostral = input("Digite a palavra amostral: \n").lower()
    while not palavra_amostral.isalpha():
        print ("Digitação incorreta. Digite uma palavra de 'a' a 'z' ")
        palavra_amostral = input("Digite uma palavra amostral: \n ").lower()
    #Contadores zerado, após calibragem no bloco anterior
    nb_vogal = 0 #numeros de vogais do espaço amostral
    nb_consoante = 0 #número de consoantes do espaço amostral
    nb_metade = 0 #intervalo de letras do espaço amostral
    for letra in palavra_amostral:
        if letra in v: 
            nb_vogal += 1
        elif letra in c:
            nb_consoante += 1
        if "a" <= letra <= "m":
            nb_metade += 1
    produto_escalar = (na_vogal*nb_vogal)+(na_consoante*nb_consoante)+(na_metade*nb_metade)
    norma_b = math.sqrt(nb_vogal**2 + nb_consoante**2 + nb_metade**2)
    if norma_a*norma_b > 0:
        similaridade = produto_escalar / (norma_a*norma_b)
    else:
        similaridade = 0.0
    distancia = 1.0-similaridade
    soma_similaridade += similaridade 
    if similaridade >= 0.95:
        classificacao = "Alta similaridade"
    elif 0.80 <= similaridade <= 0.95:
        classificacao = "Média similaridade"
    else:
        classificacao = "Baixa similaridade"
    print(f"Vetor 3D:({nb_vogal}, {nb_consoante}, {nb_metade}) | Similaridade: ({similaridade:.4f} {similaridade*100:.2f}%) | Distancia: {distancia:.4f}")
    print(f"Classificação: {classificacao}\n")
#####FASE 1 CONCLUÍDA#####
###### INÍCIO FASE 2 ########## 
media = soma_similaridade/10
print("="*50)
print(f"""Etapa de vetorização e análise concluída
    O vetor base 3D é {norma_a} e os dados acumulados são: ({na_vogal}) para vogal, ({na_consoante}) para consoante e ({na_metade}) para distribuição alfabética 
    A média das distâncias é {media}""")
print("="*50 + "\n")
#####FASE 2 CONCLUÍDA#####
### INÍCIO DA FASE 3 ###

# A partir daqui a logica de execução segue a dos passos anteriores, com a diferença do laço while.
#Com o laço while True a execução permanece até a saída pelo usuário
while True:
    nova_palavra = input("Digite uma nova palavra: \n").lower()
    if nova_palavra == "parar":
        print("Programa encerrado")
        break
    while not nova_palavra.isalpha():
        print ("Digitação incorreta. Digite uma nova palavra de 'a' a 'z' ")
        nova_palavra = input("Digite uma nova palavra: \n ").lower()
   
    nc_vogal = 0 
    nc_consoante = 0
    nc_metade = 0 
    for letra in nova_palavra:
        if letra in v: 
            nc_vogal += 1
        elif letra in c:
            nc_consoante += 1
        if "a" <= letra <= "m":
            nc_metade += 1
    produto_escalar_c = (na_vogal*nc_vogal)+(na_consoante*nc_consoante)+(na_metade*nc_metade)
    norma_c = math.sqrt(nc_vogal**2 + nc_consoante**2 + nc_metade**2)
    if norma_a*norma_c > 0:
        similaridade_c = produto_escalar_c / (norma_a*norma_c)
    else:
        similaridade_c = 0.0
    distancia_c = 1.0 - similaridade_c
    if similaridade_c >= 0.95:
        classificacao_c = "Alta similaridade"
    elif 0.80 <= similaridade_c <= 0.95:
        classificacao_c = "Média similaridade"
    else:
        classificacao_c = "Baixa similaridade"

    print(f"Vetor 3D: ({nc_vogal}, {nc_consoante}, {nc_metade} | Similaridade): {similaridade_c:.4f} ({similaridade_c*100:.2f}%) | Distância: {distancia_c:.4f}")
    print(f"Classificação: {classificacao_c}\n")