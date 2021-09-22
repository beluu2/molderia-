accesorios = ["cartera" , "billetera", "pulsera"]

b = 12
c = 23,5 
d =  {"accesorios" : accesorios , "b" : 12 , "c" : 23.5} 
for n in d : 
    print (n) 
    print (d[n])

for accesorios in d : 
     print (d[accesorios]) 

def mostrar_medidas(curva_de_talles):
    for talle in curva_de_talles : 
        print (talle) 
        datos_de_talle = (curva_de_talles[talle])
        #  print (datos_de_talle) 
        for nombre_de_medida in datos_de_talle : 
            print(f"{nombre_de_medida}: {datos_de_talle[nombre_de_medida]}")
            #print(nombre_de_medida + ": " + str(datos_de_talle[nombre_de_medida]))
            #print(": ".join([nombre_de_medida, str(datos_de_talle[nombre_de_medida])]))

talle_85 = {"cintura" : 68, "cadera" : 89 , "busto" : 85}
talle_90 = {"cintura" : 74, "cadera" : 94, "busto" : 90}
talle_95 = {"cintura" : 78, "cadera" : 97, "busto" : 95}

curva_de_talles_0 = {"talle 85" : talle_85, "talle 90" : talle_90,  "talle 95" : talle_95} 
curva_de_talles_1 = {"talle 85" : talle_95, "talle 90" : talle_85,  "talle 95" : talle_90} 
   
mostrar_medidas(curva_de_talles_0)
mostrar_medidas(curva_de_talles_1)
