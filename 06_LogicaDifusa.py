##############################################
###############Conjunto Difusos##############
#############################################
import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

# Crear el universo de discurso (rango de calificaciones)
calificaciones = np.arange(0, 101, 1)

# Crear el conjunto difuso "Bueno" con membresía triangular
calificacion_buena = fuzz.trimf(calificaciones, [70, 85, 100])

# Evaluar el grado de pertenencia de una calificación (ejemplo: 75)
pertenencia = fuzz.interp_membership(calificaciones, calificacion_buena, 75)

# Graficar el conjunto difuso
plt.figure()
plt.plot(calificaciones, calificacion_buena, 'b', linewidth=1.5, label='Bueno')
plt.fill_between(calificaciones, calificacion_buena, 0, alpha=0.2)
plt.plot([75, 75], [0, pertenencia], 'k', linewidth=1.5, label='Grado de pertenencia')
plt.title('Conjunto Difuso de Calificación')
plt.legend()
plt.show()

print(f'Grado de pertenencia de 75 en el conjunto "Bueno": {pertenencia:.2f}')

##################################################
##################Interferencia Difusa############
##################################################
import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as ctrl

# Crear antecedentes y consecuente difusos
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'comida')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de membresía
servicio.automf(3)
comida.automf(3)
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Crear reglas difusas
regla1 = ctrl.Rule(servicio['pobre'] | comida['mala'], propina['baja'])
regla2 = ctrl.Rule(comida['aceptable'], propina['media'])
regla3 = ctrl.Rule(servicio['excelente'] | comida['buena'], propina['alta'])

# Crear sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema_propina = ctrl.ControlSystemSimulation(sistema_control)

# Establecer valores de entrada
sistema_propina.input['servicio'] = 3.5  # Escala de 0-10
sistema_propina.input['comida'] = 8.0  # Escala de 0-10

# Realizar la inferencia
sistema_propina.compute()

# Obtener el valor de propina
print(f'Valor de propina: {sistema_propina.output["propina"]:.2f}')
