import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# As sequencias container armazenam referências aos objetos que elas contêm,
# que podem ser de qualquer jeito, enquanto as sequências simples armazenam
# fisicamente o valor de cada item em seu próprio espaço de memória e, 
# não como objetos distintos. Desse modo, as sequências simples são mais compactas,
# porém estão limitadas a valores mais primitivos como caracteres, bytes e números.
# Lembrando que dicionários em Python carregam KVP.

# Sequências container: list, tuple, collections.deque
# Sequências simples: str, bytes, bytearray, memoryview, array.array

# Sequências imutáveis: list, bytearray, array.array, collections.deque, memoryview
# Sequências mutáveis: tuple, str e bytes

# O item mais básico de sequência é list - um container mutável. symbols = '$c&*(%$'
symbols = '$c&*(%#@'
codes = []
for symbol in symbols:
    print('a')
    codes.append(ord(symbol))

codes


symbols = '$c&*(%#@'
codes = [ord(symbol) for symbol in symbols]
codes
type(codes)
x = 'my precious'
dummy = [x for x in 'ABC']
x
dummy
dummy2 = [ord(x) for x in 'ABC']
dummy2
# As funções embutidas FILTER e MAP podem ser empregadas em composição
# para fazer o mesmo, porém a legibilidade será prejudicada.


symbols = '$%¨&*:'
beyond = [ord(s) for s in symbols]
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii2 = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond
beyond_ascii
beyond_ascii2
# listcomp costuma ser mais ágil que filter e map.

# listcompos podem gerar listas a partir do produto cartesiano de dois ou mais
# iteráveis. os itens que compõem o produto cartesiano são tuplas compostas de itens
# de todos os iteráveis de entrada. A lista resultante tem um tamanho igual ao tamanho
# dos iteráveis de entrada das multiplicações

# GEra uma lista de tuplas organizadas por cor e, em seguida, por tamanho.
# as listacomps fazem apenas uma coisa: elas criam listas. 


colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color,size) for color in colors for size in sizes]
tshirts
type(tshirts)

# Para preencher outros tipos de sequências, uma genexp é a opção adequada.
# Uma genexp ECONOMIZA MEMÓRIA (expressão geradora).
# genexps utilizam a mesma sintaze das listcompos, porém são delimitadas por parêntes
# e não por colchetes.

# O primeiro argumento para o construtor array define o tipo de armazenamento
# para os números do array

symbols = '$%¨&*:'
tupla = tuple(ord(symbol) for symbol in symbols)
tupla_filtrada = tuple(filter(lambda x:x>127, map(ord,symbols)))
tupla
tupla_filtrada
type(tupla_filtrada)
type(tupla)
import array
array = array.array('I', (ord(symbol)for symbol in symbols))
array
type(array)
array[0]
array[1]
array[2]
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)

# TUPLAS podem ser utilizadas como listas e imutáveis e TAMBÉM como registros
# sem nomes de campos. 
    
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print('%s %s' % passport)

# Operador % atribiuiu para cada item da tupla passport uma posição da string
# de formatação do argumento de print
    
for country,_ in traveler_ids:
    print(country)

latitude, longitude = lax_coordinates # desacomplamento de tupla
latitude
longitude
# O swap é uma aplicação elegante para desacoplamento de tuplas

b, a = a, b


# Outro exemplo de desacoplamento de tupla consiste em prefixar um argumento
# ao chamar uma função

divmod(20,8) # devolve o quociente e resto
t = (20,8)
divmod(*t)
quotient, remainder = divmod(*t)
quotient, remainder

# Outra maneira de pegar apenas alguns itens ao fazer o desempacotamento em uma tupla
# é usar *

# Definir parâmetros de função com *args para capturar quaisquer
# argumentos em excesso é um recurso clássico em Python

a, b, *rest = range (5)
a,b,rest
a, b, *rest = range (10)
a,b,rest
a, b, *rest = range (1000)
a,b,rest
a, b, *rest = range (3)
a,b,rest
a, b, *rest = range (2)
a,b,rest
a, b, *rest = range (5)
a,b,rest

a, *body, c, d = range(5)
a, body, c, d
*head, b, c, d = range(5)
head, b, c, d

# DESEMPACOTAMENTO DE TUPLAS ANINHADAS

metro_areas = [
    ('Tokyo','JP',36.9,(35.68,139.69)),
    ('Dehli NCR','IN',21.9,(28.61,77.2)),
    ('Mexico City','MX',20.1,(19.43,-99.13)),
    ('New Tork-Newark','US',20.1,(40.8,-74.02)),
    ('Sao Paulo','BR',19.6,(-23.54,-46.63))]

print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude,longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name,latitude,longitude))
        
## TUPLAS NOMEADAS
        
# A função collections.namedtuple é uma fábrica (factory) que gera subclasses
# de tuple melhoradas com nomes de campos e um nome de classe - o que ajuda no debugging
# As instâncias de uma classe criada com namedtuple ocupam exatamente a mesma quantidade
# de memória que tuplas porque os nomes dos campos são armazenas na classe. 
# Elas usam menos memória que um objeto normal, pois não armazenam atributos
# em um __dict__ por instância.

from collections import namedtuple
City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722,139.691667))
tokyo
tokyo.population
tokyo.coordinates
tokyo.name
tokyo.country
tokyo[1]
tokyo[0]
tokyo[2]
tokyo[3]
# Dois parâmetros são necessários para criar uma tupla nomeada: um nome de uma classe
# e uma lista de nomes de campos especificados como um iterável de strings ou como uma
# única string delimitada por espaços
# em nosso caso:
# Nome de Uma Classe: 'City'
# String Delimitada por Espaços: 'name country population coordinates'

# Os dados devem ser passados como argumentos posicionais ao construtor 
# em comparação o construtor tuple aceita um único iterável

# Você pode acessar os campos por nome ou pela posição
# NAMEDTUPLE É UMA FUNÇÃO QUE GERA SUBCLASSES. CITY É UMA SUBCLASSE.
# Tokyo é um objeto da subclasse City que vem da função namedtuples
# O uma tupla nomeada tem alguns atributos além daqueles herdados de tuple.
# Abaixo temos os mais úteis: atributo de classe _fields, o método de classe
# _make(iterable) e o método de instância _asdict()

City._fields # quais os atributos da subclasse City que provem da função namedtuple
LatLong = namedtuple('LatLong', 'lat long')
dehli_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889,77.208889))
dehli = City._make(dehli_data)
dehli._asdict()
# _fields é uma tupla com os nomes dos campos da classe
# _make() permite instanciar uma tupla nomeada a partir de um iterável;
###### City*dehli_data() faria o mesmo que City._make(dehli_data)
#._asdict() retorna um collections.OrderedDict criado a partir da instância
# da tupla nomeada. Pode ser usado para exibir os dados da cidade de uma forma bem legível
