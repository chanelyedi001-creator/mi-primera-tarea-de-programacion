# Lista de productos
productos = {

    1: ("jugo", 100),
    2: ("Pizza", 500),
    3: ("Hamburguesa", 350),
    4: ("Refresco", 100),
    5: ("Ensalada", 250)


   


}

print("===== MENÚ =====")

for codigo, datos in productos.items():
    print(codigo, "-", datos[0], "- RD$", datos[1])

opcion = int(input("\nSeleccione un producto: "))

if opcion in productos:

    nombre = productos[opcion][0]
    precio = productos[opcion][1]

    impuesto = precio * 0.18
    propina = precio * 0.10

    total = precio + impuesto + propina

    print("\nProducto:", nombre)
    print("Precio:", precio)
    print("Impuesto:", impuesto)
    print("Propina:", propina)
    print("Total:", total)

else:
    print("Producto no existe.")

    