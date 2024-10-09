from data import * 
from app import menu
lista_deposito = [[] for _ in range(20)]
lista_cantidad = [[] for _ in range(20)]
lista_precio = [[] for _ in range(20)]
lista_acumulado = [[] for _ in range(20)]
posibles_marcas = ["Xiaomi", "Samsung", "Infinix", "Nubia"]

if __name__ == "__main__":
    menu(lista_deposito, lista_cantidad, lista_precio, data_depositos, data_cantidad, data_precio)