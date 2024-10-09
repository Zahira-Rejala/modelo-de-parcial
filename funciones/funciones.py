
#Ejercicio 1
def cargar_datos(lista_deposito: list[list], lista_cantidad: list[list], lista_precio: list[list], data_depositos: list[list], data_cantidad: list[list], data_precio: list[list]) -> None: 
    """Esa funcion lo que hace es cargar la existencia de las listas de deposito, cantidad y precio a unas listas vacias

    Args:
        lista_deposito (list[list]): Lista de listas vacia
        lista_cantidad (list[list]): Lista de listas vacia
        lista_precio (list[list]): Lista de listas vacia
        data_depositos (list[list]): Lista de listas con los datos de los smarphones
        data_cantidad (list[list]): Lista de listas con los datos de la cantidad 
        data_precio (list[list]): Lista de listas con los precios de los smarphones

        No retorna nada
    """
    for i in range(len(data_depositos)):
        for j in range(len(data_depositos[i])):
            lista_deposito[i].append(data_depositos[i][j])
            lista_cantidad[i].append(data_cantidad[i][j])
            lista_precio[i].append(data_precio[i][j])

def mostrar_tabla(lista_deposito: list[list], lista_cantidad: list[list], lista_precio: list[list]) -> None:
    """Esta funcion lo que hace es mostrar la tabla con todos los depositos y sus datos almacenados

    Args:
        lista_deposito (list[list]): Lista de listas vacia
        lista_cantidad (list[list]): Lista de listas vacia
        lista_precio (list[list]): Lista de listas vacia
        data_depositos (list[list]): Lista de listas con los datos de los smarphones

        No retorna nada
    """
    print(f"|   Deposito   |   Marca   |   Cantidad   |     Precio     |    Acumulado    ")
    for i in range(len(lista_deposito)):
        for j in range(len(lista_deposito[i])):
            acumulado = lista_cantidad[i][j] * lista_precio[i][j]
            print(f"| {i + 1:<12} | {lista_deposito[i][j]:<9} | {lista_cantidad[i][j]:<12} | ${lista_precio[i][j]:<14}| ${acumulado:<17}")



#Ejercicio 2
def calcular_unidades_almacenadas(lista_cantidad: list[list]) -> None:
    acumulador = 0
    for i in range(len(lista_cantidad)):
        for j in range(len(lista_cantidad[i])):
            acumulador = acumulador + lista_cantidad[i][j]
    print(f"La cantidad es de {acumulador} unidades en TOTAL")


#Ejercicio 3
def calcular_unidad_minima(lista_deposito, lista_cantidad):
    minimo = 0
    deposito_menor = None
    for i in range(len(lista_cantidad)):
        for j in range(len(lista_cantidad[i])):
            if minimo == 0 or minimo > lista_cantidad[i][j]:
                minimo = lista_cantidad[i][j]
                deposito_menor = lista_cantidad[i]

    print(f"La unidad de menor cantidad es {lista_deposito[i][j]} con {deposito_menor} unidades en el deposito {i + 1}")

#Ejercicio 4
def funcion(lista_deposito, lista_cantidad, marca):
    acumulador = 0
    for i in range(len(lista_cantidad)):
        for j in range(len(lista_cantidad[i])):
            if lista_deposito[i][j] == marca:
                acumulador += lista_cantidad[i][j]
    return acumulador

def maxima_cantidad_smarphone(lista_deposito, lista_cantidad):
    for i in range (len(lista_deposito)):
        for j in range (len(lista_deposito[i])):
            funcion(lista_deposito, lista_cantidad, marca= "Infinix")
    print(f"La cantidad maxima de smarphones de Infinix es de {funcion(lista_deposito, lista_cantidad, "Infinix")}")
    for i in range (len(lista_deposito)):
        for j in range (len(lista_deposito[i])):
            funcion(lista_deposito, lista_cantidad, marca= "Xiaomi")
    print(f"La cantidad maxima de smarphones de Xiaomi es de {funcion(lista_deposito, lista_cantidad, "Xiaomi")}")
    for i in range (len(lista_deposito)):
        for j in range (len(lista_deposito[i])):
            funcion(lista_deposito, lista_cantidad, marca= "Nubia")
    print(f"La cantidad maxima de smarphones de Nubia es de {funcion(lista_deposito, lista_cantidad, "Nubia")}")
    for i in range (len(lista_deposito)):
        for j in range (len(lista_deposito[i])):
            funcion(lista_deposito, lista_cantidad, marca= "Samsung")
    print(f"La cantidad maxima de smarphones de Samsung es de {funcion(lista_deposito, lista_cantidad, "Samsung")}")


