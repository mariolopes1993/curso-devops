teclado = str(input("Digite a frase: ")).upper().strip()
print("Letra A aparece {} vezes na frase.".format(teclado.count("A")))
print("Letra A está na posicao {}".format(teclado.find("A")+1))
print("outra letra A está na posicao {}".format(teclado.rfind("A")+1))