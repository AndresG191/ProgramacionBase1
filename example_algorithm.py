# Analizador léxico: +629.3E8

cadena = "+629.3E8"
# Inicializar i a cero
i = 0
es_Valido = True

# Recorrer cadena mientras aún no termina
while i < len(cadena):
    if cadena[i] == "+" or cadena[i] == "-":
        # Si el símbolo en la posición "i" es "+" o "-"
        i += 1
    elif cadena[i].isdigit():
        # Si el símbolo en la posición "i" es un dígito
        while i < len(cadena) and cadena[i].isdigit():
            # Mientras el símbolo en "i" sea un dígito
            i += 1
    else:
        # Incrementar "i" para continuar recorriendo la cadena
        i += 1

print("Fin del análisis de la cadena.")
print("La cadena es válida" if es_Valido else "No es un número válido")
