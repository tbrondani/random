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

# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# 5 - Faça um programa para a leitura de duas notas de um aluno e dizer se ele foi aprovado, reprovado ou estar em recuperação
    # A mensagem "Aluno Aprovado", se a média alcançada for maior ou igual a 7;
    # A mensagem "Aluno Reprovado", se a média for menor do que 6;
    # A mensagem "Aluno em recuperação", se a média for maior ou igual a 6 e menor que 7.

# 6 - Um aluno quer saber qual a média ele precisa para passar no último bimestre do ano. 
    # faça um programa que calcule a nota dos três últimos bimestres e mostre quanto falta para ele passar para passar.
    # as notas de cada bimestre vai de 0 a 10, logo, dependendo do valor do último bimestre, mostre em uma mensagem que ele já está reprovado.

# Faça um Programa que leia três números e mostre o maior deles.

# Faça um Programa que leia três números e mostre o maior e o menor deles.

# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# Verifica a ordem decrescente entre os números

# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

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