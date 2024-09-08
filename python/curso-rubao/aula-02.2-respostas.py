# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("hello world!")

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input("digite o número: ")
print(f"O número digitado foi: {numero}")

# Faça um Programa que peça dois números e imprima a soma.
num01 = input("digite o primeiro número: ")
num02 = input("digite o segundo número: ")
soma = num01 + num02
print(f"A soma é igual a: {soma}")

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# FORMA 01
nota01 = int(input("nota 01: "))
nota02 = int(input("nota 02: "))
nota03 = int(input("nota 03: "))
nota04 = int(input("nota 04: "))
media = (nota01 + nota02 + nota03 + nota04)/4
print(f"A média das notas é: {media}")

#FORMA 02
nota01 = input("nota 01: ")
nota02 = input("nota 02: ")
nota03 = input("nota 03: ")
nota04 = input("nota 04: ")
media = (int(nota01) + int(nota02) + int(nota03) + int(nota04))/4
print(f"A média das notas é: {int(media)}")

# Faça um Programa que converta metros para centímetros.
mt = float(input("digite qnt de metros: "))
ct = float(mt * 100)
print(f"a quantidade de centimetros é: {ct}")

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# #FORMA 01
print("para calcular a área do quadrado é necessário multiplicar a base x altura")
base = float(input("valor da base: "))
altura = float(input("valor da altura: "))
print(f"tamanho do quadrado {base * altura} e o dobro dessa área é: {(base * altura)*2}")

# #FORMA 02
print("para calcular a área do quadrado é necessário multiplicar a base x altura")
base = float(input("valor da base: "))
altura = float(input("valor da altura: "))
area = base * altura
print(f"tamanho do quadrado da area é: {area}\ndobro dessa área é: {area * 2}")

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
horaTrabalhada = float(input("digite o valor da sua hora de trabalho: "))
horaPorSemana = float(input("digite quantidade de horas trabalhadas no mês: "))
salario = horaTrabalhada * horaPorSemana
print(f"Seu salário é igual à: {salario}")

# # Faça um Programa que pergunte quanto você ganha por mês e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario = float(input("digite o valor da sua hora de trabalho: "))
horaPorMes = float(input("digite quantidade de horas trabalhadas no mês: "))
horaTrabalhada = salario / horaPorMes
print(f"O valor da sua hora trabalhada é: {horaTrabalhada}")

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
Fahrenheit = float(input("digite a temperatura em Fahrenheit: "))
Celsius = 5 / ((Fahrenheit - 32) * 9)
print(f"A temperatura em Celsius é: {Celsius}")

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Celsius = float(input("digite a temperatura em Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
print(f"A temperatura em Celsius é: {Fahrenheit}")