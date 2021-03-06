# -*- coding: utf-8 -*-
"""Lista_hackathon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hDK2QYelUn-Cq2FpxSd2zfFmvkylpWbd

# 1º Grande Hackathon de Python!

## **Contexto**

Nesta dinâmica vamos trabalhar com dados de empresas populacionais de 1960 a 2020 e de PIB de 1960 a 2016. 

Teremos listas e dicionários pré-processados para três tipos de dados:


**Metadados:** Mostra informação dos códigos dos países, região, renda e país correspondente.

**População:** Primeira coluna corresponde ao código do país, e demais colunas a cada ano (1960-2016).

**PIB:** Primeira coluna corresponde ao código do país, e demais colunas a cada ano (1960-2016).


Para carregar os dados, certifique-se de fazer o upload do arquivo `dados_mundiais.py` e dos arquivos .csv conforme descrito nas instruções!

Na maioria das questões trabalharemos apenas com dados de populações. Por padrão, `cabecalho` contém os nomes das colunas, `linhas` são as listas das linhas das tabelas, `colunas` lista das colunas e `dicio` a lista de colunas como valores, e nomes das colunas como chave.

Há dados faltantes que estão como "0" mas que não influenciarão nenhuma questão. Cabe ressaltar que se por curiosidade alguém pegar uma linha ou coluna com valor faltante e calcular a média, este valor não será realista porque os 0 entrarão no cálculo da média.

## **Para carregar os bancos de dados execute o código abaixo**
"""

from dados_mundiais import populacao_cabecalho, populacao_linhas, populacao_colunas, populacao_dicio
from dados_mundiais import pib_cabecalho, pib_linhas, pib_colunas, pib_dicio
from dados_mundiais import metadados_cabecalho, metadados_linhas, metadados_colunas, metadados_dicio

"""# **Questões**

## Questão 1

Para praticar lista!! Monte uma lista com números de 0 a 100 com apenas múltiplos de 5 e responda:
    
    a) Qual o terceiro elemento da lista? Considere que ela começa no elemento A[0].
    b) Qual número está no index 10?
"""

q1_lista = range(0, 101, 5)
                  
print(f"Respostas: \n A: {q1_lista[2]}\n B: {q1_lista[9]}")

"""## Questão 2

Utilizando a lista `populacao_linhas` filtre a linha correspondente ao Brasil (`BRA`) e responda:

    a) Qual a população máxima do Brasil nestes dados?
    b) Qual a população mínima do Brasil nestes dados?
"""

for i in populacao_linhas:
  if i[0] == 'BRA':
    a = max(i[1:])
    b = min(i[1:])

print(f"Respostas: \n Qual a população máxima do Brasil nestes dados? R: {a} \n Qual a população mínima do Brasil nestes dados? R: {b}")

#print(populacao_linhas)

"""## Questão 3

Monte uma tupla com todos os códigos de países que começam com "A" (Ex.: ('ABW', 'AFE',...). Sugestão: utilize a primeira coluna dos dados de população para isso `populacao_colunas[0]`. Então responda:

    a) Quantos elementos há na tupla?
    b) Em qual posição (índice) está o código "ARG"
"""

comeca_com_A = []

for i in populacao_colunas[0]:
  if i[0] == 'A': # verifica todos os valores que começam com A
    comeca_com_A.append(i)

print(f"Respostas: \n A: {len(comeca_com_A)} \n B: {comeca_com_A.index('ARG')}")

"""## Questão 4

Monte duas listas: uma com os valores de população do Brasil e uma com os valores de PIB do Brasil. Salve-as nas variáveis `brasil_populacao` e `brasil_pib`, respectivamente.  
Utilize as listas `populacao_cabecalho`, `populacao_linhas`, `pib_cabecalho` e `pib_linhas` para construir a seguinte estrutura:

- Lista com tuplas do ano e seus respectivos valores de população
- Lista com tuplas do ano e seus respectivos valores de PIB
    
Exemplo:

```python
[(1960, 72179235), (1961, 74311338) ... (2020, 212559409)] # brasil_populacao
[(1960, 15165569912.5199), (1961, 15236854859.469) ... (2016, 1796186586414.45)] # brasil_pib
```

E então responda:

    a) Qual a população brasileira em 1960?
    b) Qual o PIB do Brasil em 2000?
"""

brasil_populacao = []
brasil_pib = []

# Separando valores do BRA
brasil_populacao_temp = [i for i in populacao_linhas if i[0] == 'BRA']
brasil_pib_temp = [i for i in pib_linhas if i[0] == 'BRA']

# Transformando em lista simples sem o primeiro valor
brasil_populacao_temp = brasil_populacao_temp[0][1:]
brasil_pib_temp = brasil_pib_temp[0][1:]

#Criando a lista com as tuplas (ano, valor)
for i in zip(populacao_cabecalho[1:], brasil_populacao_temp):
  brasil_populacao.append(i)

