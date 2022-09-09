diaria = int(input("dias alugados: "))
km = float(input("Quilometros rodados: "))
pagar = (diaria * 60) + (km * 0.15)
print("Total a pagar é: R$ {} ".format(pagar))
