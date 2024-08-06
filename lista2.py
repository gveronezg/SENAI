# Lista 2.1. Verifique se 2 é maior que 1
print(f'Verifique se 2 é maior que 1: {2>1}')

# Lista 2.2. Teste se 5 é menor que 10.
print(f'Teste se 5 é menor que 10: {5<10}')

# Lista 2.3. Verifique se 'a' é igual a 'a'. 4. Teste se 3 é igual a 3 ou 4.
print(f"Verifique se 'a' é igual a 'a': {'a'=='a'}")

# Lista 2.4. Teste se 3 é igual a 3 ou 4.
print(f'Teste se 3 é igual a 3 ou 4: {3==(3 or 4)}')

# Lista 2.5. Verifique se 8 é maior que 5 e menor que 10.
print(f'Verifique se 8 é maior que 5 e menor que 10: {5<8<10}')

# Lista 2.6. Teste se 0 é igual a 0 ou diferente de 1.
print(f'Teste se 0 é igual a 0 ou diferente de 1: {0==0 or 0!=1}')

# Lista 2.7. Verifique se 9 é menor que 10 ou maior que 20.
print(f'Verifique se 9 é menor que 10 ou maior que 20: {10>9 or 9>20}')

# Lista 2.8. Teste se 'x' não é igual a 'y'.
print(f'Teste se "x" não é igual a "y": {not"x"=="y"}')

# Lista 2.9. Verifique se 1 é menor que 2 e 3 é maior que 2.
print(f'Verifique se 1 é menor que 2 e 3 é maior que 2: {1<2 and 3>2}')

# Lista 2.10. Teste se 'gato' é igual a 'gato' ou 'cachorro'.
print(f'Teste se "gato" é igual a "gato" ou "cachorro": {"gato"==("gato"or"cachorro")}')

# Lista 2.11. Teste se 10 é maior que 5 ou menor que 15.
print(f'Teste se 10 é maior que 5 ou menor que 15: {10>5 or 15>10}')

# Lista 2.12. Verifique se 2 mais 2 é igual a 4.
print(f'Verifique se 2 mais 2 é igual a 4: {2+2 == 4}')

# Lista 2.13. Teste se 7 é menor que 8 e maior que 6.
print(f'Teste se 7 é menor que 8 e maior que 6: {7<8 and 7>6}')

# Lista 2.14. Teste se 15 é maior que 10 ou menor que 5.
print(f'Teste se 15 é maior que 10 ou menor que 5: {15>10 or 15<5}')

# Lista 2.15. Verifique se 100 é igual a 100 ou 50.
print(f'Verifique se 100 é igual a 100 ou 50: {100 == 100 or 100 == 50}')

# Peça ao usuario para digitar um numero e imprima o dobro deste numero
# comando para entrada de dados
n = int(input("Digite um numero para dobrar: "))
# comando para saida de dados, informa a variavel digitada e seu dobro
print("O dobro de {} é: {}".format(n,(n*2)))

# Solicite duas strings do usuario e imprima a concatenação delas
txt1 = str(input("Entre com a string inicial: "))
txt2 = str(input("Agora entre com a string final: "))
print("Concatenando...")
print(txt1+" "+txt2)
