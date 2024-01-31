import random
import sys

# Recebe a quantidade de cpfs que devem ser gerados e verifica se o número é valido, caso contrário, sai do programa
try:
    num = int(input("Quantos cpfs desejas gerar? "))
except ValueError:
    print("Valor inválido, por favor digite um número inteiro.")
    sys.exit()

# Gera n cpfs aleatórios e válidos

for _ in range(num):
    cpf_9_digitos = ''
    for i in range(9):
        cpf_9_digitos += str(random.randint(0, 9))
    #Faz os cálculos para gerar os dois últimos digitos e os acrescenta ao cpf
    def cpf(pre_cpf, contador_regressivo):
        soma_valores_digito = 0
        for numero_1 in pre_cpf:
            multiplicacao = int(numero_1) * contador_regressivo
            soma_valores_digito += multiplicacao
            contador_regressivo -= 1
        digito = (soma_valores_digito * 10) % 11
        digito = 0 if digito > 9 else digito
        cpf =  f'{pre_cpf}{str(digito)}'
        return cpf

    #chama a função cpf para gerar o primeiro digito
    cpf_10_digitos = cpf(cpf_9_digitos, 10)
    #chama a função cpf para gerar o segundo digito
    cpf_final = cpf(cpf_10_digitos, 11)
    print(cpf_final)
    
    
