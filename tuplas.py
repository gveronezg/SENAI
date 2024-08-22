# Lista 12.1. Crie uma tupla vazia.
tupla = ('')

# Lista 12.2. Crie uma tupla com 5 números inteiros.
numeros = (1,2,3,4,5)

# Lista 12.3. Crie uma tupla com 3 strings.
strings = ('um','dois','três')

# Lista 12.4. Crie uma tupla mista com números inteiros e strings.
mista = (1,'um',2,'dois',3,'três')

# Lista 12.5. Acesse o primeiro elemento de uma tupla.
mista = (1,'um',2,'dois',3,'três')
print(mista[0])

# Lista 12.6. Acesse o último elemento de uma tupla.
mista = (1,'um',2,'dois',3,'três')
print(mista[-1])

# Lista 12.7. Acesse o terceiro elemento de uma tupla.
mista = (1,'um',2,'dois',3,'três')
print(mista[2])

# Lista 12.8. Verifique o comprimento de uma tupla.
mista = (1,'um',2,'dois',3,'três')
print(len(mista))

# Lista 12.9. Concatene duas tuplas.
numeros = (1,2,3)
strings = ('um','dois','três')
juntas = numeros + strings
print(juntas)

# Lista 12.10. Repita uma tupla 3 vezes.
for i in range(3):
    tupla = (1,2,3)
    print(tupla)

# Lista 12.11. Verifique se um elemento específico está presente na tupla.
numeros = (1,2,3)
n = int(input('Entre com o numero que deseja verificar se esta presente na tupla: '))
print(f'Tupla: {numeros}')
if n in numeros:
    print('O numero {} está na lista!'.format(n))
else:
    print('O numero {} não está na lista!'.format(n))

# Lista 12.12. Conte quantas vezes um elemento aparece na tupla.
numeros = (1,2,3,2,3,3)
n = int(input('Entre com algum numero: '))
print(f'Tupla: {numeros}')
contador = 0
for x in numeros:
    if n == x:
        contador +=1
print(f'O numero {n} aparece {contador} vezes na tupla!')

# Lista 12.13. Encontre o índice de um elemento específico na tupla.
times = ('corinthians', 'palmeiras', 'santos', 'são paulo')
print(times)
time = input("Você deseja saber a posição de qual time? ")
posicao = times.index(time)
print(f'O {time} está na {posicao} posição.')

# Lista 12.14. Verifique se uma tupla está vazia.
vazia = ()
cheia = (1,2,3)
if len(vazia)==0:
    print(f'Essa tupla está vazia!')
if len(cheia)>0:
    print(f'Essa tupla não está vazia!')
