links = [0, 0, 1, 3, 2, 0, 4, 1, 3, 0] #Estabelecimento das listas a serem percorridas com valores de referência
exclamacoes = [0, 1, 0, 4, 3, 0, 5, 1, 4, 0]
suspeitas = [0, 0, 1, 4, 3, 0, 5, 1, 4, 0]
classes = [
"NORMAL", "NORMAL", "NORMAL", "SPAM", "SPAM",
"NORMAL", "SPAM", "NORMAL", "SPAM", "NORMAL"
]
link_treino = int(input("Quantos links: \n")) #inputs de entrada para iteração posterior
exclamacao_treino = int(input("Quantas exclamações: \n"))
suspeita_treino = int(input("Quantas palavras suspeitas: \n"))
distancias = []
if not (len(links) == len(exclamacoes) == len(suspeitas) == len(classes)): #Aqui optei por colocar validação do tamanho da lista, pois tive uma dúvida na linha do <for> logo abaixo
    print("As listas possuem tamanho diferente")                           #tive dúvidas sobre erros em listas de tamanhos diferentes, apesar de o exercicio já definir as listas paralelas definidas
    for i in range(len(links)): #Havia colocado range (10), mas, por sugestão da IA, o len(link) foi sugerido, o que deu origem à validação anterior                                          
        distancia = abs(link_treino-links[i]) + abs(exclamacao_treino - exclamacoes[i]) + abs(suspeita_treino-suspeitas[i])
        distancias.append(distancia)

