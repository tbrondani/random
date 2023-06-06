# # this is a comment

# '''this is also a comment,
# a big multiline comment
# '''


# var = 1
# print("hello world")

# number = str(10)
# numberr = 10
# bariavel = float("10.5")

# secops = ['tales', 'atila', 'rubens', 'fillipe', 'jon']

# print(type(bariavel)) # float
# print(type(number)) # str
# print(type(numberr)) #int
# print(type(secops)) #list

##### operações com numeros 

# n1 = 5
# n2 = 2

# soma = n1 + n2 
# subtracao = n1 - n2 
# multiplicacao = n1 * n2
# divisao = n1 / n2 
# div_inteira = n1 // n2
# exponenciacao = n1 ** n2 
# modulo = n1 % n2 


########## utilizar inputs no python

# n1 = int(input("insira o valor 1: "))
# n2 = int(input("insira o valor 2: "))
# print(f"valor numero 1: {n1}\nvalor numero 2: {n2}")
# print(f"a soma dos nums é: {n1 + n2}")
# soma = n1 + n2

# print (f"a soma eh: {soma}")

################

# exercicios semana 1 #

#exercises 


# Faça um Programa que mostre a mensagem "Alo mundo" na tela.

##print("helloworld")

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

# n1 = int(input("insira o numero: "))
# print(f"o numero eh: {n1}")

# Faça um Programa que peça dois números e imprima a soma.

#n1 = int(input("insira o valor 1: "))
#n2 = int(input("insira o valor 2: "))
#print(f"valor numero 1: {n1}\nvalor numero 2: {n2}")

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# n1 = int(input("insira nota 1: "))
# n2 = int(input("insira nota 2: "))
# n3 = int(input("insira nota 3: "))
# n4 = int(input("insira nota 4: "))

# print(f"a media eh: {(n1+n2+n3+n4)/4}")


# Faça um Programa que converta metros para centímetros.

# n1 = int(input("insira qtde de metros: "))

# print(f"vc disse: {n1}")
# print(f"convertido eh: {n1 * 1000}cm")

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# n1 = int(input("insira qtde de metros: "))

# print(f"vc disse: {n1}")
# print(f"convertido eh: {n1 * 1000}cm")

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# n1 = int(input("insira qtde de $$$ por hora: "))
# n2 = int(input("insira qtde de horas: "))
# print(f"vc disse $$$: {n1}")
# print(f"vc disse horas: {n2}")
# print(f"seu salario bruto eh: R${n1 * n2}")

# # Faça um Programa que pergunte quanto você ganha por mês e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# n1 = int(input("insira salario: "))
# n2 = int(input("insira qtde de horas: "))
# print(f"vc disse $$$: {n1}")
# print(f"vc disse horas: {n2}")
# print(f"seu salario bruto por hora eh: R${n1 / n2}")

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# n1 = int(input("graus fahrenheit: "))
# transform = round((n1 - 32) * 5/9, 2)
# print(f"a temp de {n1} Fº em Cº eh: {transform} ")

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus 
# Fahrenheit.

# n1 = int(input("graus celsius: "))
# transform= (n1 * 1.8)+(32)
# print(f"a temp de {n1} Cº em Fº eh: {transform} ")



############################################
#AULA3
'''
É muito comum na programação, precisarmos que determinado bloco de código seja executado apenas se determinada condição for satisfeita.

Para esses casos, Python disponibiliza formas de se controlar o fluxo de execução de programas: são as chamadas Estruturas Condicionais IF/ELIF/ELSE.

Um conceito muito importante para se trabalhar com condições em Python é entender o conceito dos Operadores: "==, >=, <=, >, <"

Operador	Tipo	    Valor
==	        Igualdade	Verifica a igualdade entre dois valores.
!=          Igualdade  	Verifica a diferença entre dois valores.
> 	        Comparação	Verificar se o valor A é maior que o valor B.
< 	        Comparação	Verifica se o valor A é menor que o valor B.
>=	        Comparação	Verifica se o valor A é maior ou igual ao valor B.
<=	        Comparação	Verifica se o valor A é menor ou igual ao valor B.
In	        Seqüência	Verifica se o valor A está contido em um conjunto.

# '''

