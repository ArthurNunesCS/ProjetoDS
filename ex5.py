nome = input("Digite seu nome: ")
salario = float(input("Digite o seu salário: "))
if salario > 0 and salario <= 1000:
    reajuste = salario + salario * 0.20
elif salario > 1000 and salario <= 5000:
    reajuste = salario + salario * 0.10
elif salario > 5000:
    reajuste = salario + salario * 0.05
print(f'Nome: {nome} - Seu novo salário: R${reajuste:.2f}')
