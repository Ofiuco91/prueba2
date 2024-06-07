def menu_de_opciones():
    opcion = input("""--------  Menu de opciones  ----------------
                      1-Alta de productos (producto nuevo)
                      2-Baja de productos (producto existente)
                      3-Modificar productos (cantidad, ubicación)
                      4-Listar productos
                      5-Lista de productos ordenado por nombre
                      6-Salir
                      por favor, ingrese una opcion: """)
    return opcion

def alta_productos(productos:list):
    existe = False
    nombre = input("ingrese nuevo producto ")
    cantidad = int(input("ingrese cantidad "))
    fila = int(input("ingrese fila "))
    columna= int(input("ingrese columna "))
    for i in range(len(productos)):
        #for j in range(i+1,(len(productos))):
            if productos[i][2] == fila and productos[i][3]==columna: #verifico si hay algo
                existe = True
    if existe == True:
            print("error, ese lugar ya esta ocupado")
    else:
            productos.append([nombre,cantidad,fila,columna])
            print("producto agregado con exito")

def baja_de_productos(productos:list):
    existe = False
    fila= int(input("ingrese fila donde se encuentra el producto a quitar "))
    columna=int(input("ingrese columna donde se encuentra el producto a quitar "))
    for i in range(len(productos)):
        #for j in range(i+1,(len(productos))):
            if (productos[i][2] == fila) and (productos[i][3]==columna):
                existe = True
                productos.pop(i)
                print("producto dado de baja con exito")
    if existe == False:
                print("error, no se puede dar de baja, lugar vacio o inexistente")

def modificar_productos(productos:list):
    existe = False
    nuevo_existe=False
    fila=int(input("ingrese fila donde se encuentra: "))
    columna=int(input("ingrese columna donde se encuentra:"))
    for i in range(len(productos)):
        if (productos[i][2] == fila) and (productos[i][3]==columna):
                existe = True
                nueva_fila = int(input("Ingrese la nueva fila: "))
                nueva_columna = int(input("Ingrese la nueva columna: "))
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

                for j in range(len(productos)):
                    if productos[j][2] == nueva_fila and productos[j][3] == nueva_columna:
                        nuevo_existe = True
                        break
                    
                if nuevo_existe == True:
                        print("no se puede mover a este lugar por que ya esta ocupado")
                else:
                    productos[i][2] = nueva_fila
                    productos[i][3] = nueva_columna
                    productos[i][1] = nueva_cantidad
                    print("producto modificado con exito")
                break
    if existe == False:
            print("no se puede modificar, lugar vacio o inexistente")

def listar_productos(productos:list):
      for i in range(len(productos)):
           print("producto:",productos[i][0],"cantidad:",productos[i][1])

def listar_productos_ordenados_nombre(productos:list):
      for i in range(len(productos)):
              for j in range(1+i,len(productos)):
                   if productos[i]>productos[j]:
                        auxp=productos[i][0]
                        auxc=productos[i][1]
                        productos[i][0] = productos[j][0]
                        productos[i][1] = productos[j][1]
                        productos[j][0]=auxp
                        productos[j][1]=auxc
        
      listar_productos(productos)

def listar_cajonera(cajonera:list):
       for i in range(len(cajonera)):
               listar_productos(cajonera[i])

def reponer_mercaderia(cajonera:list):
    existe=False
    tipo = input("ingrese el tipo y tamaño del producto que desea reponer (tipo y medida ej: to12)")
    cantidad= int(input("ingrese la cantidad a reponer"))
    for fila in cajonera:
     for cajon in fila:
        if cajon[0] == tipo:
            existe =True
            cajon[1] += cantidad
            print(f"{cantidad} unidades de {tipo} repuestas.")
     if existe == False:
            print("el tipo no existe")

def vender_mercaderia(cajonera:list):
    existe = False
    tipo = input("ingrese el tipo y tamaño del producto que va a vender ")
    cantidad= int(input("ingrese la cantidad a vender "))
    for fila in cajonera:
        for cajon in fila:
            if cajon[0]==tipo and cajon[1] >= cantidad:
                existe = True
                cajon[1] -= cantidad
                print(f"{cantidad} unidades de {tipo} vendidas.")
        if existe == False:
            print("error no existe el tipo o no alcanza la cantidad a vender")