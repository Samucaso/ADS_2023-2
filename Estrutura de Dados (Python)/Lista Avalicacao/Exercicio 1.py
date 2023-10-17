# 1) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Em seguida, calcule a média anual das temperaturas
# e mostre a média calculada juntamente com todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )


temp_media = [27, 27, 26, 25, 23, 22, 22, 22, 23, 24, 25, 26]
temp_acima = []

media = sum(temp_media) / len(temp_media)

for i in temp_media:
    if i > media:
        temp_acima.append(i)
    else:
        continue

print(f"Média calculada: {media:.1f}")

print(f"Temperaturas acima da média anual:\nJaneiro - {temp_acima[0]}\nFevereiro - {temp_acima[1]}\n"
      f"Março - {temp_acima[2]}\nAbril - {temp_acima[3]}\nNovembro - {temp_acima[4]}\nDezembro - {temp_acima[5]}")
