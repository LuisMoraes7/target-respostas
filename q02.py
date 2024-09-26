def identifyFibonacci(n):
    valor1 = 5 * (n * n) + 4
    valor2 = 5 * (n * n) - 4
    resultado1 = (valor1 ** 0.5).is_integer()
    resultado2 = (valor2 ** 0.5).is_integer()
    if resultado1 == True or resultado2 == True:
        return True
    else:
        return False

p = 1
while (p == 1):
    n = int(input("Digite o número que deseja descobrir se está ou não na sequência de Fibonacci: "))
    resultado = identifyFibonacci(n)
    if resultado:
        print(f'{n} está na sequência de Fibonacci!')
        p = int(input(('Deseja continuar? [1 para sim e qualquer outra coisa para não] ')))
    else:
        print(f'{n} não está na sequência de Fibonacci!')
        p = int(input(('Deseja continuar? [1 para sim e qualquer outra coisa para não] ')))