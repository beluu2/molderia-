def load_currency_code_lines(nombre_archivo) :
    archivo_codigo = open(nombre_archivo, "r", encoding="utf8")
    
    ## ejemplo 1
    #contenido = archivo_codigo.readlines() #
    #print (contenido) 
    #return contenido

    # ejemplo 2
    #print (archivo_codigo.read()) 
    return archivo_codigo.read()


def load_currency_code(nombre_archivo) :
    archivo_codigo = open(nombre_archivo, "r", encoding="utf8")
    lineas = archivo_codigo.readlines() #

    codigos = []
    for linea in lineas : 
        columnas = linea.split("\t")
        print(columnas[0])
    return codigos



a = 0
codigos = load_currency_code("currency_code.txt")


#for codigo in codigos: 
#    print (codigo) 

    

