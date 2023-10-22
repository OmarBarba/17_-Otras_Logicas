def regla_si_es_cierto(condicion):
    if condicion:
        return "La regla es cierta."
    else:
        return "La regla no se cumple."

resultado = regla_si_es_cierto(True)
print(resultado)  # Devuelve "La regla es cierta."
