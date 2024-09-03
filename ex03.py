#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json
caminho_arquivo = 'dados/dados1.json'

with open(caminho_arquivo, 'r') as arquivo:
    faturamento = json.load(arquivo)

valores = [item['valor'] for item in faturamento if item['valor'] > 0]

menor_valor = min(valores)
maior_valor = max(valores)

media_mensal = sum(valores) / len(valores)

acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {acima_da_media}")