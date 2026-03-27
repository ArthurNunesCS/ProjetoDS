i = 0
n = 0
soma = 0.0
maior = 0
menor = 10
while n != -1:
    n = float(input("digite suas notas: "))
    if n <= 10:
        if n == -1:
            print(f"\na media é {soma / i :.2f} e a maior nota é {maior} e o menor é {menor}")
            break
        soma += n
        i+=1
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
    else:
        print('\n Erro: nota maior que 10')
        break