for i in zip(pib_cabecalho[1:], brasil_pib_temp):
  brasil_pib.append(i)

print(brasil_populacao)
print(brasil_pib)



"""## Questão 5

Com base nas listas feitas no exercício anterior calcule o PIB per capita (PIB dividido pela população) nos anos de 1960 a 2016 (máximo que temos de dados de PIB).
Construa a mesma estrutura de lista com tuplas anterior agora com o ano e o PIB per capita em cada tupla:

Exemplo:

```python
[(1960, x), (1961, x) ... (2016, x)] # onde x é o pib per capita para aquele ano
```

Então responda:

    a) Qual o PIB per capita em 2016? Arredonde o resultado para o inteiro mais próximo.
    b) Qual ano tivemos o melhor PIB per capita?
    
"""

#Cria pib per capita ano
pib_per_capita_ano = []

for pop in brasil_populacao:
  for pib in brasil_pib:
    if pop[0] == pib[0]:
      pib_per_capita_ano.append((pib[0], pib[1] / pop[1]))

#Avalia pib 2016
for ano in pib_per_capita_ano:
  if ano[0] == '2016':
    pib_per_capita_ano_2016 = round(ano[1])

# Avalia maior PIB
maior_pib = [0,0]
for pib in pib_per_capita_ano:
  if pib[1] >= maior_pib[1]:
    maior_pib = pib

#print(pib_per_capita_ano)
print(f"a) Qual o PIB per capita em 2016? R: {pib_per_capita_ano_2016}")
print(f'b) Qual ano tivemos o melhor PIB per capita? R: {maior_pib[0]}')

"""## Questão 6

Utilize um loop **while** para iterar sobre a lista `bra_pib` criada no exercício 4 e verifique se o PIB do ano em questão foi menor que o PIB do ano anterior.

Na primeira iteração que houver um ano que teve PIB inferior ao ano passado, retorne:

    a) O ano em que houve essa diminuição
    b) Quanto diminuiu, em percentual em relação ao ano anterior (arredonde para que não haja nenhuma casa decimal)
"""

print(brasil_pib)

tam_brasil_pib = len(brasil_pib)
cont = 0
pib = 1
ano = 0
cresc = 0

while True:
  ano_atual = brasil_pib[cont][0]
  pib_atual = brasil_pib[cont][1]
  
  if pib_atual >= pib:
    cresc = 1 - (pib_atual / pib)
    pib = pib_atual
    ano = ano_atual
      
  else:
    break

  cont += 1

print(f"a) O ano em que houve essa diminuição? R: {ano_atual}")
print(f"b) Quanto diminuiu, em percentual em relação ao ano anterior? R: {round(cresc * 100)}%")

print(pib_atual, ano_atual)

"""## Questão 7

Faça uma função que recebe como input uma lista de tuplas (como do exercício 4) e retorna outra lista de tupla com o mínimo, máximo e a média dos valores. Essas estatísticas devem ser aplicadas apenas considerando os segundos elementos das tuplas da lista de entrada. No caso da variável `bra_populacao`, por exemplo, resultaria em estatísticas das populações.

Exemplo:

```python
[('min', x), ('max', x), ('mean', x)] # onde x é a estatística correspondente
```

Aplique sua função na variável `bra_populacao` e responda:

    a) Qual o valor mínimo de população no Brasil nesses dados?
    b) Qual a média da população do Brasil? (arredonde para não ter decimais)
"""

def estatistica(lista):
  
  lista_invertida = []
  for val in lista:
    lista_invertida.append((val[1],val[0]))

  maior_pop = max(lista_invertida)
  menor_pop = min(lista_invertida)

  # Remove valor 0
  lista_invertida_sem_zero = []
  for val in lista_invertida:
    if val[0] > 0:
      lista_invertida_sem_zero.append(val[0])
  
  media_pop = sum(lista_invertida_sem_zero) / len(lista_invertida_sem_zero)

  return [('min', menor_pop[0]), ('max', maior_pop[0]), ('mean', round(media_pop))]

lista_tratada = estatistica(brasil_populacao)
print(lista_tratada)
print(f"a) Qual o valor mínimo de população no Brasil nesses dados? R: {lista_tratada[0][1]}")
print(f"b) Qual a média da população do Brasil? R: {lista_tratada[2][1]}")

"""## Questão 8

Crie uma função que calcule o valor máximo de população para um país-alvo. Sua função deve receber dois parâmetros de entrada: o código do país e os dados das populações em linhas (`populacao_linhas`) e resultar como output o valor máximo populacional para esses país. Lembre que o primeiro item da lista é o código do país e os demais os dados para os anos de 1960 a 2020.

Aplique sua função uma vez para a China (código "CHN") e para os Estados Unidos (código "USA") e responda:

    a) Qual foi a maior população que a China teve entre 2016 e 2020?
    a) Qual foi a maior população que os Estados Unidos teve entre 2016 e 2020?
"""

