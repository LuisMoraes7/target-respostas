# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

faturamento = [{'estado': 'SP', 'faturamento': 67836.43}, {'estado': 'RJ', 'faturamento': 36678.66}, {'estado': 'MG', 'faturamento': 29229.88}, {'estado': 'ES', 'faturamento': 27165.48}, {'estado': 'Outros', 'faturamento': 19849.53}]
soma = 0
for valor in faturamento:
    soma += valor.get('faturamento')

print(f'O valor total do faturamento foi {soma}!')
print('--------------')
for contribuicao in faturamento:
    percentual = ((contribuicao.get('faturamento'))/soma) * 100
    print(f'A contribuição de {contribuicao.get('estado')} foi de {round(percentual, 2)}%')
    print('-----------')