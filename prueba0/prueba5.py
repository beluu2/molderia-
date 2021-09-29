frutas_in_stock = {
    "manzana"   : {"cantidad": 5, "precio_unitario": 2.5}, 
    "frutilla"  : {"cantidad": 50, "precio_unitario" : 56}, 
    "banana"    : {"cantidad": 100, "precio_unitario" : 23},  
    "peras"     : {"cantidad": 213, "precio_unitario" : 90}
    }

pedido_fruta = input("ingrese la fruta ")
pedido_cantidad = input("ingrese la cantidad ")


fruta_elegida = frutas_in_stock[pedido_fruta]
print(fruta_elegida)



cantidad = fruta_elegida["cantidad"] 
# print("Su compra: %s")

precio_unitario = fruta_elegida ["precio_unitario"]
precio_total = precio_unitario * int(pedido_cantidad)

print (precio_total)
