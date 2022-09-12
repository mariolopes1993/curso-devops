preco = float(input("Qual preço do produto? "))

novopreco = preco - (preco * 5 / 100)

print("Novo preco com desconto de 5% vai ser: R$ {}".format(novopreco))
