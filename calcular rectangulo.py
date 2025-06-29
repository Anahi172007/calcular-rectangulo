# Programa para calcular el área de un rectángulo
# Autor: [Anahi Leon]
# Fecha: [28/06/2025]
# Descripción:
# Este programa solicita al usuario la base y la altura de un rectángulo en centímetros.
# Luego calcula el área utilizando la fórmula: área = base × altura.
# Finalmente muestra el resultado en pantalla y valida si el área es mayor que cero.

# Solicita al usuario la base del rectángulo
base = float(input("Ingrese la base del rectángulo en centímetros: 9"))

# Solicita al usuario la altura del rectángulo
altura = float(input("Ingrese la altura del rectángulo en centímetros: 5"))

# Calcula el área
area = base * altura

# Verifica si el área es válida
es_valida = area > 0

# Muestra resultados
print("El área del rectángulo es:", area, "cm²")
print("¿El área calculada es válida?", es_valida)
