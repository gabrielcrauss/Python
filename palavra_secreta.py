import os
os.system('cls')

palavra = "Cachorro".upper()

#print("Descubra a palavra secreta " + str(len(palavra)), end = '')
print("Descubra a palavra secreta ", end = '')
print('*'*len(palavra))
print()

tentativas = 0
letras_digitadas = ""

while True:
    letra_digitada = input("Digite uma letra: ").upper()
    if len(letra_digitada) > 1:
        print('Digite apenas UMA letra!')
        print()
        continue

    tentativas += 1
    
    if letra_digitada not in letras_digitadas:
        letras_digitadas += letra_digitada
    
    apresentacao = ''

    for i in palavra:
        acertou_letra = False
        
        for letra in letras_digitadas:
            #if i in palavra:
            #for k in palavra:
            if i == letra:
                apresentacao += letra
                #print("Acertou")
                acertou_letra = True
        if not acertou_letra:
            apresentacao += '*'
            #print('Errou')
            #print(f'A letra "{letra_digitada}" aparece  {palavra.count(letra_digitada.upper())} vezes') 
        #else:
        #    print("A palavra não possui essa letra")

    print(apresentacao)
    print()

    if '*' not in apresentacao:
        
        os.system('cls')
        print("#" * 35)
        print()
        print("Parabéns :)".upper())
        print()
        print("Completou em", tentativas, "tentativas")
        print()
        print("#" * 35)
        print()
        break

    

#for letra in palavra