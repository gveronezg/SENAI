# 1. Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado.

# pergunta a velocidade do carro
velocidade = int(input('Qual a velocidade do carro? '))
# verifica se a velocidade é superior a 80
if velocidade > 80:
    # mostra a mensagem sobre a multa
    print('Você foi multado!')
else:
    # mostra a mensagem que não foi multado
    print('Siga em frente!')

# 2. Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.

# pergunta o ano de nascimento
nasci = int(input('Qual o ano em que você nasceu? '))
# calcula a idade
idade = 2024 - nasci
# verifica se a idade é maior ou igual a 16
if idade>=16:
    # mostra a mensagem que é permitido votar
    print('Você já pode votar!')

# 3. Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).

# recebe o nome nesta variável
nome = input('Qual é o nome deste aluno? ')
# recebe a 1º nota nesta variável
nota1 = int(input('Qual a 1º nota deste aluno? '))
# recebe a 2º nota nesta variável
nota2 = int(input('Qual a 2º nota deste aluno? '))
# calcula a média nesta variável
media = (nota1+nota2)/2
# verifica se a média foi atingida
if media>=7:
    # retorna a mensagem de bom aproveitamento
    print(f'O aluno {nome} teve um bom aproveitamento! Sua média é: {media}')
else:
    # retorna a mensagem negativa de bom aproveitamento
    print(f'O aluno {nome} não teve um bom aproveitamento! Sua média é: {media}')

# 4. Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

# recebe o numero inteiro nesta variável
n = int(input('Entre com um número inteiro: '))
# verifica se o numero tem resto 0 quando dividido por 2
if n%2==0:
    # apresenta a mensagem de número par
    print(f'O número {n} é par!')
else:
    # apresenta a mensagem de número ímpar
    print(f'O número {n} é ímpar!')

# 5. Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
# ➢ Homens ganham 5% de desconto
# ➢ Mulheres ganham 13% de desconto

# pergunta ao usuário o nome e armazena nesta variável
nome = input('Entre com seu nome: ')
# pergunta ao usuário o sexo e armazena nesta variável
sexo = str(input('Qual seu sexo, m ou f? ')).lower()
if sexo not in ('m', 'f'):
    # mensagem de erro
    print('Sexo inválido!')
else:
    # pergunta ao usuário o valor e armazena nesta variável
    valor = float(input('Entre com o valor total de sua compra: '))
    # verifica se o usuário é do sexo masculino
    if sexo=='m':
        # calcula o valor descontado para homens
        descontado = valor*0.95
    elif sexo=='f':
        # calcula o valor descontado para mulheres
        descontado = valor*0.87
    # apresenta o valor com desconto para o cliente
    print('{}, sua conta caiu para: {} R$'.format(nome,descontado))

# 6. Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km, calcule o preço da passagem cobrando:
# ➢ R$0.50 por Km para viagens até 200Km e
# ➢ R$0.45 para viagens mais longas.

# pergunta ao usuário a quantidade de kms a rodar e armazena nesta variável
kms = float(input('Quantos KMs este passageiro deseja percorrer? '))
# verifica se a kilometragem é inferior ou igual a 200
if kms<=200:
    # apresenta o valor da passagem
    print('O preço da passagem é de: {} R$'.format(kms*0.5))
else:
    # apresenta o valor da passagem
    print('O preço da passagem é de: {} R$'.format(kms*0.45))

# 7. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

# inicia a variável em 100 para realizar os loops
i = 100
# inicia o loop até 200
while i<200:
    # verifica se o numero tem resto diferente de 0 quando dividido por 2
    if i%2!=0:
        # mostra a mensagem de que o número em questão é ímpar
        print(f'{i} este número é ímpar!')
    # soma 1 ao valor em questão antes do próximo loop
    i += 1

# 8. Números ímpares até 20: Escreva um programa que imprima todos os números ímpares de 1 até 20 usando um loop while.

# inicia a variável em 1 para realizar os loops
i = 1
# inicia o loop até 20
while i<20:
    # verifica se o numero tem resto diferente de 0 quando dividido por 2
    if i%2!=0:
        # mostra a mensagem de que o número em questão é ímpar
        print(f'{i} este número é ímpar!')
    # soma 1 ao valor em questão antes do próximo loop
    i += 1

# 9. Calcular Área de um Retângulo: Crie uma função que recebe a largura e a altura de um retângulo e retorna a sua área. A= largura X altura

# cria a função para calcular a área e solicita 2 parametros (Largura e Altura)
def area(l,a):
    # calcula a área de acordo com os 2 parametros
    area = l*a
    # retorna a área já calculada
    return (area)
# pergunta ao usuário a largura do retangulo
largura = float(input('Entre com a largura do retangulo: '))
# pergunta ao usuário a altura do retangulo
altura = float(input('Entre com a altura do retangulo: '))
# chama a função com base nos valores recebidos, para receber o calculo da área
area = area(largura,altura)
# devolve a mensagem com o valor da área calculado pela função
print(f'A área deste retangulo é {area}')
