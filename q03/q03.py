import json

# Caso queria ver o de fevereiro, somente mudar a linha abaixo para 'fevereiro.json'

with open('q03/faturamento/janeiro.json', 'r') as arquivo:
    dadosjaneiro = json.load(arquivo)

faturamento_janeiro = list(dadosjaneiro)

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

