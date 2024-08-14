"""
Exercicios.

12. Verifique se um elemento específico está na lista.
13. Conte quantos elementos a lista possui.
14. Some todos os elementos de uma lista de números.
15. Multiplique todos os elementos de uma lista de números.
16. Encontre o maior número em uma lista de números.
17. Encontre o menor número em uma lista de números.
18. Ordene uma lista de números em ordem crescente.
19. Ordene uma lista de números em ordem decrescente.
20. Inverta a ordem dos elementos em uma lista.
21. Crie uma cópia de uma lista.
22. Limpe todos os elementos de uma lista.
23. Verifique se todos os elementos de uma lista são números inteiros.
"""

# lista 10.1. Crie uma lista vazia.
vazia = []

# lista 10.2. Crie uma lista com 5 números inteiros.
lista = [1,2,3,4,5]

# lista 10.3. Crie uma lista com 3 strings.
strings = ['com','três','strings']

# lista 10.4. Crie uma lista mista com números inteiros e strings.
lista = [1,'lista',2,'mista']

# lista 10.5. Acesse o primeiro elemento de uma lista.
lista = [1,'lista',2,'mista']
print(lista[0])

# lista 10.6. Acesse o último elemento de uma lista.
lista = [1,'lista',2,'mista']
print(lista[(len(lista))-1])

# lista 10.7. Acesse o terceiro elemento de uma lista.
lista = [1,'lista',2,'mista']
print(lista[2])

# lista 10.8. Adicione um novo elemento no final da lista.
lista = [1,2,3]
lista.append(4)
print(lista)
# OR
lista += [4]
print(lista)

# lista 10.9. Adicione um novo elemento no início da lista.
lista = [1,2,3]
lista.insert(0,'novo')
print(lista)
# OR
lista = ['novo']+lista
print(lista)

# lista 10.10. Remova o último elemento da lista.
lista = [1,2,3,4,5]
lista = lista[0:(len(lista)-1)]
print(lista)

# lista 10.11. Remova o primeiro elemento da lista.
lista = [1,2,3,4,5]
lista = lista[1:(len(lista))]
print(lista)

# lista 10.12. Verifique se um elemento específico está na lista.
lista = [1,2,3,4,5]
print(3 in lista)

# lista 10.13. Conte quantos elementos a lista possui.
lista = [1,2,3,4,5]
print(len(lista))

# lista 10.14. Some todos os elementos de uma lista de números.
lista = [1,2,3,4,5]
soma = 0
for n in lista:
    soma += n
print('A soma dos números da lista é {}'.format(soma))

# lista 10.15. Multiplique todos os elementos de uma lista de números.
lista = [10,2,3,4]
mult = lista[0]
for n in lista[1:(len(lista))]:
    mult = mult * n
print('A multiplicação dos números da lista é {}'.format(mult))

# lista 10.16. Encontre o maior número em uma lista de números.
lista = [1,20,3,4,5]
maior = lista[0]
for n in lista:
    if n>maior:
        maior = n
print(f'O maior número desta lista é {maior}')

# lista 10.17. Encontre o menor número em uma lista de números.
lista = [10,3,30,40,50]
menor = lista[0]
for n in lista:
    if n<menor:
        menor = n
print(f'O menor número desta lista é {menor}')



# lista 10.18. Ordene uma lista de números em ordem crescente.
# lista 10.19. Ordene uma lista de números em ordem decrescente.
# lista 10.20. Inverta a ordem dos elementos em uma lista.
# lista 10.21. Crie uma cópia de uma lista.
# lista 10.22. Limpe todos os elementos de uma lista.
# lista 10.23. Verifique se todos os elementos de uma lista são números inteiros.