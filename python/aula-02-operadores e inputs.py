'''
TIPOS DE OPERADORES NO PYTHON

Podemos usar vários operadores no python

Soma: (+)
subtração: (-) 
multiplicação: (*)
divisão: (/)
divisao_inteira: (//)
modulo: (%)
exponenciação: (**) 

'''

numero_1 = 5
numero_2 = 2

#Exemplo de operadores
soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25

####################################################################

'''
INPUTS PYTHON

inputs entradas em tempo de execução do código.
Então o valor da variável será inserida pelo input do usuário no terminal.

'''

# EXEMPLO DE UTILIZAÇÃO DOS INPUTS

numero_1 = input("insira o valor número 1 para realizar uma soma: ")
numero_2 =input("insira o valor número 2 para realizar uma soma: ")
soma = int(numero_1) + int(numero_2)

print(f"valor número 1: {numero_1}")
print(f"valor numero 2: {numero_2}")
print(f"a soma dos valores é: {soma}")

#####################################################################

