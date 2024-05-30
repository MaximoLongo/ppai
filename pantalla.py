import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import inicializar_datos
from vino import Vino
import random
import string
from datetime import datetime


class ImportarActualizaciónVinosBodega:
    def __init__(self, root):
        self.root = root
        self.root.title("Administración de Vinos")
        self.set_window_size_and_center(800, 600)  # Establecer tamaño y centrar la ventana
        self.bodegas = inicializar_datos()
        
        # Mostrar pantalla inicial
        self.show_initial_screen()
    def generar_datos_aleatorios(self):
        anada = random.randint(1900, 2024)  # Genera un año aleatorio entre 1900 y 2024
        imagen_etiqueta = f'etiqueta.jpg'  
        notas_cata_bodega = ['Brillante','Suave','Dulce','Ligero','Fresco','Simple','Excelente','Bueno','Aceptable','Deficiente']
        nota_de_cata_bodega = random.choice(notas_cata_bodega)
        precio = round(random.uniform(10, 100), 2)  # Genera un precio aleatorio entre 10 y 100 con 2 decimales
        varietales = ['Malbec', 'Cabernet Sauvignon', 'Merlot', 'Syrah', 'Chardonnay', 'Torrontés', 'Bonarda', 'Sauvignon Blanc', 'Tannat', 'Pinot Noir']
        nombreVarietal = random.choice(varietales)
        porcentajeVarietal = float(random.randint(50, 100))
        tipo_maridaje = ['Carnes rojas', 'Quesos maduros', 'Pastas con salsa de tomate', 'Carnes a la parrilla', 'Empanadas de carne', 'Cordero', 'Asado argentino', 'Queso azul', 'Carnes blancas', 'Parrillada mixta']
        maridaje = random.choice(tipo_maridaje)

        return anada, imagen_etiqueta, nota_de_cata_bodega, precio ,nombreVarietal,porcentajeVarietal,maridaje
    
    def actualizarCaracteristicasVinoExistente(self):
        bodega_seleccionada = next((bodega for bodega in self.bodegas if bodega.nombre == self.selected_bodega.get()), None)
        if not bodega_seleccionada:
            messagebox.showerror("Error", "La bodega seleccionada no se encuentra.")
            return
    
        for vino in bodega_seleccionada.vinos:
            anada, imagen_etiqueta, nota_de_cata_bodega, precio, nombreVarietal,porcentajeVarietal,maridaje = self.generar_datos_aleatorios()
            vino.actualizar(
                anada=anada,
                imagen_etiqueta=imagen_etiqueta,
                nota_de_cata_bodega=nota_de_cata_bodega,
                precio=precio,
                nombreVarietal=nombreVarietal,
                porcentajeVarietal=porcentajeVarietal,
                maridaje=maridaje
            )
    
        messagebox.showinfo("Información", "Todos los vinos han sido actualizados exitosamente!")
        self.mostrar_vinos()

        messagebox.showinfo("Información", "Vino actualizado exitosamente!")
        self.mostrar_vinos()
    def show_initial_screen(self):
        # Crear pantalla inicial
        self.clear_frame()
        # Colores.
        self.initial_frame = tk.Frame(self.root, bg='silver')
        self.initial_frame.pack(pady=20, padx=20)

        self.title_label = tk.Label(self.initial_frame, text="Sistema de Administración de Vinos", font=("Arial", 30, "bold"),bg='silver',fg='black')
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.import_button = tk.Button(self.initial_frame, text="Importar Actualizaciones", command=self.buscarBodegasParaActualizar, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
        self.import_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.close_button = tk.Button(self.initial_frame, text="Cerrar Aplicación", command=self.root.quit, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
        self.close_button.grid(row=1, column=1, padx=10, pady=10)

    def clear_frame(self):
        # Eliminar todos los widgets del marco actual
        for widget in self.root.winfo_children():
            widget.destroy()

    def buscarBodegasParaActualizar(self):
        bodegas_para_actualizar = self.bodegas
        if not bodegas_para_actualizar:
            messagebox.showinfo("Información", "No hay bodegas con vinos para actualizar.")
            return
        
        self.clear_frame()

        self.update_frame = tk.Frame(self.root,bg='silver')
        self.update_frame.pack(pady=20, padx=20)

        self.update_label = tk.Label(self.update_frame, text="Seleccione la bodega que desea actualizar:", font=("Helvetica", 18,"bold"),bg='silver',fg='black')
        self.update_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.selected_bodega = tk.StringVar(value=bodegas_para_actualizar[0].nombre)  # Por defecto, seleccionamos la primera bodega

        for i, bodega in enumerate(bodegas_para_actualizar):
            tk.Radiobutton(self.update_frame, text=bodega.nombre, variable=self.selected_bodega, value=bodega.nombre, font=("Helvetica", 14),bg='silver').grid(row=i+1, column=0, sticky="w", pady=5)

        self.update_button = tk.Button(self.update_frame, text="Aceptar", command=self.mostrar_vinos, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
        self.update_button.grid(row=len(bodegas_para_actualizar)+2, column=0, pady=10)
        

        
        # Agregar botón para volver a la pantalla inicial
        self.back_button = tk.Button(self.update_frame, text="Volver", command=self.show_initial_screen, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
        self.back_button.grid(row=len(bodegas_para_actualizar)+2, column=1, pady=10)

    def mostrar_vinos(self):
        bodega_seleccionada = next((bodega for bodega in self.bodegas if bodega.nombre == self.selected_bodega.get()), None)
        if not bodega_seleccionada:
            messagebox.showerror("Error", "La bodega seleccionada no se encuentra.")
            return
        
        self.clear_frame()

        self.vinos_frame = tk.Frame(self.root, bg='silver')
        self.vinos_frame.pack(pady=20, padx=20)

        self.vinos_label = tk.Label(self.vinos_frame, text=f"Vinos en {bodega_seleccionada.nombre}:", font=("Helvetica", 16, "bold"), bg='silver', fg='black')
        self.vinos_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Botón para obtener vinos
        self.obtener_vinos_button = tk.Button(self.vinos_frame, text="Obtener Vinos", command=self.obtener_vinos, font=("Helvetica", 14, "bold"), bg='#0051c9', fg='white')
        self.obtener_vinos_button.grid(row=1, column=0, pady=10)

        self.back_button = tk.Button(self.vinos_frame, text="Volver", command=self.buscarBodegasParaActualizar, font=("Helvetica", 14, "bold"), bg='#0051c9', fg='white')
        self.back_button.grid(row=2, column=0, pady=10)

    def obtener_vinos(self):
        bodega_seleccionada = next((bodega for bodega in self.bodegas if bodega.nombre == self.selected_bodega.get()), None)
        if not bodega_seleccionada:
            messagebox.showerror("Error", "La bodega seleccionada no se encuentra.")
            return

        if not bodega_seleccionada.vinos:
            self.no_vinos_label = tk.Label(self.vinos_frame, text="No hay vinos disponibles en esta bodega.", font=("Helvetica", 14), bg='silver')
            self.no_vinos_label.grid(row=3, column=0, columnspan=2, pady=10)

            self.add_vino_button = tk.Button(self.vinos_frame, text="Agregar Vino", command=self.crearVino, font=("Helvetica", 14, "bold"), bg='#0051c9', fg='white')
            self.add_vino_button.grid(row=4, column=0, pady=10)
            
        else:
            self.selected_vino = tk.StringVar()  # Variable para almacenar el vino seleccionado
            self.selected_vino.set(bodega_seleccionada.vinos[0].nombre)  # Por defecto, seleccionamos el primer vino

            for i, vino in enumerate(bodega_seleccionada.vinos):
                tk.Radiobutton(self.vinos_frame, text=vino.nombre, variable=self.selected_vino, value=vino.nombre, font=("Helvetica", 12), bg='silver').grid(row=i+3, column=0, sticky="w", pady=5)

            self.show_details_button = tk.Button(self.vinos_frame, text="Ver Detalles", command=self.mostrar_datos_vino_seleccionado, font=("Helvetica", 14, "bold"), bg='#0051c9', fg='white')
            self.show_details_button.grid(row=len(bodega_seleccionada.vinos)+4, column=0, pady=10, padx=5)
            
            self.update_random_button = tk.Button(self.vinos_frame, text="Actualizar Vinos", command=self.actualizarCaracteristicasVinoExistente, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
            self.update_random_button.grid(row=len(bodega_seleccionada.vinos)+4, column=1, pady=10, padx=5)
            
            self.add_vino_button = tk.Button(self.vinos_frame, text="Agregar Vino", command=self.crearVino, font=("Helvetica", 14, "bold"), bg='#0051c9', fg='white')
            self.add_vino_button.grid(row=len(bodega_seleccionada.vinos)+4, column=2, pady=10, padx=5)
            
            self.resumen_vinos_actualizados_button = tk.Button(self.vinos_frame, text="Resumen", command=self.mostrarResumenVinosImportados, font=("Helvetica", 14, "bold"), bg='green', fg='white')
            self.resumen_vinos_actualizados_button.grid(row=len(bodega_seleccionada.vinos)+4, column=3, pady=10, padx=5)

            self.back_button.grid(row=len(bodega_seleccionada.vinos)+5, column=0, pady=10)
    
    def mostrarResumenVinosImportados(self):
        bodega_seleccionada = next((bodega for bodega in self.bodegas if bodega.nombre == self.selected_bodega.get()), None)
        if not bodega_seleccionada:
            messagebox.showerror("Error", "La bodega seleccionada no se encuentra.")
            return

        if not hasattr(bodega_seleccionada, 'vinos_actualizados') or not bodega_seleccionada.vinos_actualizados:
            messagebox.showinfo("Información", "No hay vinos actualizados para esta bodega.")
            return


        # Crear una nueva ventana
        new_window = tk.Toplevel(self.root)
        new_window.attributes('-topmost', True)
        new_window.geometry("800x600")  # Ajusta el tamaño de la ventana
        new_window.title("Resumen de Vinos Actualizados")  # Agrega un título a la ventana
        new_window.configure(bg='silver')  # Cambia el color de fondo de la ventana a plata

        # Crear un frame con scrollbar
        frame = tk.Frame(new_window, bg='silver')
        frame.pack(fill='both', expand=True)

        canvas = tk.Canvas(frame, bg='silver')
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='silver')

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)


        # Agregar un título al resumen
        titulo_label = tk.Label(scrollable_frame, text="Resumen de Vinos Actualizados", font=("Helvetica", 16, "bold"), bg='silver', fg='black')
        titulo_label.pack(pady=(10, 20))

        # Mostrar cada vino actualizado
        for vino in bodega_seleccionada.vinos_actualizados:
            vino_frame = tk.Frame(scrollable_frame, bg='silver', padx=10, pady=5, relief='groove', bd=2)
            vino_frame.pack(fill='x', pady=5)

            nombre_label = tk.Label(vino_frame, text=f"Vino: {vino.nombre}", font=("Helvetica", 14), bg='silver', anchor='center', justify='center')
            nombre_label.pack(fill='x')

            anada_label = tk.Label(vino_frame, text=f"Añada: {vino.anada}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            anada_label.pack(fill='x')

            etiqueta_label = tk.Label(vino_frame, text=f"Imagen de etiqueta: {vino.imagen_etiqueta}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            etiqueta_label.pack(fill='x')

            nota_cata_label = tk.Label(vino_frame, text=f"Nota cata Bodega: {vino.nota_de_cata_bodega}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            nota_cata_label.pack(fill='x')

            precio_label = tk.Label(vino_frame, text=f"Precio: ${vino.precio}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            precio_label.pack(fill='x')

            nombreVarietal_label = tk.Label(vino_frame, text=f"Nombre Varietal: {vino.nombreVarietal}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            nombreVarietal_label.pack(fill='x')

            porcentajeVarietal_label = tk.Label(vino_frame, text=f"Porcentaje Varietal: {vino.porcentajeVarietal}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            porcentajeVarietal_label.pack(fill='x')

            maridaje_label = tk.Label(vino_frame, text=f"Maridaje: {vino.maridaje}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            maridaje_label.pack(fill='x')

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Crear un botón para cerrar la ventana
        close_button = tk.Button(new_window, text="Cerrar", command=new_window.destroy, font=("Helvetica", 14, "bold"), bg='#0051c9', fg='white')
        close_button.pack(pady=10)


        
    def mostrar_datos_vino_seleccionado(self):
        bodega_seleccionada = next((bodega for bodega in self.bodegas if bodega.nombre == self.selected_bodega.get()), None)
        if not bodega_seleccionada:
            messagebox.showerror("Error", "La bodega seleccionada no se encuentra.")
            return
    
        vino_seleccionado = next((vino for vino in bodega_seleccionada.vinos if vino.nombre == self.selected_vino.get()), None)
        if not vino_seleccionado:
            messagebox.showerror("Error", "El vino seleccionado no se encuentra en esta bodega.")
            return
    
        detalles_vino = f"Nombre: {vino_seleccionado.nombre}\n"
        detalles_vino += f"Añada: {vino_seleccionado.anada}\n"
        detalles_vino += f"Imagen de etiqueta: {vino_seleccionado.imagen_etiqueta}\n"
        detalles_vino += f"Nota de cata bodega: {vino_seleccionado.nota_de_cata_bodega}\n"
        detalles_vino += f"Precio: {vino_seleccionado.precio}\n"
        detalles_vino += f"Nombre Varietal: {vino_seleccionado.nombreVarietal}\n"
        detalles_vino += f"Porcentaje Varietal: {vino_seleccionado.porcentajeVarietal}\n"
        detalles_vino += f"Maridaje: {vino_seleccionado.maridaje}\n"
    
        # Crear una nueva ventana
        new_window = tk.Toplevel(self.root)
        new_window.attributes('-topmost', True)
        new_window.geometry("500x500")  # Puedes ajustar el tamaño de la ventana aquí
        new_window.title("Datos del Vino")  # Agregar un título a la ventana
        new_window.configure(bg='silver')  # Cambiar el color de fondo de la ventana a plata
    
        # Crear un label para "DATOS:"
        title_label = tk.Label(new_window, text="DATOS:", font=("Helvetica", 18, "bold"), bg='silver')
        title_label.pack(padx=10, pady=10)
    
        # Crear un label para mostrar los detalles del vino
        label = tk.Label(new_window, text=detalles_vino, font=("Helvetica", 14), justify='center', bg='silver')
        label.pack(padx=10, pady=10)
    
        # Crear un botón para cerrar la ventana
        close_button = tk.Button(new_window, text="Cerrar", command=new_window.destroy, font=("Helvetica", 14, "bold"), bg='#0051c9', fg='white')
        close_button.pack(pady=10)
    
    def actualizar_vino(self):
        bodega_seleccionada = next((bodega for bodega in self.bodegas if bodega.nombre == self.selected_bodega.get()), None)
        if not bodega_seleccionada:
            messagebox.showerror("Error", "La bodega seleccionada no se encuentra.")
            return

        vino_seleccionado = next((vino for vino in bodega_seleccionada.vinos if vino.nombre == self.selected_vino.get()), None)
        if not vino_seleccionado:
            messagebox.showerror("Error", "El vino seleccionado no se encuentra en esta bodega.")
            return

        self.root.attributes("-topmost", False)  # Desactivar ventana principal como "siempre en primer plano"
        anada = 1111
        imagen_etiqueta = 1111
        nota_de_cata_bodega = 1111
        precio = 1111
        nombreVarietal = 1111
        porcentajeVarietal = 1111
        maridaje = 1111
        self.root.attributes("-topmost", True)  # Reactivar ventana principal como "siempre en primer plano"

        vino_seleccionado.actualizar(
            anada=anada if anada else None,
            imagen_etiqueta=imagen_etiqueta if imagen_etiqueta else None,
            nota_de_cata_bodega=nota_de_cata_bodega if nota_de_cata_bodega else None,
            precio=precio if precio else None,
            nombreVarietal=nombreVarietal if nombreVarietal else None,
            porcentajeVarietal=porcentajeVarietal if porcentajeVarietal else None,
            maridaje=maridaje if maridaje else None
        )

        messagebox.showinfo("Información", "Vino actualizado exitosamente!")
        self.mostrar_vinos()

    def crearVino(self):
        bodega_seleccionada = next((bodega for bodega in self.bodegas if bodega.nombre == self.selected_bodega.get()), None)
        if not bodega_seleccionada:
            messagebox.showerror("Error", "La bodega seleccionada no se encuentra.")
            return

        self.root.attributes("-topmost", False)  # Desactivar ventana principal como "siempre en primer plano"
        nombre = simpledialog.askstring("Agregar Vino", "Nombre del vino:", parent=self.root)
        if nombre is None:
            self.root.attributes("-topmost", True)
            return
        while not nombre:
            messagebox.showerror("Error", "El nombre del vino es obligatorio.")
            nombre = simpledialog.askstring("Agregar Vino", "Nombre del vino:", parent=self.root)
            if nombre is None:
                self.root.attributes("-topmost", True)
                return
        anada = simpledialog.askstring("Agregar Vino", "Año del vino:", parent=self.root)
        if anada is None:
            self.root.attributes("-topmost", True)
            return
        while not anada or not anada.isdigit() or not (1900 <= int(anada) <= 2024):
            messagebox.showerror("Error", "El año del vino es obligatorio y debe ser un número entre 1900 y 2024.")
            anada = simpledialog.askstring("Agregar Vino", "Año del vino:", parent=self.root)
            if anada is None:
                self.root.attributes("-topmost", True)
                return
        imagen_etiqueta = simpledialog.askstring("Agregar Vino", "Imagen de etiqueta del vino:", parent=self.root)
        if imagen_etiqueta is None:
            self.root.attributes("-topmost", True)
            return
        while not imagen_etiqueta:
            messagebox.showerror("Error", "La imagen de etiqueta del vino es obligatoria.")
            imagen_etiqueta = simpledialog.askstring("Agregar Vino", "Imagen de etiqueta del vino:", parent=self.root)
            if imagen_etiqueta is None:
                self.root.attributes("-topmost", True)
                return

        notas_de_cata = ['Brillante', 'Suave', 'Dulce', 'Ligero', 'Fresco', 'Simple', 'Excelente', 'Bueno', 'Aceptable', 'Deficiente']
        nota_de_cata_bodega = simpledialog.askstring("Agregar Vino", "Nota de cata de la bodega (Brillante, Suave, Dulce, Ligero, Fresco, Simple, Excelente, Bueno, Aceptable, Deficiente):", parent=self.root)
        if nota_de_cata_bodega is None:
            self.root.attributes("-topmost", True)
            return
        while not nota_de_cata_bodega or nota_de_cata_bodega not in notas_de_cata:
            messagebox.showerror("Error", "La nota de cata de la bodega es obligatoria y debe respetar el formato.")
            nota_de_cata_bodega = simpledialog.askstring("Agregar Vino", "Nota de cata de la bodega (Brillante, Suave, Dulce, Ligero, Fresco, Simple, Excelente, Bueno, Aceptable, Deficiente):", parent=self.root)
            if nota_de_cata_bodega is None:
                self.root.attributes("-topmost", True)
                return

        precio = simpledialog.askstring("Agregar Vino", "Precio del vino:", parent=self.root)
        if precio is None:
            self.root.attributes("-topmost", True)
            return
        def is_float(num):
            try:
                float(num)
                return True
            except ValueError:
                return False
        while not precio or not is_float(precio) or float(precio) < 0:
            messagebox.showerror("Error", "El precio del vino es obligatorio y debe ser un número positivo.")
            precio = simpledialog.askstring("Agregar Vino", "Precio del vino:", parent=self.root)
            if precio is None:
                self.root.attributes("-topmost", True)
                return

        varietales = ['Malbec', 'Cabernet Sauvignon', 'Merlot', 'Syrah', 'Chardonnay', 'Torrontés', 'Bonarda', 'Sauvignon Blanc', 'Tannat', 'Pinot Noir']
        nombre_varietales = []
        porcentaje_varietales = []
        total_porcentaje = 0

        while total_porcentaje < 100:
            nombre_varietal = simpledialog.askstring("Agregar Vino", f"Nombre del Varietal del vino (Malbec, Cabernet Sauvignon, Merlot, Syrah, Chardonnay, Torrontés, Bonarda, Sauvignon Blanc, Tannat, Pinot Noir):", parent=self.root)
            if nombre_varietal is None:
                self.root.attributes("-topmost", True)
                return
            while not nombre_varietal or nombre_varietal not in varietales:
                messagebox.showerror("Error", "El nombre del Varietal del vino es obligatorio y debe ser un nombre de Varietal válido.")
                nombre_varietal = simpledialog.askstring("Agregar Vino", f"Nombre del Varietal del vino (Malbec, Cabernet Sauvignon, Merlot, Syrah, Chardonnay, Torrontés, Bonarda, Sauvignon Blanc, Tannat, Pinot Noir):", parent=self.root)
                if nombre_varietal is None:
                    self.root.attributes("-topmost", True)
                    return

            porcentaje_varietal = simpledialog.askstring("Agregar Vino", "Porcentaje del Varietal del vino:", parent=self.root)
            if porcentaje_varietal is None:
                self.root.attributes("-topmost", True)
                return
            while not porcentaje_varietal or not is_float(porcentaje_varietal) or not (0 < float(porcentaje_varietal) <= 100 - total_porcentaje):
                messagebox.showerror("Error", f"El porcentaje del Varietal del vino es obligatorio y debe ser un número entre 0 y {100 - total_porcentaje}.")
                porcentaje_varietal = simpledialog.askstring("Agregar Vino", "Porcentaje del Varietal del vino:", parent=self.root)
                if porcentaje_varietal is None:
                    self.root.attributes("-topmost", True)
                    return

            nombre_varietales.append(nombre_varietal)
            porcentaje_varietales.append(float(porcentaje_varietal))
            total_porcentaje += float(porcentaje_varietal)

            if total_porcentaje < 100:
                add_more = messagebox.askyesno("Agregar Vino", f"El porcentaje total es {total_porcentaje}%. ¿Desea agregar más varietales?")
                if not add_more:
                    break

        if total_porcentaje != 100:
            messagebox.showerror("Error", "La suma de los porcentajes de varietales debe ser 100%.")
            self.root.attributes("-topmost", True)
            return

        tipo_maridaje = ['Carnes rojas', 'Quesos maduros', 'Pastas con salsa de tomate', 'Carnes a la parrilla', 'Empanadas de carne', 'Cordero', 'Asado argentino', 'Queso azul', 'Carnes blancas', 'Parrillada mixta']
        maridaje = simpledialog.askstring("Agregar Vino", "Tipo de maridaje del vino (Carnes rojas, Quesos maduros, Pastas con salsa de tomate, Carnes a la a la parrilla, Empanadas de carne, Cordero, Asado argentino, Queso azul, Carnes blancas, Parrillada mixta")
        self.root.attributes("-topmost", True)  # Reactivar ventana principal como "siempre en primer plano"

        nuevo_vino = Vino(
            nombre=nombre,
            anada=anada,
            imagen_etiqueta=imagen_etiqueta,
            nota_de_cata_bodega=nota_de_cata_bodega,
            precio=precio,
            nombreVarietal=nombre_varietal,
            porcentajeVarietal=porcentaje_varietales,
            maridaje=maridaje,
            estado="pendiente",
            periodo_actualizacion=bodega_seleccionada.periodo_actualizacion,
            bodega=bodega_seleccionada
        )
        bodega_seleccionada.crearVino(nuevo_vino)

        messagebox.showinfo("Información", "Vino agregado exitosamente!")
        self.mostrar_vinos()

    def set_window_size_and_center(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def finCU(self, window):
        window.destroy()
        # Reactivar ventana principal como "siempre en primer plano"
        self.root.attributes("-topmost", True)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImportarActualizaciónVinosBodega(root)
    root.configure(bg='silver')  # Un azul suave
    root.mainloop()




