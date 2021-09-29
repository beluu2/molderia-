
def generar_stock (marcas,colores,talles) : 
    stock = []

    for marca in marcas : 
        for color in colores: 
            for x in talles: 
                producto = {"brand" : marca,"color": color, "talle": x}
                stock.append(producto)

    return stock
    








































lista_de_marcas_calzado     = ["adidas", "nike", "puma" , "fila", "dc"]
lista_de_marcas_pantalones  = ["adidas", "nike", "puma" , "fila"]
lista_de_marcas_remeras     = ["adidas", "nike", "puma" , "fila", "dc"]
lista_de_marcas_camisas     = ["etiqueta negra", "cuesta blanca", "levi's"]
lista_de_marcas_perfumes    = ["chanel", "paco rabanne", "nina ricci"]
lista_de_marcas_carteras    = ["chanel", "barbara"]

lista_de_colores = ["negro", "blanco", "rosa", "azul"]
talles = ["36", "38", "40" , "42"]


stock_calzado      = generar_stock(lista_de_marcas_calzado      , lista_de_colores, talles)
stock_remeras      = generar_stock(lista_de_marcas_remeras      , lista_de_colores, talles)
stock_camisas      = generar_stock(lista_de_marcas_camisas      , lista_de_colores, talles)
stock_perfumes     = generar_stock(lista_de_marcas_perfumes     , lista_de_colores, talles)
stock_carteras     = generar_stock(lista_de_marcas_carteras     , lista_de_colores, talles)
stock_pantalones   = generar_stock(lista_de_marcas_pantalones   , lista_de_colores, talles)

