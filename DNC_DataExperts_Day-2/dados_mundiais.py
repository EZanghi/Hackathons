with open('metadados_paises.csv') as file:
	metadados_cabecalho = file.readline().strip('\n').split(',')
	metadados_linhas = [line.strip('\n').split(',') for line in file]
	metadados_colunas = [list(line) for line in zip(*metadados_linhas)]
	metadados_dicio = {k:v for k,v in zip(metadados_cabecalho, metadados_colunas)}


with open('populacao_mundial.csv') as file:
	populacao_cabecalho = file.readline().strip('\n').split(',')
	populacao_linhas = []
	for line in file:
		line = line.strip('\n').split(',')
		line[1:] = map(int, line[1:])
		populacao_linhas.append(line)
	populacao_colunas = [list(line) for line in zip(*populacao_linhas)]
	populacao_dicio = {k:v for k,v in zip(populacao_cabecalho, populacao_colunas)}
	

with open('dados_pib_paises.csv') as file:
	pib_cabecalho = file.readline().strip('\n').split(',')
	pib_linhas = []
	for line in file:
		line = line.strip('\n').split(',')
		line[1:] = map(float, line[1:])
		pib_linhas.append(line)
	pib_colunas = [list(line) for line in zip(*pib_linhas)]
	pib_dicio = {k:v for k,v in zip(pib_cabecalho,pib_colunas)}
