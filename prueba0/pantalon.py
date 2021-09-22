def pantalon_rectangulo_base(medidas):
    result = {}
    result["AB"] = medidas["cadera"] / 4 + 4
    result["AC"] = medidas["largo_pantalon"]
    result["BF"] = medidas["alto_cadera"]
    result["AG"] = medidas["tiro_delantero"]
    result["AI"] = medidas["alto_rodilla"]
    return result

def pantalon_molde_base(medidas_cuerpo, medidas_rectangulo_base):
    result = {}
    result["MLL"] = medidas_cuerpo["cintura"] / 4
    result["MB"] = result["MLL"] + 2.5
    result["MA"] = medidas_rectangulo_base["AB"] - result["MB"]
    return result

lista_medidas = [{"largo_pantalon" : 106 , "alto_rodilla" : 56 , "cintura" : 98,  "cadera" :114, "alto_cadera" : 20 , "tiro_delantero" :28}  
, {"largo_pantalon" : 106 , "alto_rodilla" : 56 , "cintura" : 109,  "cadera" :125 , "alto_cadera" : 20 , "tiro_delantero" :28}  
, {"largo_pantalon" : 106 , "alto_rodilla" : 56 , "cintura" : 109,  "cadera" :125 , "alto_cadera" : 20 , "tiro_delantero" :28}  
, {"largo_pantalon" : 106 , "alto_rodilla" : 56 , "cintura" : 109,  "cadera" :125 , "alto_cadera" : 20 , "tiro_delantero" :28}  
, {"largo_pantalon" : 106 , "alto_rodilla" : 56 , "cintura" : 109,  "cadera" :125 , "alto_cadera" : 20 , "tiro_delantero" :28}  
, {"largo_pantalon" : 106 , "alto_rodilla" : 56 , "cintura" : 109,  "cadera" :125 , "alto_cadera" : 20 , "tiro_delantero" :28}  
, {"largo_pantalon" : 106 , "alto_rodilla" : 56 , "cintura" : 109,  "cadera" :125 , "alto_cadera" : 20 , "tiro_delantero" :28}  
]

for medidas_cuerpo in lista_medidas:
    rectangulo_base = pantalon_rectangulo_base(medidas_cuerpo)
    print("Rectangulo base: " + str(rectangulo_base))
    print("")
    molde_base = pantalon_molde_base(medidas_cuerpo, rectangulo_base)
    print("Molde base: " + str(molde_base))
    print("")
