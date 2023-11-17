
lista = [] 
def cargakeywords(contador):
    with open("keywords.txt") as f:
        for linea in f:
            keywords = linea
            lista.append(keywords)
        print("Menu de la aplicación Kwranking")
        print("[1] –- Importar palabras clave")
        print("[2] – Mostrar palabras clave")
        print("[0] – Salir")
        numero = int(input("¿Qué opción desea elegir? "))

        while numero != 0:
            if numero == 1:
                cargakeywords(0)
            elif numero == 2:
                print(lista)
            elif numero == 0:
                finalizar()
                break
            else:
                print("Opción incorrecta")
            print("Menu de la aplicación Kwranking")
            print("[1] – Importar palabras clave")
            print("[2] – Mostrar palabras clave")
            print("[0] – Salir")
            numero = int(input("¿Qué opción desea elegir? "))
        finalizar()
    
def finalizar():
    print("Projecto Terminado")
ton = "0"
if ton == "1":
    pass
else:
    print("Menu de la aplicación Kwranking")
    print("[1] – Importar palabras clave")
    print("[2] – Mostrar palabras clave")
    print("[0] – Salir")

    numero = int(input("¿Qué opción desea elegir? "))

    while numero != 0:
        if numero == 1:
            cargakeywords(0)
        elif numero == 2:
            print("Error: keywords does not exist")
            break
        elif numero == 0:
            finalizar()
            break
        else:
            print("Opción incorrecta")
        print("Menu de la aplicación Kwranking")
        print("[1] – Importar palabras clave")
        print("[2] – Mostrar palabras clave")
        print("[0] – Salir")
        numero = int(input("¿Qué opción desea elegir? "))


finalizar()