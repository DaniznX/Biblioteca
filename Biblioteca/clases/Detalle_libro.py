import Libro
import Editorial
class detalle_libro:
    def __init__(self, id_detalle_libro, isbn, fecha_edicion, id_editorial, numero_paginas, id_categoria_libro, cantidad_libro, libros_disponibles):
        Libro.__init__(isbn)
        Editorial.__init__(id_editorial)
        self.id_detalle_libro = id_detalle_libro
        self.fecha_edicion = fecha_edicion
        self.numero_paginas = numero_paginas
        self.id_categoria_libro = id_categoria_libro
        self.cantidad_libro = cantidad_libro
        self.libros_disponibles = libros_disponibles
    def actualizar_disponibilidad(self, origen, cantidad):
        if(self.cantidad_libro > self.libros_disponibles + cantidad):
            if(origen == "retirar"):
                if(self.libros_disponibles > 0):
                    self.libros_disponibles = self.libros_disponibles - cantidad
                else:
                    print("No hay libros disponilbles para realizar el prestamo solicitado.")
            else:
                self.libros_disponibles = self.libros_disponibles + cantidad
        else:
            print("Nuestros registros indican que hay un error en la cantidad de ejemplares.")