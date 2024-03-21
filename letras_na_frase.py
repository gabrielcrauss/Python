#########################################
# Verificar qual a letra que aparece mais
import os
os.system('cls')

frase = "Este é um exemplo de verificação de qual letra aparace mais vezes na frase"

frase = frase.upper()

letra_vencedora = ''
maior_quantidade = 0

count = 0

while count < len(frase):
    letra = frase[count]
    
    if letra == ' ':
        count += 1
        continue

    quantidade = 0
    i = 0

    while i < len(frase):
        if letra == frase[i]:
            quantidade += 1
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            letra_vencedora = letra
        i += 1
    count += 1
print(frase)
print()
print(f'A letra \'{letra_vencedora}\' teve a maior número de ocorrências com {maior_quantidade} X')    
print()


