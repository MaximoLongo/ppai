from datetime import datetime

class Bodega:
    def __init__(self, nombre, fechaUltimaActualizacion,coordenadas_ubicacion, descripcion, historia, periodo_actualizacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaUltimaActualizacion = fechaUltimaActualizacion
        self.coordenadas_ubicacion = coordenadas_ubicacion
        self.historia = historia
        self.periodo_actualizacion = periodo_actualizacion
        self.vinos = []  # Lista de vinos en la bodega
        self.vinos_actualizados = []

    def crearVino(self, vino):
        self.vinos.append(vino)
        self.vinos_actualizados.append(vino)
        
    def actualizar_vinos(self,vino):
        self.vinos_actualizados.append(vino)
        self.fechaUltimaActualizacion = datetime.now()
    
    def eliminar_vino(self, vino):
        if vino in self.vinos:
            self.vinos.remove(vino)
        else:
            raise ValueError(f"El vino {self.nombre} no se encuentra en esta bodega.")
        
    def mostrar_resumen_vinos_actualizados(self):
        resumen = "Resumen de Vinos Actualizados:\n"
        for vino in self.vinos_actualizados:
            resumen += f"Vino: {vino.nombre}, Añada: {vino.anada}, Precio: {vino.precio}\n"
        return resumen
    
    def mostrar_todos_los_vinos(self):
        if self.vinos:
            return "\n".join(str(vino) for vino in self.vinos)
        else:
            return f"No hay vinos en {self.nombre}."
    
    def __str__(self):
        return f"{self.nombre} - {self.descripcion}, Historia: {self.historia}, Coordenadas: {self.coordenadas_ubicacion}"
