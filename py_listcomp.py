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

# TUPLE COMO LISTA IMUTÁVEL: aceita todos os métodos de list que não envolvam
# acrescentar ou remover itens - uma vez que tuplas são imutáveis. 
# Outra exceção: tuplas não possuem o método __reversed__


# Slicing

s = 'bicycle'
s[::3]
s[::-1] # inverte a palavra
s[::-2]

l = list(range(10))
l[2:5]
l[2:5] = [20,30]
l
del l[5:7]
l
l[3::2] = [11,22]
l[2:5] = 100
l[2:5] = [100]
l
# Quando o alvo da distribuição é uma fatia, o lado direito deve ser um objeto iterável
# mesmo que tenha apenas um item

l = [1,2,3]
l*5
5*'abcd'
# Tanto + quanto * sempre criam um novo objeto e jamais alteram seus operandos.

board = [['_']*3 for i in range(3)]
board
board[1][2] = 'X'
board

# __iadd__ é o método especial (dunder method) que faz funcionar a adição combinada (+=)
# "in place addition"
# Quando __iadd__ não estiver implementado, o Python usará __add__ como alternativa

l = [1,2,3]
id(l)
l*=2
l
id(l)
t=(1,2,3)
type(t)
id(t)
t*=2
id(t)
t
# ID da lista inicial
# Após a multiplicação, a lista será o mesmo objeto, com novos itens acrescentados
# Para o caso da Tupla, o ID se altera por se tratar de uma SEQUENCIA IMUTAVEL
# Após a múltiplicação, uma nova tupla foi criada.

# A concatenação repetida de sequências imutáveis é ineficiente, pois, em vez de simplesmente
# concatenar novos itens, o interpretador prcisar copiar toda a sequência-alvo para criar
# uma nova sequência com os novos itens concatenados.]
# Uma exceção é o STR. Pelo fato de a criação de strings com += em laçoes ser bem comum,
# o CPython está otimizado para esse caso de uso. As instâncias de str são alocadas em memória
# com espaço extra de mood que a concatenação não exigirá uma cópia de string completa 
# todas as vezes.

t = (1,2,[30,40])
t[2] += [50,60]
t
# Resultado inesperado: o item t2 é alterado e uma exceção é gerada.

#LIST.SORT e função embutida sorted

#o método list.sort ordena uma lista in-place - isto é, sem criar uma cópia. 
# ele devolve None para nos lembrar de que o objeto-alvo é alterado e que não foi criada
# uma nova lista. Essa é uma convenção importante da API de Python: as funções ou os métodos que
# alteram um objeto in place devolvem NONE para deixar claro a quem chamou que o objeto em si
# foi alterado e nenhum objeto novo foi criado. 
# O mesmo comportamento pode ser visto, por eemplo, na função random.shuffle.

# A convenção de devolver None para indicar alterações in place tem uma desvantagem:
# não é possível chamar esses métodos em cascata;

# Por outr lado, a função embutida sorted cria uma nova lista e a retorna. Na verdade,
# ela aceita qualquer objeto iterável como argumento, ioncluindo sequencias imutáveis e geradores.

# o parâmetro KEY tanto para o método .sort quando para sorted é uma função de um só argumento
# aplicada a cada item para gerar a sua chave de ordenação.

fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
sorted(fruits, reverse=True)
sorted(fruits, key = len)
sorted(fruits, key = len, reverse = True)
fruits.sort() #ordenamento in place
print(fruits.sort()) #Retorna None
fruits # lista ordenada in place

# Administrando sequências ordenadas com bisect

# o módulo bisecr oferece duas funções principais - bisect e insort.
# Usam algoritmo de busca binária para encontrar rapidamente e inserir itens
# em qualquer sequência ordenada
# bisect (haystack, needle) -> haystack deverá ser uma sequência ordenada.
# Todos os itens que aparecerem até essa posição são menores ou iguais a needle - mantendo
# haystack em ordem crescente com a sua inserção

import bisect
import sys
HAYSTACK =  [1,4,5,6,8,12,15,20,21,23,26,29,30]
NEEDLE = [0,1,2,5,8,10,22,23,29,30,31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
def demo(bisect_fn):
    for needle in reversed(NEEDLE):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle,position,offset))
