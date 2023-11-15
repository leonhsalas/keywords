

def cargakeywords():
    with open("keywords.txt") as f:
        for linea in f:
            keywords = linea
        print("Menu de la aplicación Kwranking")
        print("[1] –- Importar palabras clave")
        print("[2] – Mostrar palabras clave")
        print("[0] – Salir")
        numero = int(input("¿Qué opción desea elegir? "))

        while numero != 0:
            if numero == 1:
                cargakeywords()
            elif numero == 2:
                print(keywords)
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

print("Menu de la aplicación Kwranking")
print("[1] – Importar palabras clave")
print("[2] – Mostrar palabras clave")
print("[0] – Salir")

numero = int(input("¿Qué opción desea elegir? "))

while numero != 0:
    if numero == 1:
        cargakeywords()
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