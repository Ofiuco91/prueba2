def menu_de_opciones():
    opcion  = input("""----------- Menu de opciones --------------
                    1-Listar los alumnos por orden ascendente de apellido, si se repite, ordenar por nombre.
                    Mostrar legajo, nombre, apellido y edad.
                    2-Obtener el promedio de notas para cada estudiante
                    3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de 
                    “Ingenieria en Informatica”
                    4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y apellido
                    5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido
                    6-Listar nombre y apellido de los alumnos que forman el grupo “Club de
                    Informática” con sus respectivos promedios
                    7-Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.
                    opcion:...""")
    return opcion

def ordenar_por_apellido_y_nombre(lista:list):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]["apellido"] > lista[j]["apellido"]:
                aux =  lista[i]
                lista[i]=lista[j]
                lista[j]=aux
            if lista[i]["apellido"] == lista[j]["apellido"]:
                if lista[i]["nombre"]>lista[j]["nombre"]:
                    aux = lista[i]
                    lista[i]=lista[j]
                    lista[j]=aux
    for estudiante in lista:
        print(f"nombre: {estudiante["nombre"]} legajo:{estudiante["legajo"]} apellido:{estudiante["apellido"]} edad:{estudiante["edad"]}")

def promediar_notas(lista:list):
    promedio = 0
    for i in lista:
        promedio = round(sum(i["notas"]) / len(i["notas"]),1)

        print(f"el estudiante: {i["nombre"]} {i["apellido"]} tiene un promedio de: {promedio}")

def listar_datos_informaticos(lista:list):
     for i in lista:
           if i["programa"]["nombre"]=="Ingenieria en Informatica":
               print(f"nombre: {i["nombre"]} apellido: {i["apellido"]} legajo: {i["legajo"]} edad: {i["edad"]}")

def promedio_edad(lista:list):
        promedio = 0
        contador = 0
        print("estudiantes:")
        for i in lista:
            contador += 1
            promedio = i["edad"] + promedio
            print(f"nombre: {i["nombre"]} apellido: {i["apellido"]}")
        promedio = promedio / contador
        print("el promedio de edad de los estudiantes es: ",promedio)

def informar_alumno_mayor_promedio(lista:list):
    promedio = 0
    mayor_promedio=0
    for i in lista:
        promedio = round(sum(i["notas"]) / len(i["notas"]),1)
        if promedio > mayor_promedio:
            mayor_promedio = promedio
    for i in lista:
        if round(sum(i["notas"]) / len(i["notas"]),1) == mayor_promedio:
            print(f"el/los alumno/s con mayor promedio es: {i["nombre"]} {i["apellido"]} y es de: {mayor_promedio} ")

def menor_edad(lista):
    menor_edad=1000
    for i in lista:
        if i["edad"]<menor_edad:
            menor_edad = i["edad"]
    return menor_edad

def programas_mas_jovenes(lista):
    for i in lista:
        if i["edad"] == menor_edad(lista):
            print(f"nombre: {i["nombre"]} apellido: {i["apellido"]} programas: {i["programa"]["nombre"]}")
        