# a = 10
# b = 20
# soma = a + b

# # Estrutura Condicional Simples
# # neste exemplo, conseguimos criar uma condicional simples.

# if soma > 0:
#      print("Maior que Zero.")

# # Estrutura Condicional Composta
# #No exemplo, conseguimos validar a estrutura condicional composta, onde temos uma condicional simples + seu antônimo.

# if soma > 0:
#      print("Maior que Zero.")
# else:
#      print("Menor que Zero.")


# # Estrutura Condicional Aninhada
# '''
# Para usarmos mais de uma condição, usamos as estruturas condicionais aninhadas
# No exemplo conseguimos validar 3 condições: se a soma é igual a 0, se a soma é igual a 0 e se a soma é diferente dos dois resultados dentro do aninhamento que só pode ser menor que 0
# '''

# if soma > 0:
#      print("Maior que Zero.")
# elif soma == 0:
#      print("Igual a Zero.")
# else:
#      print("Menor que Zero.")

# #EXEMPLO: Fala a média das notas bimestrais do aluno e diga se ele foi aprovado ou não

# nota_a = float(input('digita a nota do primeiro bimestre: '))
# nota_b = float(input('digita a nota do segundo bimestre: '))
# nota_c = float(input('digita a nota do terceiro bimestre: '))
# nota_d = float(input('digita a nota do quarto bimestre: '))

# media = (nota_a + nota_b + nota_c + nota_d)/4

# if media >= 5:
#     print(f'Parabéns, você foi aprovado. Sua média é: {media}')
# elif media >= 4 and media <= 4.9:
#     print(f'Estude mais, você está de recuperação. Sua média é: {media}')
# else:
#     print(f'Você reprovou, vai ficar sem video game. Sua média é: {media}')

###EXERCICIOS

#Exercicios aula 2/3 pelo BRABO RUBENS.

# 1-  Faça um Programa que peça dois números e imprima o maior deles.

# n1 = int(input("insira n1: "))
# n2 = int(input("insira n2: "))

# if n1 == n2:
#     print ("numeros iguais, refaça")
# elif n1 > n2:
#     print ("n1 eh maior que n2")
# elif n2 > n1:
#     print("n2 eh maior que n1")

# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# n1 = int(input("insira n1: "))

# if n1 > 0:
#     print ("numero positivo")
# elif n1 < 0:
#     print("numero negativo")

# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


# l1 = str(input("insira letra: "))

# if l1 == str("F"):
#     print ("sexo feminino")
# elif l1 == str("M"):
#     print ("sexo masculino")
# else:
#     print("opcao invalida ou erro no input, apenas 1 caractere eh aceito")

# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# l1 = str(input("insira letra: "))

# if l1 in ('a', 'e', 'i', 'o', 'u'):
#     print ("vogal")
# elif l1 in ('0','1','2','3','4','5','6','7','8','9'):
#     print ("insira uma letra e nao um numero")
# else:
#     print("consoante")



# 5 - Faça um programa para a leitura de duas notas de um aluno e dizer se ele foi aprovado, reprovado ou estar em recuperação
    # A mensagem "Aluno Aprovado", se a média alcançada for maior ou igual a 7;
    # A mensagem "Aluno Reprovado", se a média for menor do que 6;
    # A mensagem "Aluno em recuperação", se a média for maior ou igual a 6 e menor que 7.

# n1 = int(input("insira nota1: "))
# n2 = int(input("insira nota2: "))

# media = (n1+n2)/2
# print("a nota eh:", media)

# if not n1.isdigit() or not n2.isdigit():
#     print("Entrada inválida. Por favor, insira números inteiros.")

# if media >= 7:
#      print ("Aluno Aprovado")
# elif media >= 6 and media <= 7:
#      print("Aluno em Recuperacao")
# elif media < 6:
#      print ("Aluno Reprovado")


