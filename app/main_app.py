from validaciones import validar_opcion
from funciones import (
    limpiar_pantalla, ejercicios, mostrar_tabla, cargar_datos, calcular_unidades_almacenadas, calcular_unidad_minima,
    maxima_cantidad_smarphone, mayor_recaudacion, deposito_con_mas_de_cincuentamil, porcentaje_por_deposito, tabla

)

def menu(lista_deposito, lista_cantidad, lista_precio, data_depositos, data_cantidad, data_precio):
    while True:
        ejercicios()
        opcion = validar_opcion(1, 9)
        match opcion:
            case 1:
                cargar_datos(lista_deposito, lista_cantidad, lista_precio, data_depositos, data_cantidad, data_precio)
                mostrar_tabla(lista_deposito,lista_cantidad,lista_precio)
            case 2:
                calcular_unidades_almacenadas(lista_cantidad)
            case 3:
                calcular_unidad_minima(lista_deposito,lista_cantidad)
            case 4:
                maxima_cantidad_smarphone(lista_deposito, lista_cantidad)
            case 5:
                mayor_recaudacion(lista_deposito, lista_cantidad, lista_precio)
            case 6:
                deposito_con_mas_de_cincuentamil(lista_deposito, lista_cantidad, lista_precio)
            case 7:
                porcentaje_por_deposito(lista_deposito, lista_cantidad)
            case 8:
                tabla(lista_cantidad, lista_precio, lista_deposito)
            case 9:
                break
        limpiar_pantalla()
