qtdUsuarios= []
idadeUsuarios= []
maior = 0
while True:
    nome = input('Digite seu nome: ')
    qtdUsuarios.append(nome)

    idade = int(input('Digite sua idade: '))
    idadeUsuarios.append(idade)
    if idade > 18:
        maior += 1

    encerrar = input('Deseja encerrar? Se sim, digite encerrar: ')

    if encerrar == 'encerrar' or encerrar == 'Encerrar':
        print(f'\nA quantidade de usuarios é: {len(qtdUsuarios)} \n' +
              f'Possuem {maior} maiores de idades')
        break