# 6 - Um aluno quer saber qual a média ele precisa para passar no último bimestre do ano. 
    # faça um programa que calcule a nota dos três últimos bimestres e mostre quanto falta para ele passar para passar.
    # as notas de cada bimestre vai de 0 a 10, logo, dependendo do valor do último bimestre, mostre em uma mensagem que ele já está reprovado.


# n1 = int(input("insira bimestre1:"))
# n2 = int(input("insira bimestre2:"))
# n3 = int(input("insira bimestre3:"))


# media = (n1+n2+n3)/3
# final = (n1+n2+n3)/4

# if final >= 7:
#      print ("Aluno Aprovado")
# elif media >= 6 and media <= 7:
#      print("Aluno em Recuperacao")
# elif media < 6:
#      print ("Aluno Reprovado")



# Faça um Programa que leia três números e mostre o maior deles.

# n1 = int(input("insira 1:"))
# n2 = int(input("insira 2:"))
# n3 = int(input("insira 3:"))


# if n1 > n2 and n1 > n3:
#      print ("n1 is the best")
# elif n2 > n1 and n2 > n3:
#      print("n2 is the best")
# elif n3 > n1 and n3 > n2:
#      print ("n3 is the best")
# else:
#     print("algo deu errado")



# Faça um Programa que leia três números e mostre o maior e o menor deles.

# n1 = int(input("insira 1:"))
# n2 = int(input("insira 2:"))
# n3 = int(input("insira 3:"))


# if n1 < n2 and n1 < n3:
#      print ("n1 is the lowest")
# elif n2 < n1 and n2 < n3:
#      print("n2 is the lowest")
# elif n3 < n1 and n3 < n2:
#      print ("n3 is the lowest")
# else:
#     print("algo deu errado")

# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

# p1 = int(input("insira 1:"))
# p2 = int(input("insira 2:"))
# p3 = int(input("insira 3:"))


# if p1 < p2 and p1 < p3:
#      print ("p1 is the lowest")
# elif p2 < p1 and p2 < p3:
#      print("p2 is the lowest")
# elif p3 < p1 and p3 < p2:
#      print ("p3 is the lowest")
# else:
#     print("algo deu errado")




# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# n1 = int(input("insira 1:"))
# n2 = int(input("insira 2:"))
# n3 = int(input("insira 3:"))

# lala = [n1, n2, n3]

# lala.sort()
# print("decrescente", lala)
# lala.sort(reverse=True)
# print("crescente", lala)

# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# p = str(input("insira letra: "))

# if p == str("M"):
#     print ("good morning")
# elif p == str("V"):
#     print ("good afternoon")
# elif p == str("N"):
#     print ("good evening")
# else:
#     print("opcao invalida ou erro no input, apenas 1 caractere eh aceito")

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

# nome = str(input("insira seu nome"))
# cargo = str(input(("insira seu cargo")))

# s = float(input("insira seu salario:"))

# p5 = (s/100)*5
# p10 = (s/100)*10
# p15 = (s/100)*15
# p20 = (s/100)*20


# if s <= 1200:
#     sa = s + p20
#     print(f"nome:{nome}\n cargo:{cargo}\n salario pre-reajuste:{s}\n salario pos-ajuste:{sa}\n valor do aumento:{p20}\n percentual aplicado:20%\n ")
# elif s > 1200 and s <= 1800:
#     sa = s  + p15
#     print(f"nome:{nome}\n cargo:{cargo}\n salario pre-reajuste:{s}\n salario pos-ajuste {sa}\n valor do aumento:{p15}\n percentual aplicado:15%\n ")
# elif s > 3000:
#     sa = s  + p5
#     print(f"nome:{nome}\n cargo:{cargo}\n salario pre-reajuste:{s}\n salario pos-ajuste {sa}\n valor do aumento:{p5}\n percentual aplicado:5%\n ")
# else:
#     print ("oops algo deu errado")
#end aula 3#
