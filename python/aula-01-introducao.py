'''
#VARIÁVEIS
Variável é o nome utilizado para definir um ou mais valores que são manipulados pelos programas durante a sua operação

#TIPOS DE DADOS.
Entendendo o que são os tipos de dados no python
temos vários tipos de dados no python, este vai dizer que tipo de dados estamos trabalhando.
Se tentarmos somar um inteiro com uma string, o python vai mostrar um erro de ValueType, porque são tipos diferentes.

'''

# VARIÁVEIS DO TIPO INTEIRO (INT):

var_int = 10 # variável que recebe um tipo inteiro
print(var_int)
print(type(var_int))

# # VARIÁVEIS DO TIPO STRING (STR):

var_string = "Valores entre aspas duplas ("") ou simples ('') para indicar tipo string" # variável que recebe um tipo string
print(var_string)
print(type(var_string))

# # VARIÁVEIS DO TIPO FLOAT (FLOAT):

var_float = 10.5 # variável que recebe um tipo float
print(var_float)
print(type(var_float))

# # VARIAVEIS TIPO LISTA (LIST):

lista = ['laranja', 'maça', 'melancia', 'uva']
print(lista)
print(type(lista))

# VARIAVEIS TIPO DICIONARIO (DICT) " {chave: valor}":

var_dicionario = { #variável do tipo dictionario
    'Nome': 'Renan',
    'Estado': 'sp',
    'Telefone': '982503645'
}

print(type(var_dicionario))

print(var_dicionario['Nome'])
print(var_dicionario['Estado'])
print(var_dicionario['Telefone'])

# VARIAVEIS TIPO TUPLAS (TUPLES):

tuplas = ('rubens', 1, 10.5, ['laranja', 'maça']) #variável do tipo tuplas
print(type(tuplas))
print(tuplas)
