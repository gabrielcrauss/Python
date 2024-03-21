import os
os.system('cls')

lista = []

print('#' * 30)
print('# Lista de Compras'.upper()) 
print('# 1 para exibir a lista') 
print('# 2 para inserir na lista') 
print('# 3 para remover um elemento') 
print('# 4 para limpar a lista') 
print('# 5 Sair') 
print()

while True:
    
    print()
    opcao = input('Digite a opção desejada: ')

    try:
        opcao = int(opcao)
    except ValueError:
        print("Opção inválida.")
        print()
        continue  

    if opcao > 5:
        print('Opção inválida')
        print()
        continue

    if opcao == 1:
        if len(lista) == 0:
            print('Lista Vazia')
        for item in enumerate(lista):
            indice, nome = item
            print(indice, nome)
        #print(lista)
    
    if opcao == 2:
        item = input('Digite o novo item: ')
        lista.append(item)
        print(item, 'adicionad@ na lista!')
        print()
        print("Lista: ", lista)

    if(opcao == 3):
        remover = input('Digite o item a ser removido: ')
        if remover in lista:
            lista.remove(remover)
            print(remover, 'removida da lista!')
            print("Lista: ", lista)
        else:
            try:
                remover = int(remover)
            except ValueError:
                print(remover , 'não encontrad@')
                print()
                continue 
            if remover > len(lista) or remover < 0:
                print('indice não encontrado')
                print()
                continue 
            else: 
                del lista[remover]
            print("Lista: ", lista)
    
    if opcao == 4:
        if len(lista) == 0:
            print('A lista já está vazia')
        else:
            lista.clear()
            print('Lista esvaziada!')

    if opcao == 5:
        print('Tchau!')
        break
