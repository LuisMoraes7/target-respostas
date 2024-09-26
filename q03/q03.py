#  3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#  • O menor valor de faturamento ocorrido em um dia do mês;
#  • O maior valor de faturamento ocorrido em um dia do mês;
#  • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# faturamento_janeiro = []
# from random import randint
# for c in range(0, 30, 1):
#     faturamento_janeiro.append(randint(70, 200))

# c = 0
# with open('q03/faturamento/fevereiro.json', 'w') as file:
#     file.write('[')
#     for i in faturamento_janeiro:
#         c += 1
#         file.write('{' + f'"{c}": {str(i)}' + '}' + ', \n')
#     file.write(']')


import json

with open('q03/faturamento/janeiro.json', 'r') as arquivo:
    faturamento_janeiro = json.load(arquivo)

print(f'Faturamento em 30 dias de janeiro: {faturamento_janeiro}')
soma = 0
for numero in faturamento_janeiro:
    soma += numero

mediafaturamento = soma/len(faturamento_janeiro)


menor_valor = min(faturamento_janeiro)
maior_valor = max(faturamento_janeiro)

acima_media = []
for index, numero in enumerate(faturamento_janeiro):
    if numero >= mediafaturamento:
        acima_media.append({'dia': (index + 1), 'faturamento': numero})

quantidade_dias = 0
for dia in acima_media:
    days = dia.get('dia')
    if days:
        quantidade_dias += 1



print('Analisamos o faturamento de um mês. Descobrimos que: ')
print(f'O maior valor é {maior_valor}')
print(f'O menor valor foi {menor_valor}')
print(f'A média dos faturamentos foi {mediafaturamento}')
print(f'Foram {quantidade_dias} dias do mês que o valor do faturamento superou a média mensal.')
for dados in acima_media:
    print(f'Dia: {dados.get('dia')} de janeiro, Faturamento: {dados.get('faturamento')}')

