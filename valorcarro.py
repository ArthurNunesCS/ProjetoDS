valor = float(input("Digite o valor do carro: "))
valorimposto = valor + valor * 0.45
imposto = valorimposto - valor
valorconsumidor = valorimposto + valorimposto * 0.12
lucro = valorconsumidor - valor
print(f'O valor do carro é {valorconsumidor} reais, o valor do imposto é {imposto}, e o lucro do distribuidor é de {lucro}')