if __name__ == '__main__':
    if sys.argv[-1]=='left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('DEMO:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)

def grade(score,breakpoints=[60,70,80,90],grades='FDCBDA'):
    i = bisect.bisect(breakpoints, score)
    return grandes[i]

# Inserção com bisect.insort

import bisect 
import random

SIZE =7
random.seed(1729)

my_list = []
for i in rang(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list,new_item)
    print('%2d ->' new_item, my_list)
    
# Criando, salvando e carregando um array grande de números de ponto flutuante

from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
floats[-1]
fp=open('floats.bin','wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]
floats2==floats #True

# MemoryViews

#Alterando valor de um item do array ao mudar um de seus bytes

numbers = array('h', [-2,-1,0,1,2])
memv = memoryview(numbers)
len(memv)
memv_oct = memv.cast('B') # Cria memv_oct ao fazer o casting dos elementos de memv para o typecode 'B' -> unsigned char
memv_oct.tolist()
memv_oct[5] = 4 # Atribui o valor 4 ao byte de offset 5
# Oserve a mudança em numbers: um 4 no nobre mais significativo de um inteiro de dois bytes sem sinal é 1024
numbers

# Operação básicas com linhas e colunas em um numpy.ndarray

import numpy
a = numpy.arange(12)
type(a)
a.shape
a.shape = 3,4
a[2]
a[2,1]
a[:,1]
a.transpose()
floats = numpy.loadtxt('floats-19M-lines.txt')
floats[-3:]
floats *=.5
floats[-3:]
from time import perf_counter as pc
t0 = pc();
floats /=3;
pc() - t0
numpy.save('floats-10M.npy', 'r+')
floats2 = numpy.load('floats-10M.npy','r+')
floats2 *=6
floats2[-3:]

# Trabalhando com um deque

from collection import deque

dq = deque(range(10), maxlen=10)
dq
dq.rotate(3)
dq
dq.rotate(-4)
dq
dq.appendleft(-1)
dq
dq.extend([11,22,33])
dq
dq.extendleft([10,20,30,40])
dq
     
# Se estivermos lidando com lista de números, arrays é mais prático. 
# Usamos muito mais lista porque é bem mais prático.
    
# O tipo list é flexível e fácil de usar, porém, dependendo dos requisitos específicos,
# há oções melhores. Por exemplo, se houver necessidade de armazenar 
# dez milhões de valores de ponto flutuante, um ARRAY será muito mais eficiente,
# pois um ARRAY não armazena objetos FLOAT COMPLETOS, mas apenas os BYTES COMPACTOS que presentam
# seus valores na máquina. Assim como um array na linguagem C. 
# o array possui métodos adicionais para carregar e salvar rapidamente
# por exemplo: .frombytes e .tofile

# Se estivermos lidando com lista de números, arrays é mais prático. 
# Usamos muito mais lista porque é bem mais prático.
    
# O tipo list é flexível e fácil de usar, porém, dependendo dos requisitos específicos,
# há oções melhores. Por exemplo, se houver necessidade de armazenar 
# dez milhões de valores de ponto flutuante, um ARRAY será muito mais eficiente,
# pois um ARRAY não armazena objetos FLOAT COMPLETOS, mas apenas os BYTES COMPACTOS que presentam
# seus valores na máquina. Assim como um array na linguagem C. 
# o array possui métodos adicionais para carregar e salvar rapidamente
# por exemplo: frombytes e .tofile

# A classe MEMORYVIEW embutida é um tipo de sequ~encia de memória compartilhada que permite lidar
# com fatias de arrays sem copiar os bytes. Foi insirada na biblioteca NumPy
# Uma MEMORYVIEW é essencial uma estrutura de array NumPy genérica no próprio Python
# (sem a matemática). Ela permite compartilhar memória entre estruturas de dados
# (informações como imagens PIL, banco de dados SQLite, arrays de Numpy, etc). sem fazer uma cópia inicial.
# Isso é muito importante para BIG DATA!
# O método da classe memoryvier chamado memoryview.cast permite alterar o modo como vários bytes são lidos ou escritos
# como unidades sem mover os dados por aí (como o operador cast em C). memoryview.cast devolve outro objeto
# memoryview, sempre compartilhando a mesma memória.


