def cargakeywords():
    with open("keywords.txt") as f:
        for linea in f:
            keywords = linea
            print(keywords)
def finalizar():
    print("Project ended")


numero = int(input("Cual es el numero "))

while numero != 0:
    if numero == 1:
        cargakeywords()
    elif numero == 0:
        finalizar()
        break
    else:
        print("pon 1. 2 o 0")
    numero = int(input("Cual es el numero "))

finalizar()