def popMaxPais(lista, pais):
  
  # Separando valores do BRA
  pais_populacao = [i for i in lista if i[0] == pais]

  return pais_populacao

populacao = popMaxPais(populacao_linhas, 'CHN')
print(max(populacao))

"""## Questão 9

Crie uma função que retorne uma lista com os valores de PIB em dado ano para uma lista de países. Sua lista deve receber como input a lista de países, o ano-alvo, os dados em lista (para essa tarefa utilize a lista `pib_colunas`) e o cabeçalho para a identificação dos anos. 

Exemplo:

```python
get_dados_anuais_por_listapaises(country_codes, target_year, data, data_cabecalho)
get_dados_anuais_por_listapaises(['BRA','USA'], 2015, pib_colunas, populacao_cabecalho)
```

Aplique sua função nos países 'USA','ESP' e 'BRA' (Estados Unidos, Espanha e Brasil) no ano de 2016 com os dados de PIB e responda:

    a) Qual o PIB da Espanha?
    b) Qual o PIB do Brasil?
   
Arredonde seu resultado para não haver decimais.
"""



"""## Questão 10

Crie um dicionário que capture a população e o PIB máximo para uma lista de países. Sua lista de países deve conter os Estados Unidos, Brasil e República Centro-Africana (USA, BRA e CAF, respectivamente). Utilize as variáveis `populacao_linhas` e `pib_linhas` para a construção desse dicionário que deve apresentar a seguinte estrutura:

```python
{
    'pais1': {'max_populacao': 123, 'max_pib': 123},
    'pais2': {'max_populacao': 123, 'max_pib': 123}
}
```

Então responda:

    a) Qual o PIB máximo nos Estados Unidos (USA)?
    b) Qual o PIB máximo na República Centro-Africana (CAF)?
"""



"""## Questão 11

Crie uma função que receba uma lista de valores e adicione em um dicionário quantas vezes cada elemento aparece. Condições importantes:
* Se houver elemento vazio, retirá-lo do dicionário;
* Adicione um parâmetro na função que manterá apenas os N elementos que mais aparecem

Exemplo:

```python
counter(lista, n_largest) # onde 'lista' é a lista e n_largest a quantidade de elementos que mais aparecem
```

- a) Aplique sua função na lista de grupo de renda (`metadadados_dicio['IncomeGroup']`), selecionando o primeiro elemento que mais aparece e responda quantas vezes ele apareceu.
- b) Aplique sua função na lista região (`metadados_dicio['Region']`), selecionando os dois primeiros elementos que mais aparecem e responda quantas vezes **o segundo** elemento apareceu.
    
Exemplo de aplicação da função para obter resultado esperado:

```python
counter(metadados_dicio['IncomeGroup'], n_largest=1) # a
counter(metadados_dicio['Region'], n_largest=2) # b
```
"""



"""## Questão 12

Faça uma função que retorne uma lista com tuplas, cada tupla com dois elementos: a região geográfica e o valor de uma função-alvo (como a soma, por exemplo) de todos os valores de PIB em todos os anos dos países correspondentes à região. 

Por exemplo, as suas regiões-alvos devem ser:

```
target_regions = ['East Asia & Pacific', 'Europe & Central Asia', 'Latin America & Caribbean', 'Middle East & North Africa', 'North America', 'South Asia', 'Sub-Saharan Africa']
```

E você deve utilizar a variável `metadados_dicio` para verificar a correspondência de região e país, e `pib_linhas` para capturar os valores de PIB.  
A sua função receberá as variáveis `metadados_dicio`, `pib_linhas` e `target_regions` como variáveis, além de um parâmetro para definir uma função custom que irá agregar os valores, quer seja soma, mínimo, máximo ou média. 

**Importante:** Há valores nulos que estão como zeros. Remova-os antes de aplicar sua função que irá agregar/resumir estes valores em um único valor (exemplo, valor máximo).

EXEMPLO:

```python
custom_function_per_region(metadados_dicio=metadados_dicio, pib_linhas=pib_linhas, target_regions=target_regions, target_function=max)
```

SAÍDA ESPERADA (neste caso de valor máximo, sem arredondamento):
```
[('Sub-Saharan Africa', 568498937588.035),
 ('Middle East & North Africa', 756350347333.334),
 ('South Asia', 2263792499341.01),
 ('Latin America & Caribbean', 2616201578192.25),
 ('Europe & Central Asia', 3890606893346.69),
 ('East Asia & Pacific', 11199145157649.2),
 ('North America', 18624475000000.0)]
```

Aplique sua função passando a função `min` como função-alvo. Divida os valores por 1 bilhão, faça o arredondamento para que não haja decimais e responda:

    a) Qual o valor mínimo de PIB, em bilhões, para países da América do Norte ('North America')?
    b) Qual o valor mínimo de PIB, em bilhões, para países da África-subsaariana ('Sub-Saharan Africa')?
"""