#Ejercicio 5
def mayor_recaudacion(lista_deposito, lista_cantidad, lista_precio):
    maximo = 0
    deposito_mayor = None
    for i in range(len(lista_deposito)):
        for j in range(len(lista_deposito[i])):
            acumulado = lista_cantidad[i][j] * lista_precio[i][j]
            if maximo == 0 or maximo < acumulado:
                maximo = acumulado
                deposito_mayor = lista_deposito[i][j]
    print(f"La unidad de mayor recaudacion es {deposito_mayor} con {maximo} unidades en el deposito {i}")


#Ejercicio 6
def deposito_con_mas_de_cincuentamil(lista_deposito, lista_cantidad, lista_precio):
    contador = 0
    for i in range(len(lista_deposito)):
        for j in range(len(lista_deposito[i])):
            if lista_cantidad[i][j] > 50000:
                contador += 1
#                mostrar_tabla(lista_deposito[i][j], lista_cantidad[i][j], lista_precio[i][j])
    print(f"La cantidad de depositos con mas de 50000 de recaudacion son: {contador}")
    

#Ejercicio 7
def porcentaje_por_deposito(lista_deposito, lista_cantidad):
    total_smarphones = 0
    for i in range(len(lista_cantidad)):
        for j in range(len(lista_cantidad[i])):
            total_smarphones += lista_cantidad[i][j]
    numero_samsung = funcion(lista_deposito, lista_cantidad, marca="Samsung")
    numero_xiaomi = funcion(lista_deposito, lista_cantidad, marca="Xiaomi")
    numero_nubia = funcion(lista_deposito, lista_cantidad, marca="Nubia")
    numero_infinix = funcion(lista_deposito, lista_cantidad, marca="Infinix")

    porcentaje_samsung = (numero_samsung / total_smarphones) * 100
    porcentaje_xiaomi = (numero_xiaomi / total_smarphones) * 100
    porcentaje_nubia = (numero_nubia / total_smarphones) * 100
    porcentaje_infinix = (numero_infinix / total_smarphones) * 100
    print(f"El porcentaje de Samsung es %{porcentaje_samsung}")
    print(f"El porcentaje de Xiaomi es %{porcentaje_xiaomi}")
    print(f"El porcentaje de Nubia es %{porcentaje_nubia}")
    print(f"El porcentaje de Infinix es &{porcentaje_infinix}")
    lista_porcentaje = []
    lista_porcentaje.append(porcentaje_infinix)
    lista_porcentaje.append(porcentaje_nubia)
    lista_porcentaje.append(porcentaje_samsung)
    lista_porcentaje.append(porcentaje_xiaomi)
    maximo = 0
    for i in range(len(lista_porcentaje)):
        if maximo == 0 or maximo < lista_porcentaje[i]:
            maximo = lista_porcentaje[i]
    print(f"La marca con mas porcentaje es Xiaomi con {lista_porcentaje[i]}")

#Ejercicio 8
def tabla(lista_cantidad, lista_precio, lista_deposito):
    lista_acumulado = [[] for _ in range(20)]
    for i in range(len(lista_deposito)):
        for j in range(len(lista_deposito[i])):
            acumulado = lista_cantidad[i][j] * lista_precio[i][j]
            lista_acumulado[i].append(acumulado)

    print(f"{lista_acumulado}")

    # cantidad_columnas = len(lista_acumulado[0])
    # for i in range(cantidad_columnas - 1):
    #     indice_maximo = i
    #     for j in range(i + 1, cantidad_columnas):
    #         if lista_acumulado[j] > lista_acumulado[indice_maximo]:
    #             indice_maximo = j
    #     if indice_maximo != i:
    #         for indice_fila in range(len(lista_acumulado)):
    #             lista_acumulado[indice_fila][i], lista_acumulado[indice_fila][indice_maximo] = lista_acumulado[indice_fila][indice_maximo], lista_acumulado[indice_fila][i]
    # print(f"{lista_acumulado}")
    for i in range(0, len(lista_acumulado)):
        maximo = i
        for j in range(i + 1, len(lista_acumulado)):
            if lista_acumulado[j] > lista_acumulado[i]:
                maximo = j
        lista_acumulado[i], lista_acumulado[maximo] = lista_acumulado[maximo], lista_acumulado[i]
    
    print(f"{lista_acumulado}")