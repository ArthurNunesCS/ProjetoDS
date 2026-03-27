p = float(input("digite seu peso em kg: "))
a = float(input("digite sua altura em m: "))

imc = p/a**2

classi = ""
if imc < 18.5:
    classi = "abaixo do peso normal"
elif imc >= 18.5 and imc <= 24.9:
    classi = "peso normal" 
elif imc >= 25 and imc <= 29.9:
    classi = "excesso de peso"
elif imc >= 30 and imc <= 34.9:
    classi =  "obesidade classe 1"
elif imc >= 35 and imc <=39.9:
    classi = "obesidade classe 2"
else:
    classi = "obesidade clsse 3"


print (f"seu imc é {imc:.2f} e você esta na classificação: {classi}")