from abc import ABC, abstractmethod

class Documento(ABC):
    def __init__(self, titulo):
        self.titulo = titulo
    
    @abstractmethod
    def exportar(self):
        pass

    # OPCIONAL: los padres abstractos pueden tener metodos normales
    def mostrar_titulo(self):
        print(f"Documento: {self.titulo}")

class PDF(Documento):
    def exportar(self):
        print(f"Esportando {self.titulo} a PDF...")

class Word(Documento):
    def exportar(self):
        print(f"Esportando {self.titulo} a Word...")

class Excel(Documento):
    def exportar(self):
        print(f"Esportando {self.titulo} a Excel...")

# Dara error porque no se puede instanciar una clase abstracta
try:
    doc_invalido = Documento("Mi archivo")
except:
    print(f"[BLOQUEO DE SEGURIDAD]")

pdf_doc = PDF("Reporte de Ventas")
pdf_doc.mostrar_titulo()
pdf_doc.exportar()

word_doc = Word("Informe Anual")
word_doc.mostrar_titulo()
word_doc.exportar()

excel_doc = Excel("presupuesto 2023")
excel_doc.mostrar_titulo()
excel_doc.exportar()