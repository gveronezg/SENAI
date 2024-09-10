# 1) Crie uma função que verifica se uma variável contém apenas números

def contem_numeros(var):
    if var.isnumeric():
        return ('A variável {} contém apenas números'.format(var))
    else:
        return ('A variável {} não contém apenas números'.format(var))

variavel = input('Digite algo: ')
print(contem_numeros(variavel))

# 2) Crie uma função que verifica se uma string é minúscula

def é_minúscula(str):
    if str.isalpha():
        if str.islower():
            return ('A string {} contém apenas letras minúsculas'.format(str))
        else:
            return ('A string {} não contém apenas letras minúsculas'.format(str))
    else:
        return ('A string {} não contém apenas letras'.format(str))

string = str(input('Entre com uma string: '))
print(é_minúscula(string))

# 3) Crie uma função que verifica se uma string é maiúscula

def é_maiúscula(str):
    if str.isalpha():
        if str.isupper():
            return ('A string {} contém apenas letras maiúscula'.format(str))
        else:
            return ('A string {} não contém apenas letras maiúscula'.format(str))
    else:
        return ('A string {} não contém apenas letras'.format(str))

string = str(input('Entre com uma string: '))
print(é_maiúscula(string))

# 4) Crie uma função que verifica se uma string começa com uma letra específica

def começa_com(str,letra):
    if str.startswith(letra):
        return ('A string {} começa com a letra {}'.format(str,letra))
    else:
        return ('A string {} não começa com a letra {}'.format(str,letra))

letra = str(input('Entre com uma letra qualquer: '))
string = str(input('Entre com uma string: '))
print(começa_com(string,letra))

# 5) Crie uma função que verifica se uma string termina com uma letra específica

def começa_com(str,letra):
    if str.endswith(letra):
        return ('A string {} termina com a letra {}'.format(str,letra))
    else:
        return ('A string {} não termina com a letra {}'.format(str,letra))

letra = str(input('Entre com uma letra qualquer: '))
string = str(input('Entre com uma string: '))
print(começa_com(string,letra))

# 6) Crie uma função que verifica se um valor é um número inteiro

# 7) Crie uma função que verifica se uma string contém apenas espaços em branco

def em_branco(str):
    if str.isspace():
        return ('A string {} contém apenas espaços em branco'.format(str))
    else:
        return ('A string {} não contém apenas espaços em branco'.format(str))

string = str(input('Entre com uma string: '))
print(em_branco(string))
