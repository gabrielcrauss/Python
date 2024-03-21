import os
os.system('cls')

# Cálculo do 1º dígito do CPF
# Multiplica o primeiro dígito do CPF por 10, o segundo por 9 e assim por diante
# até o 9º dígito do CPF
# Exemplo
# 021.039.520-65
# 0*10 + 2*9 + 1*8 + 0*7 + 3*6 + 9*5 + 5*4 + 2*3 + 0*2
# Depois somar os resultados
# Com o resultodo somado de todos, deve multiplicar por 10
# Com isso, faça o resto da divisão por 11
# se o resultado for maior que 9 retornar 0
# Este será o 1º dígito verificador

# O segundo dígito verificador é tudo igual, 
# porém deve pegar o 1º dígito verificar e colocar como 10º número
# e a multiplicação deve começar com 11 ao invéz de 10

def valida_cpf(cpf):
    
    cpf = cpf.replace(".", "").replace(",", "").replace("-", "")
   
    if len(cpf) != 11:
        return False
    
    if not cpf.isdigit():
        return False
    
    if cpf == cpf[::-1]: # Verifica se todos os número são iguais. A função inverte a string
        return False     
    
    cpf_lista = cpf[0:9]        #Pega os 9 primeiros dígitos da string
    cpf_lista = list(cpf_lista) # Transforma em uma lista todos os dígitos

    ########################################
    # 1º Dígito verificador
    multiplicacao = 10
    soma_total = 0

    for numero in cpf_lista:
        soma_total += (int(numero) * multiplicacao)
        multiplicacao -= 1

    total_soma_multiplicacao = soma_total * 10
    resto_divisao = total_soma_multiplicacao % 11
    primeiro_digito_verificador = resto_divisao if resto_divisao <= 9 else 0

    ########################################
    # 2º Dígito verificador
    #

    cpf_lista.append(primeiro_digito_verificador)

    multiplicacao = 11
    soma_total = 0

    for numero in cpf_lista:
        soma_total += (int(numero) * multiplicacao)
        multiplicacao -= 1

    total_soma_multiplicacao = soma_total * 10
    resto_divisao = total_soma_multiplicacao % 11
    segundo_digito_verificador = resto_divisao if resto_divisao <= 9 else 0

    ########################################
    # Verifica se os dígitos verificadores conferem com o cpf original
    #

    if segundo_digito_verificador == int(cpf[-1]) and primeiro_digito_verificador == int(cpf[-2]):
        return True
    else:
        return False



#########################################
#   Cria CPF válido 
    
import random    
count = 0

def gera_cpf_valido():
    cpf_criado = ''
    for i in range(11):
        cpf_criado += str(random.randint(0,9))
    return cpf_criado

count = 0
while True:
    teste_cpf = gera_cpf_valido()
    if valida_cpf(teste_cpf):
        print()
        print('Gerou um CPF válido:', teste_cpf , 'em' , count, 'tentativas')
        print()
        break
    count += 1
