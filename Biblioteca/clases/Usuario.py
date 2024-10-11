import tipo_usuario
import re
from rut import rut_identificador

class Usuario:
    def __init__(self, id_usuario, correo_usuario, telefono_usuario, habilitado, nombre_usuario, id_rut_nacional, id_rut_internacional, id_tipo_usuario):
        rut_identificador.__init__(id_rut_nacional)
        rut_identificador.__init__(id_rut_internacional)
        tipo_usuario.__init__(id_tipo_usuario)
        self.id_usuario = id_usuario
        self.correo_usuario = correo_usuario
        self.telefono_usuario = telefono_usuario
        self.habilitado = habilitado
        self.nombre_usuario = nombre_usuario
        
    def validar_rut_nacional(self):
        return rut_identificador.is_valid_rut(self.rut_nacional)
    
    def validar_rut_internacional(self):
        return rut_identificador.is_valid_rut(self.rut_internacional)
    
    def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo)):
            return True
        else:
            return False
        