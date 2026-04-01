valor = float(input("Digite o valor do carro: "))
imposto = valor * 0.45
valorimposto = valor + imposto 
lucro = valorimposto * 0.12
valorconsumidor = valorimposto + lucro
print(f'O valor do carro liquido é {valorconsumidor} reais, o valor do carro bruto é {valor} reais, o valor do imposto é {imposto}, e o lucro do distribuidor é de {lucro}')
