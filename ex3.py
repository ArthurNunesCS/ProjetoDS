idvendedor = int(input("digite o id do vendedor "))
codpeca = int(input("digite o código da peça "))
precounit = float(input("digite o preco unitario "))
qtdvendida = int(input("digite a qtd vendida "))

totvenda = precounit * qtdvendida

com = totvenda * 0.05

print (f'O vendedor {idvendedor} vendeu {qtdvendida} unidade(s) da peça {codpeca} o seu preço unitário é {precounit} a comissão é {com}')
