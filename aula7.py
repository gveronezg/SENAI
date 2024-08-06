# 1. Verifique se um número é positivo.
numero = float(input("Digite um número: "))
if numero>0:
    print("O número {} é positivo.".format(numero))
else:
    print("O número {} não é positivo.".format(numero))

# 2. Verifique se um número é negativo.
numero = float(input("Digite um número: "))
if numero<0:
    print("O número {} é negativo.".format(numero))
else:
    print("O número {} não é negativo.".format(numero))

# 3. Verifique se um número é zero.
numero = float(input("Digite um número: "))
if numero<0:
    print("O número {} é negativo.".format(numero))
else:
    print("O número {} não é negativo.".format(numero))

# 4. Verifique se um número é par.
numero = float(input("Digite um número: "))
if numero%2==0:
    print("O número {} é par".format(numero))
else:
    print("O número {} não é par".format(numero))

# 5. Verifique se um número é ímpar.
numero = float(input("Digite um número: "))
if numero%2!=0:
    print("O número {} é ímpar".format(numero))
else:
    print("O número {} não é ímpar".format(numero))

# 6. Verifique se um número é maior que outro.
n1 = float(input("Entre com um número: "))
n2 = float(input("Agora entre com outro número: "))
if n1>n2:
    print("O número {} é maior que {}".format(n1,n2))
else:
    print("O número {} não é maior que {}".format(n1,n2))

# 7. Verifique se um número é menor que outro.
n1 = float(input("Entre com um número: "))
n2 = float(input("Agora entre com outro número: "))
if n1<n2:
    print("O número {} é menor que {}".format(n1,n2))
else:
    print("O número {} não é menor que {}".format(n1,n2))

# 8. Verifique se um número é igual a outro.
n1 = float(input("Entre com um número: "))
n2 = float(input("Agora entre com outro número: "))
if n1==n2:
    print("O número {} é igual a {}".format(n1,n2))
else:
    print("O número {} não é igual a {}".format(n1,n2))

# 9. Verifique se um número é diferente de outro.
n1 = float(input("Entre com um número: "))
n2 = float(input("Agora entre com outro número: "))
if n1!=n2:
    print("O número {} é diferente de {}".format(n1,n2))
else:
    print("O número {} não é diferente de {}".format(n1,n2))

# 14. Verifique se uma pessoa é adulta (idade >= 18).
idade = int(input("Entre com sua idade: "))
if idade>=18:
    print("Você é adultou por ter {} anos.".format(numero))
else:
    print("Você não é adultou por ter {} anos.".format(numero))

# 15. Verifique se uma pessoa é adolescente (idade entre 13 e 17).
idade = int(input("Entre com sua idade: "))
if idade>=13 and idade<=17:
    print("Você é adolescente por ter {} anos.".format(numero))
else:
    print("Você não é adolescente por ter {} anos.".format(numero))

# 16. Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano
ano = int(input("Entre com o ano de seu nascimento: "))
if (2024-ano)>16:
    print("Você poderá votar este ano!")
else:
    print("Você não poderá votar este ano!")

# 17. Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens: ACESSO PERMITIDO caso a senha seja válida. ACESSO NEGADO caso a senha seja inválida.
senha = int(input("Entre com a senha: "))
if senha==1234:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")

# 18. As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.
maças = int(input("Quantas maças foram compradas: "))
if maças>=12:
    total = maças*0.25
else:
    total = maças*0.30
print("O valor da compra é: {} R$".format(total))

# 19. Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas: - para homens: (72.7 * Altura) – 58 - para mulheres: (62.1 * Altura) – 44.7
altura = float(input("Entre com sua altura: "))
entrada = int(input("Entre com :\n1 para Feminino\n2 para Masculino"))
if entrada==1:
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é {:.2f}".format(peso))
elif entrada==2:
    peso = (72.7 * altura) - 58
    print("Seu peso ideal é {:.2f}".format(peso))
else:
    print("Entrada inválida!")

# 20. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte: − Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área − Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área. − Se o número de lados for igual a 5 escrever PENTÁGONO
lados = int(input("Quantos lados tem este polígono regular: "))
medida = int(input("Qual o tamanho em centímetros: "))
if lados==3:
    print("TRIÂNGULO e o valor da área")
elif lados==4:
    print("QUADRADO e o valor da sua área")
elif lados==5:
    print("PENTÁGONO")
