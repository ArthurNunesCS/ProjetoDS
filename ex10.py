n1 = float(input("digite sua primeira nota: "))
n2 = float(input("digite sua segunda nota: "))
n3 = float(input("digite sua terceira nota: "))

media = (n1+n2+n3)/3

conceito = ""

if media >= 8:
    conceito = "A"
elif media >=5 and media <8:
    conceito = "B"
else:
    conceito = "C"
    
print(f"sua media é {media} e seu conceito é {conceito}")