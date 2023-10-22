def aplicar_operacion(operacion, numeros):
    return [operacion(x) for x in numeros]

cuadrado = lambda x: x * x
numeros = [1, 2, 3, 4, 5]

resultados = aplicar_operacion(cuadrado, numeros)
print(resultados)  # Devuelve [1, 4, 9, 16, 25]
