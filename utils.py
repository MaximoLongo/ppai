from vino import Vino
from bodega import Bodega
from random import choice

def inicializar_datos():
    bodega1 = Bodega("Bodega A", "", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega A", "2026")
    bodega2 = Bodega("Bodega B", "", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega B", "2026")
    bodega3 = Bodega("Bodega C", "", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega C", "2026")
    bodega4 = Bodega("Bodega D", "", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega D", "2026")
    bodega5 = Bodega("Bodega E", "", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega E", "2026")

    notas_cata_bodega = ['Brillante','Suave','Dulce','Ligero','Fresco','Simple','Excelente','Bueno','Aceptable','Deficiente']
    vino1 = Vino("Vino 1", 2015, "etiqueta1.jpg", choice(notas_cata_bodega), 20.0,"Malbec", 70.0, "Carnes rojas","pendiente", "2026", bodega1)
    vino2 = Vino("Vino 2", 2018, "etiqueta2.jpg", choice(notas_cata_bodega), 15.0,"Cabernet Sauvignon", 60.0, "Quesos maduros","actualizado", "2024", bodega1)
    vino3 = Vino("Vino 3", 2017, "etiqueta3.jpg", choice(notas_cata_bodega), 25.0,"Merlot", 80.0, "Pastas con salsa de tomate","pendiente", "2026", bodega1)
    vino4 = Vino("Vino 4", 2019, "etiqueta4.jpg", choice(notas_cata_bodega), 18.0,"Syrah", 70.0, "Carnes a la parrilla", "pendiente", "2026", bodega2)
    vino5 = Vino("Vino 5", 2016, "etiqueta5.jpg", choice(notas_cata_bodega), 22.0, "Malbec", 60.0, "Empanadas de carne","actualizado", "2024", bodega2)
    vino6 = Vino("Vino 6", 2017, "etiqueta6.jpg", choice(notas_cata_bodega), 30.0,"Cabernet Sauvignon", 80.0, "Cordero","pendiente", "2026", bodega2)
    vino7 = Vino("Vino 7", 2018, "etiqueta7.jpg", choice(notas_cata_bodega), 16.0, "Malbec", 70.0, "Asado argentino","pendiente", "2026", bodega3)
    vino8 = Vino("Vino 8", 2019, "etiqueta8.jpg", choice(notas_cata_bodega), 24.0,"Syrah", 60.0, "Queso azul","actualizado", "2024", bodega3)
    vino9 = Vino("Vino 9", 2016, "etiqueta9.jpg", choice(notas_cata_bodega), 28.0, "Merlot", 80.0, "Carnes blancas","pendiente", "2026", bodega4)
    vino10 = Vino("Vino 10", 2017, "etiqueta10.jpg", choice(notas_cata_bodega), 19.0,"Malbec", 70.0, "Parrillada mixta", "pendiente", "2026", bodega5)

    bodega1.crearVino(vino1)
    bodega1.crearVino(vino2)
    bodega2.crearVino(vino3)
    bodega2.crearVino(vino4)
    bodega2.crearVino(vino5)
    bodega3.crearVino(vino6)
    bodega3.crearVino(vino7)
    bodega3.crearVino(vino8)
    bodega4.crearVino(vino9)
    bodega5.crearVino(vino10)
    
    return [bodega1, bodega2, bodega3, bodega4, bodega5]

def mostrar_bodegas(bodegas):
    if not bodegas:
        return "No hay bodegas para mostrar."
    else:
        return "\n".join(str(bodega) for bodega in bodegas)

def mostrar_vinos_de_bodega(bodega):
    return bodega.mostrar_todos_los_vinos()

def obtener_bodegas_para_actualizar(bodegas, periodo_actual):
    return [bodega for bodega in bodegas if bodega.obtener_vino_para_actualizar(periodo_actual)]
    
def mostrar_vinos_para_actualizar(vinos):
    if not vinos:
        return "No hay vinos para actualizar."
    else:
        return "\n".join(str(vino) for vino in vinos)
