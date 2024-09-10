def divisao_por_zero():
    try:
        numero = float(input("Digite um número para dividir 1 por ele: "))
        resultado = 1 / numero
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

divisao_por_zero()

def conversao_para_inteiro():
    try:
        texto = input("Digite um número inteiro: ")
        numero = int(texto)
        print(f"O número inteiro é: {numero}")
    except ValueError:
        print("Erro: Valor inválido. Por favor, digite um número inteiro.")

conversao_para_inteiro()

def verificar_indice():
    lista = [10, 20, 30, 40, 50]
    try:
        indice = int(input("Digite um índice para verificar: "))
        valor = lista[indice]
        print(f"O valor no índice {indice} é: {valor}")
    except IndexError:
        print("Erro: Índice fora dos limites da lista.")
    except ValueError:
        print("Erro: Valor inválido para índice. Por favor, digite um número inteiro.")

verificar_indice()

def dividir(a, b):
    try:
        resultado = a / b
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

# Testando a função
dividir(10, 2)
dividir(10, 0)

def conversao_para_decimal():
    try:
        texto = input("Digite um número decimal: ")
        numero = float(texto)
        print(f"O número decimal é: {numero}")
    except ValueError:
        print("Erro: Valor inválido. Por favor, digite um número decimal.")

conversao_para_decimal()

def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")

# Testando a função
abrir_arquivo("arquivo_que_nao_existe.txt")
abrir_arquivo("arquivo_existe.txt")  # Substitua pelo nome de um arquivo existente para testar
