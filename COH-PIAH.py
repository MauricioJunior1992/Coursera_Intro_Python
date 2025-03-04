import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto): #TUDO CERTO

    sentencas = separa_sentencas(texto)

    frases = []
    for frase in sentencas:
        frases += separa_frases(frase)

    palavras = []
    for palavra in frases:
        palavras += separa_palavras(palavra)

    palavrasUnicas = n_palavras_unicas(palavras)

    palavrasDiferentes = n_palavras_diferentes(palavras)

    tamPalavras = 0
    for palavra in palavras:
        tamPalavras += len(palavra)
    tamMedioPalavras = tamPalavras / len(palavras)

    typeToken = palavrasDiferentes / len(palavras)

    hapaxLego = palavrasUnicas / len(palavras) 

    tamSentenca = 0
    for sentenca in sentencas:
        tamSentenca += len(sentenca)
    tamMedioSentenca = tamSentenca / len(sentencas)

    complexSentenca = len(frases) / len(sentencas)

    tamFrases = 0
    for frase in frases:
        tamFrases += len(frase)
    tamMedioFrases = tamFrases / len(frases)

    as_b = [tamMedioPalavras, typeToken, hapaxLego, tamMedioSentenca, complexSentenca, tamMedioFrases]

    return as_b

def compara_assinatura(as_a, as_b): #TUDO CERTO
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    somaDif = 0
    while i < 6:
        somaDif += abs((as_a[i]) - (as_b[i]))
        i += 1
    similaridade = somaDif / 6
    return similaridade

def avalia_textos(textos, as_a):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    aux = 1000
    i = 1
    for texto in textos:
        as_b = calcula_assinatura(texto)
        similaridade = compara_assinatura(as_a, as_b)
        if similaridade < aux:
            textoInfec = i
            aux = similaridade
        i += 1

    return textoInfec


as_a = le_assinatura()
textos = le_textos()
textoInfectado = avalia_textos(textos, as_a)
print("O autor do texto", textoInfectado, "está infectado com COH-PIAH")