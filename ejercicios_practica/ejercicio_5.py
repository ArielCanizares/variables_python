# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados
print ("Tomaremos las 3 primeras letras de", palabra_1, "y las 2 primeras letras de", palabra_2)
parcial_1 = palabra_1[:3]
parcial_2 = palabra_2[:2]
print ("y la nueva palabra que se formará de esa conjunción será:", parcial_1 + parcial_2)