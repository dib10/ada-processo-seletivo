def solution(postagens):
    contagem_hashtags = {}
    for postagem in postagens:
        palavras = postagem.split() # separa a postagem em palavras c split
        for palavra in palavras:
            if palavra.startswith('#'): #startswith verifica se a palavra começa com #
                hashtag = palavra.lower()
                if hashtag in contagem_hashtags:
                    contagem_hashtags[hashtag] += 1
                else:
                    contagem_hashtags[hashtag] = 1
    classificacao = [[hashtag, contagem] for hashtag, contagem in contagem_hashtags.items()]
    classificacao.sort(key=lambda x: (-x[1], x[0])) #key lambda ordena a lista pelo segundo elemento de forma decrescente e pelo primeiro elemento de forma crescente
    return classificacao

postagens = [
    "Nesta semana eu tive o privilégio de ministrar uma palestra sobre Web Scraping com Python. Foi irado! #python #education #technology #programming",
    "#Python é muito bom #adoro #programming"
]

print(solution(postagens))