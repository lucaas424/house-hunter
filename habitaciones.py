class Habitacion:
    def __init__(self, numero, tipo, esta_ocupada=False):
        self.numero = numero
        self.tipo = tipo
        self.esta_ocupada = esta_ocupada

    def ocupar(self):
        self.esta_ocupada = True

    def liberar(self):
        self.esta_ocupada = False

    def mostrar_info(self):
        estado = "Ocupada" if self.esta_ocupada else "Libre"
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Estado: {estado}"


if __name__ == "__main__":
    habitacion_101 = Habitacion(101, "Doble")
    print(habitacion_101.mostrar_info())
    habitacion_101.ocupar()
    print(habitacion_101.mostrar_info())
