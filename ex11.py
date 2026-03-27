i = 0 

while i <= 3:
    s = int(input("digite a senha: "))
    i+=1
    if s == 1234:
        print ("aceesso permitido")
        break
    elif i == 3:
        print ("acesso bloqueado ")
        break