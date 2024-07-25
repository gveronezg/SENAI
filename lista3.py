if False:
    """
    Exercícios.

    1. Exercício: Pergunta Nome
    Peça ao usuário seu nome, endereço, idade, sexo e profissão e imprima em
    uma única mensagem.

    2. Exercício: Soma Simples
    Peça ao usuário 6 números e imprima a soma deles.

    3. Exercício: Idade
    Pergunte o seu ano de nascimento e imprime "Você tem [idade] anos."

    4. Exercício: Cálculo de Quadruplo.
    Pergunte um número ao usuário e imprima o quadruplo desse número.

    5. Exercício: Antecessor, Sucessor e soma entre eles.
    Desenvolva um programa que leia um número inteiro qualquer e que apresente
    o número informado, seguido do seu antecessor, seu sucessor e a soma entre
    eles.

    6. Exercício: Reajuste.
    Faça um algoritmo que leia um valor qualquer e imprima na tela com um
    reajuste de 5%.

    7.Exercício: Salário.
    Faça um algoritmo que efetue o cálculo do salário líquido de um professor. As
    informações fornecidas serão: valor da hora aula, número de aulas lecionadas
    no mês e percentual de desconto do INSS. Imprima na tela o salário líquido
    final.

    8.Exercício: Cálculos.
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e
    mostre: o produto do dobro do primeiro com metade do segundo. a soma do
    triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

    9.Exercício: Peso Ideal
    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
    que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

    10.Exercício: Salário
    Faça um Programa que pergunte quanto você ganha por hora e o número de
    horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
    descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o
    sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS.
    quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário
    líquido, conforme a tabela abaixo

    11. Exercício: Votos
    Escreva um algoritmo para ler o número total de eleitores de um município, o
    número de votos brancos, nulos e válidos. Calcular e escrever o percentual que
    cada um representa em relação ao total de eleitores

    12.Exercício: Dados Inverso
    Crie um algoritmo que leia dois números nas variáveis numA e numB, nessa
    ordem, e os mostre na tela em ordem inversa, isto é, se os dados lidos forem 7
    e 15, por exemplo, devem ser mostrados na ordem 15 e 7, um embaixo do
    outro (em linhas distintas).

    13.Exercício: Cálculo Profundidade
    Crie um programa no qual o usuário deverá inserir os valores da altura, largura
    e profundidade de uma caixa d’água, em cm. No final, exiba o volume dessa
    caixa d’água.
    Dica: Volume = Altura x Largura x Profundidade

    14.Exercício: Lata de óleo
    Faça um algoritmo que calcule e apresente o valor do volume de uma lata de
    óleo, dado seu raio e sua altura.
    V = R X A

    15.Exercício: Resistência
    Um circuito elétrico é composto de três resistências R1, R2 e R3. Faça um
    algoritmo para calcular a resistência equivalente desse circuito.
    R = R1 + R2 + R3
    """

# 1. Peça ao usuário seu nome, endereço, idade, sexo e profissão e imprima em uma única mensagem.
# comando para entrada de dados.
nome = input("Entre com seu nome: ")
endereço = input("Entre com seu endereço: ")
idade = int(input("Entre com sua idade: "))
sexo = input("Entre com seu sexo: ")
profissão = input("Entre com sua profissão: ")
# comando para saida de dados, informa a variavel digitada e seu dobro
print("Olá {}. Seu endereço é: {}. Sua idade é: {}. Seu sexo é: {}. Seu profissão é: {}".format(nome,endereço,idade,sexo,profissão))

# 2. Peça ao usuário 6 números e imprima a soma deles.
n1 = int(input("Entre com o 1º numero: "))
n3 = int(input("Entre com o 2º numero: "))
n4 = int(input("Entre com o 3º numero: "))
n2 = int(input("Entre com o 4º numero: "))
n5 = int(input("Entre com o 5º numero: "))
n6 = int(input("Entre com o 6º numero: "))
print("Somando os 6 numeros que foram inseridos: {}".format(n1+n2+n3+n4+n5+n6))

# 2. Peça ao usuário 6 números e imprima a soma deles.
n1 = int(input("Entre com o 1º numero: "))
n3 = int(input("Entre com o 2º numero: "))
n4 = int(input("Entre com o 3º numero: "))
n2 = int(input("Entre com o 4º numero: "))
n5 = int(input("Entre com o 5º numero: "))
n6 = int(input("Entre com o 6º numero: "))
print("Somando os 6 numeros que foram inseridos: {}".format(n1+n2+n3+n4+n5+n6))

# 3. Pergunte o seu ano de nascimento e imprime "Você tem [idade] anos."
nasc = int(input("Qual seu ano de nascimento? "))
# comando para saida de dados
print("Você deve ter em torno de {} anos de idade.".format(2024-nasc))

# 4. Pergunte um número ao usuário e imprima o quadruplo desse número.
num = int(input("Qual o número que devo quadruplicar? "))
# comando para saida de dados
print("O quadruplo de {} é: {}".format(num,num*4))

# 5. Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado, seguido do seu antecessor, seu sucessor e a soma entre eles.
num = int(input("Entre com algum numero inteiro: "))
ant, suc = num-1, num+1
# comando para saida de dados
print("O número informado foi: {}. Seu antecessor é: {}. Seu sucessor é: {}. E a soma entre eles é: {}".format(num,ant,suc,num+ant+suc))

# 6. Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.
num = float(input("Entre com algum número qualquer: "))



# 10. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. Quanto pagou ao INSS. Quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo.
# pergunte quanto você ganha por hora
hora = int(input("Quanto você ganha por hora? "))
# o número de horas trabalhadas no mês
mes = int(input("Quantas horas você trabalha por mês? "))
# calcule e mostre o total do seu salário no referido mês
salb = hora*mes
# são descontados 11% para o Imposto de Renda
ir = salb*0.11
# 8% para o INSS
inss = salb*0.08
# 5% para o sindicato
sin = salb*0.05
# salário liquido
sall = salb-ir-inss-sin
# mostrando a saída
print("salário bruto: {} R$ | inss: {} R$ | sindicato: {} R$ | salário líquido: {} R$".format(salb,inss,sin,sall))



# 15. Um circuito elétrico é composto de três resistências R1, R2 e R3. Faça um algoritmo para calcular a resistência equivalente desse circuito. R = R1 + R2 + R3
r1 = int(input("Qual o valor da Resistencia 1? "))
r2 = int(input("Qual o valor da Resistencia 2? "))
r3 = int(input("Qual o valor da Resistencia 3? "))
print("A resistêcia equivalente deste circuito é: {}".format(r1+r2+r3))

import math

n = int(input("Digite um número para obter a sua raiz quadrada: "))
raiz = math.sqrt(n)

print("A raiz de {} é {}".format(n,int(raiz)))