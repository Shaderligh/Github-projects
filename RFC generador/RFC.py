import random

prohibidas=["BACA", "BAKA", "BUEI", "BUEY", "CACA", "CACO", "CAGA", "CAGO", "CAKA", "CAKO", "COGE", "COGI", "COJA", "COJE","COJI", 
              "COJO", "COLA", "CULO", "FEDA", "FETO", "GUEI", "GUEY", "KACA", "KACO", "KAGA", "KAGO", "KOGE", "KOJO", "KULO", "LOCO",
              "LOKA", "LOKO", "MAME", "MAMO", "MEAR", "MEAS", "MEON", "MION", "MOCO", "MULA", "PEDA", "PEDO", "PENE", "PUTA", "PUTO", "QULO", "RATA", "RUIN"]

particulas=["DA", "DAS", "DE", "DEL", "DER", "DI", "DIE", "EL", "LA", "LAS", "LE", "LES", "LOS", "MAC", "MC", "VAN", "VON", "Y"]


def limpiar(texto):
    texto = texto.upper()
    texto = texto.replace("Á", "A")
    texto = texto.replace("É", "E")
    texto = texto.replace("Í", "I")
    texto = texto.replace("Ó", "O")
    texto = texto.replace("Ú", "U")
    texto = texto.replace("Ü", "U")
    texto = texto.replace("Ñ", "X")

    palabra= ""

    for letra in texto:
        if letra >= "A" and letra <= "Z":
            palabra = palabra + letra

    return palabra


def primera(apellido):
    palabras = apellido.upper().split()

    while len(palabras) > 1 and limpiar(palabras[0]) in particulas:
        palabras.pop(0)

    if len(palabras) == 0:
        return "X"

    return limpiar(palabras[0])


def letras_paterno(apellido):
    apellido = primera(apellido)

    if len(apellido) == 0:
        return "X"

    primera_letra = apellido[0]
    vocal = "X"

    for i in range(1, len(apellido)):
        if apellido[i] in "AEIOU":
            vocal = apellido[i]
            break

    return primera_letra + vocal


def letra_materno(apellido):
    apellido = primera(apellido)
    return apellido[0] if len(apellido) > 0 else "X"


def letra_nombre(nombres):
    palabras = nombres.upper().split()

    if len(palabras) == 0:
        return "X"

    if len(palabras) > 1:
        if palabras[0] == "JOSE" or palabras[0] == "MARIA":
            nombre = palabras[1]
        else:
            nombre = palabras[0]
    else:
        nombre = palabras[0]

    nombre = limpiar(nombre)

    if len(nombre) == 0:
        return "X"

    return nombre[0]


def calcular_rfc(paterno, materno, nombres, anio, mes, dia):
    letra1 = letras_paterno(paterno)
    letra2 = letra_materno(materno)
    letra3 = letra_nombre(nombres)

    fecha = str(anio % 100).zfill(2)
    fecha = fecha + str(mes).zfill(2)
    fecha = fecha + str(dia).zfill(2)

    rfc = letra1 + letra2 + letra3 + fecha

    if rfc[:4] in prohibidas:
        rfc = rfc[:3] + "X" + rfc[4:]

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for i in range(3):
        rfc = rfc + random.choice(letras)

    return rfc


paterno = input("Apellido paterno: ")
materno = input("Apellido materno: ")
nombres = input("Nombres: ")

anio = int(input("Año de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
dia = int(input("Día de nacimiento: "))

rfc = calcular_rfc(paterno, materno, nombres, anio, mes, dia)

print("Su RFC es:", rfc)