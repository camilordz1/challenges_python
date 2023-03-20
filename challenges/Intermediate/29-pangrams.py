# Roy quiere mejorar su velocidad de escritura en máquina para concursos de programación. 
# Su amigo le dijo que escribiera la oración "The quick brown fox jumps over the lazy dog" 
# repetidamente porque es un pangrama. (pangramas son oraciones construidas usando todas 
#                                       las letras del alfabeto, por lo menos una vez.)

# Después de escribir la oración muchas veces, Roy se aburrió. Entonces comenzó a buscar 
# otros pangramas.

# Dada una oración "s", dile a Roy si es un pangrama o no.

# Formato de Entrada

# La Entrada consiste en una linea que contiene "s".

# Restricciones
# La longitud de "s" puede ser a lo mucho 10**3  y puede contener espacios, minúsculas y mayúsculas. 
# Las minúsculas y mayúsculas de una misma letra son consideradas la misma letra.

# Formato de Salida

# Imprime una línea "pangram" si "s" es un pangrama, sino imprime "not pangram".

# Ejemplo de Entrada #1

# We promptly judged antique ivory buckles for the next prize    

# Ejemplo de Salida #1

# pangram

# Ejemplo de Entrada #2

# We promptly judged antique ivory buckles for the prize    

# Ejemplo de Salida #2

# not pangram

# Explicación

# En el primer caso de prueba, la respuesta es un pangram porque la oración contiene 
# todas las letras.

def pangrams(s):
    dic = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,
           "n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,
           "y":24,"z":25}
    s = s.lower().replace(" ","") 
    verification = [0]*len(dic)

    for letter in s:
        verification[dic[letter]] += 1 

    print(verification)

pangrams("We promptly judged antique ivory buckles for the next prize")        