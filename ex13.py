nome = ""
idade = 0
i = 0
mdezoito = 0

while nome != "encerrar":
    nome = input("digite seu nome: ")
    if nome == "encerrar":
        break
    idade = int(input("digite sua idade: "))
    if idade >= 18:
        mdezoito += 1
    i += 1
    
    
print(f"{i} usuário(s) foram cadastrados e {mdezoito} são maiores de idade")
