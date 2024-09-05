x = False
while x == False:
    print('Crie uma senha forte contendo pelo menos 1:')
    print('Letra Maiúscula + Espaço + Letras Minúscula + Número.')
    senha = input()
    apenas_letras = senha.isalpha()
    apenas_espacos = senha.isspace()
    apenas_numeros = senha.isnumeric()
    apenas_maiusculos = senha.isupper()
    apenas_minusculos = senha.islower()
    letras_e_numeros = senha.isalnum()
    titulo = senha.istitle()
    if apenas_letras == True:
        print('A senha não pode conter apenas letras!')
    elif apenas_espacos == True:
        print('A senha não pode conter apenas espaços!')
    elif apenas_numeros == True:
        print('A senha não pode conter apenas números!')
    elif apenas_maiusculos == True:
        print('A senha não pode conter apenas letras maiúsculas!')
    elif apenas_minusculos == True:
        print('A senha não pode conter apenas letras minúsculas!')
    elif letras_e_numeros == True:
        print('A senha não pode conter apenas letras e números!')
    elif letras_e_numeros == True:
        print('A senha não pode conter apenas a 1º letra maiúsculas e as demais minúsculas!')
    else:
        x = True
        print('Senha criada!')
    print()
# -------------------------------------------------------------------------------------------
nota = -1
while (nota < 0) or (nota > 10):
    nota = int(input('Entre com uma nota de 0 a 10.'))
print(f"A nota é {nota}")
# -------------------------------------------------------------------------------------------
user = input('Entre com o nome de usuário: ')
senha = user
while user == senha:
    senha = input('Entre com uma senha diferente do nome de usuário: ')
print('Usuário e Senha cadastrados!')