else:
    print("FIM!")

# 21. Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso. − Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO. − Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
lados = int(input("Quantos lados tem este polígono regular: "))
medida = int(input("Qual o tamanho em centímetros: "))
if lados>3:
    print("NÃO É UM POLÍGONO.")
elif lados==4:
    print("FIM!")
elif lados>5:
    print("POLÍGONO NÃO IDENTIFICADO.")

# 22. Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que: Triângulo Retângulo: possui um ângulo reto. (igual a 90o) Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90o) Triângulo Acutângulo: possui três ângulos agudos. (menor que 90o)
a1 = float(input("Entre com o 1º ângulo do triângulo: "))
a2 = float(input("Entre com o 2º ângulo do triângulo: "))
a3 = float(input("Entre com o 3º ângulo do triângulo: "))
if a1 or a2 or a3 == 90:
    print("Triângulo Retângulo")
elif a1 or a2 or a3 > 90:
    print("Triângulo Obtusângulo")
elif a1 and a2 and a3 < 90:
    print("Triângulo Acutângulo")

# 23. Faça um programa que leia um número e escreva na tela se o número é menor, igual ou maior que zero.
numero = float(input("Entre com algum número: "))
if numero<0:
    print("O número {} é menor que 0.".format(numero))
elif numero==0:
    print("O número {} é igual a 0.".format(numero))
else:
    print("O número {} é maior que 0.".format(numero))

# 24. O IMC (índice de massa corpórea) indica o grau de obesidade de uma pessoa. Este índice é obtido pelo peso (em kg) dividido pelo quadrado da altura (em metros). A tabela a seguir apresenta as faixas deste índice:
"""
IMC             AVALIAÇÃO
<20             Abaixo do normal
[20,25[         Normal
[25,30[         Sobrepeso
[30,35[         Obesidade leve
[35,40[         Obesidade moderada
>= 40           Obesidade mórbida
"""
peso = float(input("Entre com seu peso (em kg): "))
altura = float(input("Entre com sua altura (em metros): "))
imc = peso / altura*altura
if imc < 20:
    print("Abaixo do normal")
elif imc>=20 and imc<25:
    print("Normal")
elif imc>=25 and imc<30:
    print("Sobrepeso")
elif imc>=30 and imc<35:
    print("Obesidade leve")
elif imc>=35 and imc<40:
    print("Obesidade moderada")
elif imc>=40:
    print("Obesidade mórbida")

# 1. Imprima os números de 1 a 10.
for n in range(1,11):
    print(n)

# 2. Imprima uma mensagem 5 vezes.
for n in range(5):
    print("for em python 5 vezes")

# 3. Imprima os números de 80 a 1 (em ordem decrescente).
for n in range(80,0,-1):
    print(n)

# 4. Imprima os números de 1 a 100, pulando de 5 em 5.
for n in range(1,101):
    if n == 1:
        print(n)
    elif n%5==0:
        print(n)

# 5. Imprima os números de 100 a 1, pulando de 10 em 10.
for n in range(101,0,-1):
    if n%10==0:
        print(n)
    elif n == 1:
        print(n)

# 6. Escreva um algoritmo que exiba 20 vezes a mensagem “Eu gosto de estudar Algoritmos!”.
for n in range(20):
    print("Eu gosto de estudar Algoritmos!")

# 7. Leia o nome do usuário e escreva o nome dele na tela 10 vezes.
nome = input("Entre com seu nome: ")
for n in range(10):
    print("{}".format(nome))

# 8. Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.
negativos = 0
for n in range(1,6):
    valor = int(input(f"Entre com o {n}º valor de a: "))
    if valor<0:
        negativos += 1
print("Dos 5 valores, {} são negativos.".format(negativos))

# 9. Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.
soma = 0
for n in range(1,500):
    if n%3==0:
        if n%2!=0:
            soma += n
print(f"A some deles é: {soma}")

# 10. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.
for n in range(100,201):
    if n%2!=0:
        print("{} é impar!".format(n))

# 11. Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
numero = float(input(f"Entre com algum número: "))
print("Tabuada do {}".format(numero))
for n in range(11):
    print(f'{numero} X {n} = {numero*n:.2f}')

# 12. Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10. Use o formato de apresentação (considerando que o usuário informou o número 5):

# 13. Modifique o algoritmo do exercício 1, de maneira que sejam impressos somente as multiplicações da tabuada cujo resultado seja um número par.
