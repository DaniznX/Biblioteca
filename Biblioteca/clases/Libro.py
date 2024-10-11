class libro:
    def __init__(self,isbn, titulo, autor, npagina, editorial, año):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.npagina= npagina
        self.editorial = editorial
        self.año = año
        
    def validar_isbn(self):
        if(10 <= len(self.isbn) <= 13 and self.isbn.isdigit()):
            return True
        else:
            return False
        