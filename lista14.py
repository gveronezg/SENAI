# lista14.1) Calcule a raiz quadrada de um número digitado pelo usuário math.sqrt()
n = int(input('Entre com um número inteiro: '))
from math import sqrt
print(sqrt(n))

# lista14.2) Calcule a raiz quadrada arredondado para cima math.ceil()
n = int(input('Entre com um número inteiro: '))
from math import sqrt,ceil
raiz = sqrt(n)
print(ceil(raiz))

# lista14.3) Calcule a raiz quadrada arredondado para baixo math.floor()
n = int(input('Entre com um número inteiro: '))
from math import sqrt,floor
raiz = sqrt(n)
print(floor(raiz))

# lista14.4) Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. math.trunc()
n = int(input('Entre com um número real: '))
from math import trunc
print(trunc(n))

# lista14.5) Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. hipotenusa = math.hypot(catetoOposto,catetoAdjacente)
co = int(input('Entre com o cateto oposto: '))
ca = int(input('Entre com o cateto adjacente: '))
from math import hypot
print(hypot(co,ca))

# lista14.6) Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. seno = math.sin(math.radians(angulo)) cosseno = math.cos(math.radians((angulo))) tangente = math.tan(math.radians(angulo))
ang = int(input('Entre com um angulo qualquer: '))
from math import sin,cos,tan
print(sin(ang))
print(cos(ang))
print(tan(ang))

# lista14.7) Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude  ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. Import random (Dica) leia quatro números em variáveis do tipo string e depois adicione em uma lista escolhido = random.choice(lista)
# Cria uma lista para armazenar os nomes dos alunos
alunos = []
# Coleta os nomes dos alunos
for i in range(4):
    nome = input(f'Entre com o nome do {i+1}º aluno: ')
    alunos.append(nome)
import random
# Sorteia um aluno aleatoriamente
escolhido = random.choice(alunos)
# Exibe o nome do aluno escolhido
print(f'O aluno sorteado foi: {escolhido}')

# lista14.8) O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. lista = [n1,n2,n3,n4] random.shuffle(lista)
alunos = []
# Coleta os nomes dos alunos
for i in range(4):
    nome = input(f'Entre com o nome do {i+1}º aluno: ')
    alunos.append(nome)
import random
# Sorteia a ordem dos alunos
random.shuffle(alunos)
# Exibe a ordem de apresentação
print(f'A ordem de apresentação é: {alunos}')