from pymarc import MARCReader

# Retornar a localização Arco de um livro com o nome do autor e do livro #
def localizacao_arco_nome(sobrenome, livro):

	sobrenome_split = sobrenome.split() # Faz uma lista de sobrenomes
	sobrenome_formatado = sobrenome_split[len(sobrenome_split)-1][0:3].upper() # Armazena as três primeiras letras em maiuscula

	insignificativas = ["a", "ante", "após", "apos", "ate", "até", "com", "contra", "de", "desde", "em", "entre", "para", "per", "perante", "por", "sem", "sob", "sobre", "trás", "a", "os", "o", "as", "um", "uma", "uns", "umas", "do", "no", "ao", "pelo", "dos", "nos", "nos", "aos", "pelos", "da", "na", "à", "pela", "das", "nas", "às", "pelas", "dum", "num", "duns", "nuns", "duma", "numa", "dumas", "numas"]

	title_split = livro.lower().strip('\"').split() # Lista de palavras no nome do livro

	for e, i in enumerate(title_split): # Remove as palavras insignificativas
		if i.lower() in insignificativas:
			title_split.pop(e)

	localizacao_arco = f"{sobrenome_formatado}{title_split[0][0]}"
	return localizacao_arco

def marc(arquivo):
	 # Dicionário para guardar dados

	with open(arquivo, 'rb') as fh:
		reader = MARCReader(fh)
        
		for dados_leitor in reader:
			data = {
				"Autor" : dados_leitor.author(),
				"Livro" : dados_leitor.title()
			}

		localizador = localizacao_arco_nome(data["Autor"], data["Livro"])
		
		return localizador