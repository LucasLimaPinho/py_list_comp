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
