# SENAI

1º Aula - 22/07/2024 ###########################################################################################################

Algoritmo
	Sequência finita de passos que levam à execução de uma tarefa.
	Sequência de instruções para um fim específico.

Tripé do algoritmo
	Entrada de Dados
	Processamento
	Saída

Forma de apresentação:
	Descrição Narrativa
	Fluxograma
	Pseudocódigo

Algoritmo para realizar a troca de um pneu furado:
	1-Pegar o macaco e a chave de roda.
	2-Pegar o step.
	3-Levantar o carro com o macaco.
	4-Retirar a roda furada.
	5-Colocar o step.
	6-Abaixar o carro.
	7-Guardar a roda furada.
	8-Guardar o macaco e a chave de roda.

2º Aula - 23/07/2024 ###########################################################################################################

WI-FI-EDUC
ac6ce0ss4@educ
https://www.online-python.com/
https://luizpedroprofessor.blogspot.com/p/python.html

Variavel = valor que pode ser modificado ao longo do algoritmo
Constante = valor que é criado e fixado duranto todo o algoritmo

Tipos de dados
	caracter = texto entre aspas
 	inteiro = negativos e positivos
  	real = numero que tem pontuação
   	lógico = verdadeiro e falso

print() = printa dados
input() = recebe dados

Operadores Matemáticos
	+ adição
	- subtração
	* multiplicação
	/ divisão
	** exponenciação

Operadores Relacionais
	== igual
 	!= diferente
  	> maior
   	>= maior ou igual
    	< menor
	<= menor ou igual
 
Operadores Lógicos
	e = and
 	ou = or
  	não = not

Tabela Verdade
	AND
 		T and T = T
   		T and F = F
     		F and T = F
       		F and F = F
	OR
 		T or T = T
   		T or F = T
     		F or T = T
       		F or F = F
   	NOT
 		not T = F
   		not F = T

3º Aula - 24/07/2024 ###########################################################################################################

PYTHON
	linguagem de alto nivel
 	orientada a objetos
  	tipagem dinânima e forte
   	fácil aprendizagem
    	comunidade ativa
     	muitas bibliotecas/recursos
      	linguagem interpretada

7º Aula - 05/08/2024 ###########################################################################################################

Estrutura de Repetição
	For (para) = determinadas vezes
	While (enquanto) = infinitas vezes

For {referência} in {sequência}:
	{bloco de código}
 
for n in range(10000):
    print(n)

for n in range(5,16):
    print(n)
    
for n in range(15,6,-1):
    print(n)

8º Aula - 06/08/2024 ###########################################################################################################

While = Enquanto

inicializando
x = 1
while x<= 15:
    print(x)
    # incrementando
    x=x+1

contador = 0
acumulador = 0
media = 0
valor = float(input("Entre com um numero positivo: "))

while valor>0.0:
    contador = contador + 1
    acumulador = acumulador + valor
    # Entrada de valores
    valor = float(input("Entre com um numero não positivo para encerrar: "))
    
media = acumulador / contador
print("Total da soma dos numeros: {}".format(acumulador))
print(f"Total de numero digitados: {contador}")
print("Media: ",media)

9º Aula - 07/08/2024 ###########################################################################################################

FUNÇÕES
def nome_da_função (parâmetros):
	<instruções>
 	return "valor do retorno"

def mensagem1():
	print("Hello World1")

def mensagem2():
 	return 'Hello World2'

mensagem1()
print(mensagem2())

print()

def ler_notas():
    n=float(input('Digite uma nota para o aluno(a): '))
    return n
    
def resultado(n1,n2):
    print('Nota 1: ',n1)
    print('Nota 2: ',n2)
    media=(n1+n2)/2
    print('Média: ',media,'\nResultado: ',end="")
    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")
        
a = ler_notas()
b = ler_notas()
resultado(a,b)

Xº Aula - 13/08/2024 ###########################################################################################################

LISTA

primeiro = [1,2,3,4]
print(len(primeiro))
print(primeiro[0])
print(primeiro[2:4])

lista = [1,2,3]
inteiro = 1
real = 1.4
string = "luiz"
booleano = True
print(type(lista))
print(type(inteiro))
print(type(real))
print(type(string))
print(type(booleano))

Concatenação

print(primeiro+[5,6])

end=" " (Quebra de Linha)
for n in [1,2,3,4]:
	print (n,end="")

lista = [1,2,3]
print(3 in lista)
print(0 in lista)

lista[<uma expressão do tipo inteiro>]
lista[<início>:<fim>]
lista + outra_lista
print(lista)
len(lista)
list(intervalo(<superior>))
==,!=,<,>,<=,>=
for <variável> in lista: <instrução>
<qualquer valor> in lista

MÉTODOS
LEGENDA = (x = indice,y = valor)

.append(y) : adicionar no final da lista
.insert(x,y) : idiciona em local especifico
.pop(x) : remove em local especifico
.sum() : soma todos os valores da lista

Yº Aula - 19/08/2024 ###########################################################################################################

Função open()
	arquivo = open('arquivo.txt','w') = abre o arquivo ou cria caso não o encontre
