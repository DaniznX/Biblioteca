import Libro
class Biblioteca:
    def __init__(self, id_biblioteca, nombre, direccion, telefono, isbn):
        Libro.__init__(isbn)
        self.id_biblioteca = id_biblioteca
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def buscar_libro(identificacion):
        pass
    def prestar_libro(self):
        pass
    def devolver_libri(self):
        pass