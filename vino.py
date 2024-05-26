class Vino:
    def __init__(self, nombre, anada, imagen_etiqueta, nota_de_cata_bodega, precio, estado, periodo_actualizacion, bodega):
        self.nombre = nombre
        self.anada = anada
        self.imagen_etiqueta = imagen_etiqueta
        self.nota_de_cata_bodega = nota_de_cata_bodega
        self.precio = precio
        self.estado = estado
        self.periodo_actualizacion = periodo_actualizacion
        self.bodega = bodega
        
    def actualizar(self, nombre=None, anada=None, imagen_etiqueta=None, nota_de_cata_bodega=None, precio=None):
        actualizado = False
        if nombre:
            self.nombre = nombre
            actualizado = True
        if anada:
            self.anada = anada
            actualizado = True
        if imagen_etiqueta:
            self.imagen_etiqueta = imagen_etiqueta
            actualizado = True
        if nota_de_cata_bodega:
            self.nota_de_cata_bodega = nota_de_cata_bodega
            actualizado = True
        if precio:
            self.precio = precio
            actualizado = True
        return actualizado

    def esDeBodega(self):
        return self.bodega

    def __str__(self):
        return f"Nombre:{self.nombre} - Añada({self.anada}) - Precio: ${self.precio}, Estado: {self.estado}, Periodo de Actualización: {self.periodo_actualizacion}, Bodega: {self.bodega.nombre}"
