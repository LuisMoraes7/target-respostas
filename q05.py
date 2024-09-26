while True:
        palavra = input('Digite uma palavra: ')    
        valido = True
        for letra in palavra:
            if not ('a' <= letra <= 'z' or 'A' <= letra <= 'Z'):
                valido = False
                break
        if valido:
            lista = []
            for letra in palavra:
                lista.append(letra)
            tamanho = len(lista) + 1 
            print('Palavra invertida: ', end='')
            for c in range(-1, -tamanho, -1):
                print(lista[c], end='')
            break
        else:
            print('O que você digitou não é uma palavra. Tente novamente!')


