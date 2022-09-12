from random import randint

cond = "N"
while cond == "N":
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))

    soma = num1 + num2

    print("Soma de", num1, "+", num2, "é igual: ",soma)
    print("Seu ID é: ", randint(0,10000000))
    
    cond = str(input("Deseja sair? S/N: ")).upper()
print("Você acabou de sair! ")
