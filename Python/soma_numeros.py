cond = "N"
while cond == "N":
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))

    soma = num1 + num2

    print("Soma de", num1, "+", num2, "é igual: ",soma)
    
    cond = str(input("Deseja sair? S/N: ")).upper()
print("Você acabou de sair! ")
