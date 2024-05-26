from vino import Vino
from bodega import Bodega

def inicializar_datos():
    bodega1 = Bodega("Bodega A", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega A", "2026")
    bodega2 = Bodega("Bodega B", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega B", "2026")
    bodega3 = Bodega("Bodega C", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega C", "2026")
    bodega4 = Bodega("Bodega D", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega D", "2026")
    bodega5 = Bodega("Bodega E", "40.7128, -74.0060", "Una bodega histórica", "Historia de la Bodega E", "2026")

    vino1 = Vino("Vino 1", 2015, "etiqueta1.jpg", "Cata Bodega A1", 20.0, "pendiente", "2026", bodega1)
    vino2 = Vino("Vino 2", 2018, "etiqueta2.jpg", "Cata Bodega A2", 15.0, "actualizado", "2024", bodega1)
    vino3 = Vino("Vino 3", 2017, "etiqueta3.jpg", "Cata Bodega A3", 25.0, "pendiente", "2026", bodega1)
    vino4 = Vino("Vino 4", 2019, "etiqueta4.jpg", "Cata Bodega B1", 18.0, "pendiente", "2026", bodega2)
    vino5 = Vino("Vino 5", 2016, "etiqueta5.jpg", "Cata Bodega B2", 22.0, "actualizado", "2024", bodega2)
    vino6 = Vino("Vino 6", 2017, "etiqueta6.jpg", "Cata Bodega B3", 30.0, "pendiente", "2026", bodega2)
    vino7 = Vino("Vino 7", 2018, "etiqueta7.jpg", "Cata Bodega C1", 16.0, "pendiente", "2026", bodega3)
    vino8 = Vino("Vino 8", 2019, "etiqueta8.jpg", "Cata Bodega C2", 24.0, "actualizado", "2024", bodega3)
    vino9 = Vino("Vino 9", 2016, "etiqueta9.jpg", "Cata Bodega C3", 28.0, "pendiente", "2026", bodega3)
    vino10 = Vino("Vino 10", 2017, "etiqueta10.jpg", "Cata Bodega D1", 19.0, "pendiente", "2026", bodega4)
        
    bodega1.agregar_vino(vino1)
    bodega1.agregar_vino(vino2)
    bodega1.agregar_vino(vino3)
    bodega1.agregar_vino(vino4)
    bodega1.agregar_vino(vino5)
    bodega1.agregar_vino(vino6)
    bodega1.agregar_vino(vino7)
    bodega1.agregar_vino(vino8)
    bodega1.agregar_vino(vino9)
    bodega1.agregar_vino(vino10)
    
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
