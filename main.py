import random

contador = 1
num = -1
acertoNum = 0
acertoStar = 0
listRdNumbers = []
listRdStars = []
listNumbers = []
listStars = []

print("Euromilhões...")

for i in range(0, 5):
    rdnum = random.randint(1, 50)
    num = int(input(f"Digite o número {contador} (de 1 a 50): \n"))
    while num < 1 or num > 50 or num in listNumbers:
        num = int(input(f"Digite o número {contador} (de 1 a 50): \n"))
    listNumbers.append(num)
    while rdnum in listRdNumbers:
        rdnum = random.randint(1, 50)
    listRdNumbers.append(rdnum)
    contador += 1
    i += 1
    listNumbers.sort()
    listRdNumbers.sort()
#print(listRdNumbers)

for x in listNumbers:
    for y in listRdNumbers:
        if x == y:
            acertoNum += 1

contador = 1
num = -1

for i in range(0, 2):
    rdstar = random.randint(1, 12)
    num = int(input(f"Digite a estrela {contador} (de 1 a 12): \n"))
    while num < 1 or num > 12 or num in listStars:
        num = int(input(f"Digite a estrela {contador} (de 1 a 12): \n"))
    listStars.append(num)
    while rdstar in listRdStars:
        rdstar = random.randint(1, 12)
    listRdStars.append(rdstar)
    contador += 1
    i += 1
    listStars.sort()
    listRdStars.sort()

for x in listStars:
    for y in listRdStars:
        if x == y:
            acertoStar += 1

print(f"Números apostados: {listNumbers}")
print(f"Estrelas apostadas: {listStars}")
print(f"Chave: {listRdNumbers}")
print(f"Estrelas: {listRdStars}")
print(f"Acertou {acertoNum} números e {acertoStar} estrelas!")

