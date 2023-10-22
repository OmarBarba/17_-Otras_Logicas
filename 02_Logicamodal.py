#logica modal
print("logica modal")
# Definimos un mundo posible
mundo_posible = {
    "llueve": True,
    "sol": False
}

# Expresamos una afirmación modal usando "◻"
afirmacion_modal = "◻llueve"

# Evaluamos la necesidad
if afirmacion_modal[1:] in mundo_posible and mundo_posible[afirmacion_modal[1:]]:
    resultado = "La afirmación es necesaria en este mundo posible."
else:
    resultado = "La afirmación no es necesaria en este mundo posible."

# Mostramos el resultado
print(resultado)
