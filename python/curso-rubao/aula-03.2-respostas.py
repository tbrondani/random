# 1-  Faça um Programa que peça dois números e imprima o maior deles.
# num1 = 10
# num2 = 20

# if num1 > num2:
#     print(f'o maior número é: {num1}')
# else:
#     print(f'o maior número é: {num2}')

# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# num3 = 23232332222
# div = num3 % 2
# if div != 0:
#     print("esse numéro é impar")
# else:
#     print("esse numéro é par")


# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# letra = 'M'
# if letra.lower() == 'f':
#     print("F - Feminino")
# elif letra.lower() == 'm':
#     print("M - Masculino")
# else:
#     print("Sexo inválido")


# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# vogal = ('a','e','i','o','u')
# consoante = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
# letra = '3'
# if letra.lower() in vogal:
#     print('isso é um vogal')
# elif letra.lower() in consoante:
#     print('isso é um consoante')
# else:
#     print("isso não é vogal ou consoante.")

# 5 - Faça um programa para a leitura de duas notas de um aluno e dizer se ele foi aprovado, reprovado ou estar em recuperação
    # A mensagem "Aluno Aprovado", se a média alcançada for maior ou igual a 7;
    # A mensagem "Aluno Reprovado", se a média for menor do que 6;
    # A mensagem "Aluno em recuperação", se a média for maior ou igual a 6 e menor que 7.

# 6 - Um aluno quer saber qual a média ele precisa para passar no último bimestre do ano. 
    # faça um programa que calcule a nota dos três últimos bimestres e mostre quanto falta para ele passar para passar.
    # as notas de cada bimestre vai de 0 a 10, logo, dependendo do valor do último bimestre, mostre em uma mensagem que ele já está reprovado.

nota_bimestre1 = float(input("Digite a nota do primeiro bimestre: "))
nota_bimestre2 = float(input("Digite a nota do segundo bimestre: "))
nota_bimestre3 = float(input("Digite a nota do terceiro bimestre: "))

media_atual = (nota_bimestre1 + nota_bimestre2 + nota_bimestre3) / 3

nota_minima_passar = 5  # Nota mínima para passar

if media_atual >= nota_minima_passar:
    print("Parabéns! Você já está aprovado.")
else:
    nota_bimestre4 = float(input("Digite a nota do quarto bimestre: "))
    media_desejada = (media_atual * 3 + nota_bimestre4) / 4
    falta_para_passar = nota_minima_passar * 4 - media_atual * 3
    if media_desejada < nota_minima_passar:
        print("Você está reprovado. Sua média atual é:", media_atual)
    else:
        print("Para passar, você precisa obter a média", media_desejada)
        print("Falta(m) {:.2f} ponto(s) para passar.".format(falta_para_passar))

# Faça um Programa que leia três números e mostre o maior deles.

num1 = 20
num2 = 40
num3 = 3

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = 10
num2 = 20
num3 = 30

# Encontrar o maior número
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Encontrar o menor número
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("O maior número é:", maior)
print("O menor número é:", menor)



# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 < preco2 and preco1 < preco3:
    print("Você deve comprar o primeiro produto.")
elif preco2 < preco1 and preco2 < preco3:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")

# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica a ordem decrescente entre os números
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
meio = (num1 + num2 + num3) - (maior + menor)

print("Os números em ordem decrescente são:", maior, meio, menor)
# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = input("Em qual turno você estuda? Digite M - para Matutino, V - para Vespertino ou N - para Noturno: ")

if turno == "M" or turno == "m":
    print("Bom dia!")
elif turno == "V" or turno == "v":
    print("Boa tarde!")
elif turno == "N" or turno == "n":
    print("Boa noite!")
else:
    print("Valor inválido!")
# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    # salários até R$ 1200,00 (incluindo) : aumento de 20%
    # salários entre R$ 1200,00 e R$ 1800,00 : aumento de 15%
    # salários entre R$ 1800,00 e R$ 3000,00 : aumento de 10%
    # salários acima de 3000,00 : aumento de 5% Após o aumento ser realizado, informe na tela:
        # nome do funcionário
        # cargo do funcionário
        # o salário antes do reajuste;
        # o percentual de aumento aplicado;
        # o valor do aumento;
        # o novo salário, após o aumento.

nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário atual do funcionário: "))

percentual_aumento = 0
if salario <= 1200.00:
    percentual_aumento = 20
elif salario <= 1800.00:
    percentual_aumento = 15
elif salario <= 3000.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento

print("Nome do funcionário:", nome)
print("Cargo do funcionário:", cargo)
print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento aplicado:", percentual_aumento, "%")
print("Valor do aumento: R$", valor_aumento)
print("Novo salário após o aumento: R$", novo_salario)