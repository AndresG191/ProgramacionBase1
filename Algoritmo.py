#Analizador lexico
cadena = "9.E"
#Validamos a 0 i
i = 0

es_Valido = True

while i < len(cadena):
    # Paso 1: Verificar signo inicial opcional
    if i == 0 and (cadena[i] == "+" or cadena[i] == "-"):
        i += 1

    # Paso 2: Debe haber al menos un dígito antes del punto o E
    if i < len(cadena) and cadena[i].isdigit():
        while i < len(cadena) and cadena[i].isdigit():
            i += 1
    else:
        es_Valido = False
        break

    # Paso 3: Punto decimal opcional seguido de dígitos
    if i < len(cadena) and cadena[i] == ".":
        i += 1
        if i < len(cadena) and cadena[i].isdigit():
            while i < len(cadena) and cadena[i].isdigit():
                i += 1
        else:
            es_Valido = False
            break

    # Paso 4: Exponente opcional (E o e)
    if i < len(cadena) and (cadena[i] == "E" or cadena[i] == "e"):
        i += 1
        # Signo opcional después de E
        if i < len(cadena) and (cadena[i] == "+" or cadena[i] == "-"):
            i += 1
        # Deben seguir dígitos después de E o el signo
        if i < len(cadena) and cadena[i].isdigit():
            while i < len(cadena) and cadena[i].isdigit():
                i += 1
        else:
            es_Valido = False
            break

    # Si quedan caracteres después de procesar, no es válido
    if i < len(cadena):
        es_Valido = False
        break

print("Es una cadena válida" if es_Valido else "No es una cadena válida")