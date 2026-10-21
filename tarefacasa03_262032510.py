links = [0, 0, 1, 3, 2, 0, 4, 1, 3, 0]
exclamacoes = [0, 1, 0, 4, 3, 0, 5, 1, 4, 0]
suspeitas = [0, 0, 1, 4, 3, 0, 5, 1, 4, 0]
classes = [
"NORMAL", "NORMAL", "NORMAL", "SPAM", "SPAM",
"NORMAL", "SPAM", "NORMAL", "SPAM", "NORMAL"
]
link_teste: []
exclamacao_teste: []
suspeita_teste: []
for i in range (3):
    link1 = int(input("Digite a quantidade de links: \n "))
    link_teste.append(link1)
    
    exclamacao1 = int(input("Digite a quantidade de exclamações:\n "))
    exclamacao_teste.append(exclamacao1)

    suspeita1 = int(input("Digite a quantidade de palabras suspeitas: \n"))
    suspeita_teste.append(suspeita1)

