# Atributos e métodos de array Numpy

import numpy as np

km = np.array([44410., 5712., 37123., 5534., 25757.])
anos = np.array([2003, 1991, 1990, 2022, 2006])
dados = np.array([km, anos])

print('ATRIBUTOS:')

# ndarray.shape -- número de linhas e colunas
print(f'.shape: {dados.shape}')

# ndarray.ndim -- dimensão do array (nesse caso 2: linhas e colunas)
print(f'.ndim: {dados.ndim}')

# ndarray.size -- números de elementos
print(f'.size: {dados.size}')

# ndarray.dtype -- tipo dos elementos
print(f'.dtype: {dados.dtype}')

# ndarray.T -- arrat transposto (transforma linhas em colunas e vice-versa)
print(f'.T:\n{dados.T}')  # .transpose() é a mesma coisa

print('\nMÉTODOS:')

# ndarray.tolist -- transforma array numpy em lista python
print(f'.tolist(): {dados.tolist()}')

# ndarray.reshape -- retorna um array com os mesmos dados, mas com uma nova forma
print(f'.reshape():\n{dados.reshape((5, 2), order="C")}')  # existem formas diferentes de indexar, ex: order='F'

# ndarray.resize -- altera a forma e o tamanho do array
print(f'.resize():')
dados_new = dados.copy()
print(dados_new)
dados_new = dados_new.re

