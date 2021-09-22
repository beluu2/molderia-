def llenar_diccionario(diccionario_vacio_o_no):
    resultado = dict(diccionario_vacio_o_no)
    resultado["valor_1"] = 0
    resultado["nombre"] = "juan"
    resultado["cantidad"] = 10
    return resultado

def llenar_diccionario_por_keys(diccionario_vacio_o_no):
    resultado = {}
    for key in diccionario_vacio_o_no:
        resultado[key] = diccionario_vacio_o_no[key]

    resultado["valor_1"] = 0
    resultado["nombre"] = "juan"
    resultado["cantidad"] = 10
    return resultado


diccionario_vacio = {"0":2, "a":3, "b":20, "c":223, "0":2, }

diccionario_lleno = llenar_diccionario(diccionario_vacio)
diccionario_lleno_2 = llenar_diccionario_por_keys(diccionario_vacio)

print("Diccionario vacio: " + str(diccionario_vacio))
print("Diccionario lleno: " + str(diccionario_lleno))
