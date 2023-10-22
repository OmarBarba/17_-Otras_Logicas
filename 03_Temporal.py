
######################logica temporal 
print("logica temporal")
# Secuencia de eventos
secuencia_eventos = ["evento_A", "evento_B", "evento_C"]

# Expresamos una afirmación temporal usando "F"
afirmacion_temporal = "evento_A F evento_C"

# Evaluamos la afirmación temporal
if afirmacion_temporal in " ".join(secuencia_eventos):
    resultado = "La afirmación temporal se cumple en la secuencia de eventos."
else:
    resultado = "La afirmación temporal no se cumple en la secuencia de eventos."

# Mostramos el resultado
print(resultado)
