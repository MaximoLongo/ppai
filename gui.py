import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import inicializar_datos, mostrar_bodegas, mostrar_vinos_de_bodega, obtener_bodegas_para_actualizar
from vino import Vino
from bodega import Bodega
class VinoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administración de Vinos")
        self.set_window_size_and_center(800, 600)  # Establecer tamaño y centrar la ventana
        self.bodegas = inicializar_datos()
        
        # Mostrar pantalla inicial
        self.show_initial_screen()
            
    def show_initial_screen(self):
        # Crear pantalla inicial
        self.clear_frame()
        # Colores


        self.initial_frame = tk.Frame(self.root, bg='silver')
        self.initial_frame.pack(pady=20, padx=20)

        self.title_label = tk.Label(self.initial_frame, text="Sistema de Administración de Vinos", font=("Arial", 30, "bold"),bg='silver',fg='black')
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.import_button = tk.Button(self.initial_frame, text="Importar Actualizaciones", command=self.select_bodega_to_update, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
        self.import_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.close_button = tk.Button(self.initial_frame, text="Cerrar Aplicación", command=self.root.quit, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
        self.close_button.grid(row=1, column=1, padx=10, pady=10)

    def clear_frame(self):
        # Eliminar todos los widgets del marco actual
        for widget in self.root.winfo_children():
            widget.destroy()

    def select_bodega_to_update(self):
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

        self.vinos_frame = tk.Frame(self.root,bg='silver')
        self.vinos_frame.pack(pady=20, padx=20)

        self.vinos_label = tk.Label(self.vinos_frame, text=f"Vinos en {bodega_seleccionada.nombre}:", font=("Helvetica", 16, "bold"),bg='silver',fg='black')
        self.vinos_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        if not bodega_seleccionada.vinos:
            self.no_vinos_label = tk.Label(self.vinos_frame, text="No hay vinos disponibles en esta bodega.", font=("Helvetica", 14),)
            self.no_vinos_label.grid(row=1, column=0, columnspan=2, pady=10)
            
            self.add_vino_button = tk.Button(self.vinos_frame, text="Agregar Vino", command=self.agregar_vino, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
            self.add_vino_button.grid(row=2, column=0, pady=10)

            self.back_button = tk.Button(self.vinos_frame, text="Volver", command=self.select_bodega_to_update, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
            self.back_button.grid(row=3, column=0, pady=10)
        else:
            self.selected_vino = tk.StringVar()  # Variable para almacenar el vino seleccionado
            self.selected_vino.set(bodega_seleccionada.vinos[0].nombre)  # Por defecto, seleccionamos el primer vino

            for i, vino in enumerate(bodega_seleccionada.vinos):
                tk.Radiobutton(self.vinos_frame, text=vino.nombre, variable=self.selected_vino, value=vino.nombre, font=("Helvetica", 12),bg='silver').grid(row=i+1, column=0, sticky="w", pady=5)

            self.show_details_button = tk.Button(self.vinos_frame, text="Ver Detalles", command=self.mostrar_datos_vino_seleccionado, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
            self.show_details_button.grid(row=len(bodega_seleccionada.vinos)+5, column=0, pady=10, padx=5)
            
            self.update_button = tk.Button(self.vinos_frame, text="Actualizar Vino", command=self.actualizar_vino, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
            self.update_button.grid(row=len(bodega_seleccionada.vinos)+5, column=1, pady=10, padx=5)
            
            self.add_vino_button = tk.Button(self.vinos_frame, text="Agregar Vino", command=self.agregar_vino, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
            self.add_vino_button.grid(row=len(bodega_seleccionada.vinos)+5, column=2, pady=10, padx=5)
            

            
            self.resumen_vinos_actualizados_button = tk.Button(self.vinos_frame, text="Resumen", command=self.mostrar_resumen_vinos_actualizados, font=("Helvetica", 14,"bold"), bg='green', fg='white')
            self.resumen_vinos_actualizados_button.grid(row=len(bodega_seleccionada.vinos)+5, column=3, pady=10, padx=5)
            
            self.back_button = tk.Button(self.vinos_frame, text="Volver", command=self.select_bodega_to_update, font=("Helvetica", 14,"bold"), bg='#0051c9', fg='white')
            self.back_button.grid(row=len(bodega_seleccionada.vinos)+7, column=1, pady=10, padx=5)
    
    def mostrar_resumen_vinos_actualizados(self):
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

            precio_label = tk.Label(vino_frame, text=f"Precio: ${vino.precio:.2f}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            precio_label.pack(fill='x')

            etiqueta_label = tk.Label(vino_frame, text=f"Imagen de etiqueta: {vino.imagen_etiqueta}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            etiqueta_label.pack(fill='x')

            nota_cata_label = tk.Label(vino_frame, text=f"Nota cata Bodega: {vino.nota_de_cata_bodega}", font=("Helvetica", 12), bg='silver', anchor='center', justify='center')
            nota_cata_label.pack(fill='x')

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
        nombre = simpledialog.askstring("Actualizar", f"Nuevo nombre para {vino_seleccionado.nombre} (dejar en blanco para mantener actual):", parent=self.root)
        anada = simpledialog.askinteger("Actualizar", f"Nuevo año para {vino_seleccionado.nombre} (dejar en blanco para mantener actual):", parent=self.root)
        imagen_etiqueta = simpledialog.askstring("Actualizar", f"Nueva imagen de etiqueta para {vino_seleccionado.nombre} (dejar en blanco para mantener actual):", parent=self.root)
        nota_de_cata_bodega = simpledialog.askstring("Actualizar", f"Nueva nota de cata bodega para {vino_seleccionado.nombre} (dejar en blanco para mantener actual):", parent=self.root)
        precio = simpledialog.askfloat("Actualizar", f"Nuevo precio para {vino_seleccionado.nombre} (dejar en blanco para mantener actual):", parent=self.root)
        self.root.attributes("-topmost", True)  # Reactivar ventana principal como "siempre en primer plano"

        vino_seleccionado.actualizar(
            nombre=nombre if nombre else None,
            anada=anada if anada else None,
            imagen_etiqueta=imagen_etiqueta if imagen_etiqueta else None,
            nota_de_cata_bodega=nota_de_cata_bodega if nota_de_cata_bodega else None,
            precio=precio if precio else None
        )

        messagebox.showinfo("Información", "Vino actualizado exitosamente!")
        self.mostrar_vinos()

    def agregar_vino(self):
        bodega_seleccionada = next((bodega for bodega in self.bodegas if bodega.nombre == self.selected_bodega.get()), None)
        if not bodega_seleccionada:
            messagebox.showerror("Error", "La bodega seleccionada no se encuentra.")
            return

        self.root.attributes("-topmost", False)  # Desactivar ventana principal como "siempre en primer plano"
        nombre = simpledialog.askstring("Agregar Vino", "Nombre del vino:", parent=self.root)
        if not nombre:
            messagebox.showerror("Error", "El nombre del vino es obligatorio.")
            self.root.attributes("-topmost", True)
            return
        
        anada = simpledialog.askinteger("Agregar Vino", "Año del vino:", parent=self.root)
        imagen_etiqueta = simpledialog.askstring("Agregar Vino", "Imagen de etiqueta del vino:", parent=self.root)
        nota_de_cata_bodega = simpledialog.askstring("Agregar Vino", "Nota de cata de la bodega:", parent=self.root)
        precio = simpledialog.askfloat("Agregar Vino", "Precio del vino:", parent=self.root)
        self.root.attributes("-topmost", True)  # Reactivar ventana principal como "siempre en primer plano"

        if anada is None or precio is None:
            messagebox.showerror("Error", "La añada y el precio del vino son obligatorios.")
            return

        nuevo_vino = Vino(
            nombre=nombre,
            anada=anada,
            imagen_etiqueta=imagen_etiqueta,
            nota_de_cata_bodega=nota_de_cata_bodega,
            precio=precio,
            estado="pendiente",
            periodo_actualizacion=bodega_seleccionada.periodo_actualizacion,
            bodega=bodega_seleccionada
        )
        bodega_seleccionada.agregar_vino(nuevo_vino)

        messagebox.showinfo("Información", "Vino agregado exitosamente!")
        self.mostrar_vinos()

    def set_window_size_and_center(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def cerrar_nueva_ventana(self, window):
        window.destroy()
        # Reactivar ventana principal como "siempre en primer plano"
        self.root.attributes("-topmost", True)

if __name__ == "__main__":
    root = tk.Tk()
    app = VinoApp(root)
    root.configure(bg='silver')  # Un azul suave
    root.mainloop()
