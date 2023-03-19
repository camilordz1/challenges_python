# Camel Case es un estilo de nomenclatura común en muchos lenguajes de programación. 
# En Java, los nombres de métodos y variables normalmente comienzan con una letra minúscula, 
# y todas las palabras posteriores comienzan con una letra mayúscula (ejemplo: startThread). 
# Los nombres de las clases siguen el mismo patrón, excepto que comienzan con una letra 
# mayúscula (ejemplo: BlueCar).

# Su tarea es escribir un programa que cree o divida nombres de clases, métodos y variables 
# de Camel Case.

# Formato de entrada

# Cada línea del archivo de entrada comenzará con una operación (S o C) seguida de un punto 
# y coma seguido de M, C o V seguido de un punto y coma seguido de las palabras en las que 
# deberá operar.
# La operación será S (dividir) o C (combinar)
# M indica método, C indica clase y V indica variable
# En el caso de una operación de división, las palabras serán un método camel case, una clase 
# o un nombre de variable que debe dividir en una lista de palabras delimitadas por espacios 
# que comienzan con una letra minúscula.
# En el caso de una operación de combinación, las palabras serán una lista delimitada por 
# espacios de palabras que comienzan con letras minúsculas que debe combinar en la cadena de 
# caracteres de camello adecuada. Los métodos deben terminar con un conjunto vacío de paréntesis 
# para diferenciarlos de los nombres de las variables.

# Formato de salida

# Para cada línea de entrada, su programa debe imprimir la lista de palabras delimitadas por 
# espacios (en el caso de una operación de división) o la cadena de mayúsculas y minúsculas 
# apropiada (en el caso de una operación de combinación).


import sys

def camel_case(args):
    
    op,tp,name = str(args).split(";")

    if op == "C":
        return join(tp,name).replace("\n","")+"\n"

    if op == "S":
        return divide(name).replace("\n","")+"\n"   


def divide(name):
    name = list(name)
    pos = [pos for pos, letter in enumerate(name) if letter.isupper()]
    pos.sort(reverse=True)

    for index in pos:
        if index != 0:
            name.insert(index," ")
    return "".join(name).replace("()","").lower()        
        

def join(tp,name):
    
    name = name.split(" ")
    
    par=True
    if tp == "V":
        par = False
        
    if len(name) == 1 and (tp == "M" or tp == "V"):
        return f"{name[0]}{'()'*par}"
    
    if len(name) == 1 and tp == "V":
        return f"{name[0].title()}{'()'*par}"

    if tp == "M" or tp == "V":                   
        result = [word.title() for word in name] 
        result[0] = name[0]
        return f'{"".join(result)}{"()"*par}'
    
    return "".join([word.title() for word in name])

if __name__ == "__main__":
    
    lines = sys.stdin.readlines()
    
    for line in lines:
        camel_case(line)

    print(">>> ",camel_case("C;M;mouse pad"))
    print(">>> ",camel_case("S;C;LargeSoftwareBook"))
    print(">>> ",camel_case("C;V;mobile phone"))
