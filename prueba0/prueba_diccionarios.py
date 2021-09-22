def calcular_color (lista_de_colores) : 
    if len (lista_de_colores) == 1 : 
        return lista_de_colores [0] 
    if len (lista_de_colores) == 2 : 
        if lista_de_colores[0] == "rojo" and lista_de_colores[1] == "amarillo":
            return "naranja"
        if lista_de_colores[0] == "rojo" and lista_de_colores[1] == "azul":
            return "violeta"
        if lista_de_colores[0] == "azul" and lista_de_colores[1] == "amarillo":
            return "verde"

colores_prim = ("rojo","amarillo","azul")

print (colores_prim)
for color in colores_prim: 
    lista_de_colores = [color]
    print (calcular_color(lista_de_colores))

for color_a in colores_prim : 
    for color_b in colores_prim : 
        lista_colores = [color_a, color_b]
        color_final = calcular_color(lista_colores)
        print (lista_colores) 
        print (color_final) 

