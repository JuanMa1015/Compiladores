import tkinter as tk
from tkinter import ttk, messagebox

class Pila:
    """
    Clase que implementa una estructura de datos Pila (LIFO).
    
    Atributos:
        elementos: Lista que almacena los elementos de la pila.
    """
    def __init__(self):
        """Inicializa una pila vacía."""
        self.elementos = []
    
    def apilar(self, dato):
        """Agrega un elemento a la parte superior de la pila.
        
        Args:
            dato: Elemento a agregar a la pila.
        """
        self.elementos.append(dato)
    
    def desapilar(self):
        """Elimina y retorna el elemento superior de la pila.
        
        Returns:
            El elemento removido de la pila.
            
        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.elementos.pop()
    
    def cima(self):
        """Retorna el elemento superior de la pila sin eliminarlo.
        
        Returns:
            El elemento en la cima de la pila.
            
        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.elementos[-1]
    
    def esta_vacia(self):
        """Verifica si la pila está vacía.
        
        Returns:
            bool: True si la pila está vacía, False en caso contrario.
        """
        return len(self.elementos) == 0
    
    def tamanio(self):
        """Retorna el número de elementos en la pila.
        
        Returns:
            int: Cantidad de elementos en la pila.
        """
        return len(self.elementos)
    
    def obtener_elementos(self):
        """Retorna una lista con todos los elementos de la pila.
        
        Returns:
            list: Elementos de la pila en orden (base a cima).
        """
        return self.elementos.copy()

class AplicacionPilas:
    """
    Clase principal que maneja la interfaz gráfica de la aplicación de pilas.
    """
    def __init__(self, root):
        """Inicializa la aplicación con la ventana principal."""
        self.root = root
        self.root.title("Aplicación de Pilas")
        self.root.geometry("500x400")
        
        # Inicializar la pila
        self.pila = Pila()
        
        # Configurar la interfaz gráfica
        self._configurar_interfaz()
    
    def _configurar_interfaz(self):
        """Configura todos los elementos de la interfaz gráfica."""
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame de controles
        frame_controles = ttk.Frame(self.main_frame)
        frame_controles.pack(fill=tk.X, pady=5)
        
        # Etiqueta y campo de entrada
        ttk.Label(frame_controles, text="Dato:").pack(side=tk.LEFT, padx=5)
        self.entry_dato = ttk.Entry(frame_controles, width=15)
        self.entry_dato.pack(side=tk.LEFT, padx=5)
        
        # Botones de operaciones
        ttk.Button(frame_controles, text="Apilar", command=self._apilar).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Desapilar", command=self._desapilar).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Ver Cima", command=self._ver_cima).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Tamaño", command=self._mostrar_tamanio).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="¿Vacía?", command=self._verificar_vacia).pack(side=tk.LEFT, padx=2)
        
        # Frame de visualización
        frame_visual = ttk.Frame(self.main_frame)
        frame_visual.pack(fill=tk.BOTH, expand=True)
        
        # Canvas para representación gráfica de la pila
        self.canvas = tk.Canvas(frame_visual, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Actualizar visualización inicial
        self._actualizar_visualizacion()
    
    def _apilar(self):
        """Maneja la operación de apilar un elemento."""
        dato = self.entry_dato.get()
        if not dato:
            messagebox.showwarning("Advertencia", "Por favor ingrese un dato")
            return
        
        self.pila.apilar(dato)
        self._actualizar_visualizacion()
        self.entry_dato.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Dato '{dato}' apilado correctamente")
    
    def _desapilar(self):
        """Maneja la operación de desapilar un elemento."""
        try:
            dato = self.pila.desapilar()
            self._actualizar_visualizacion()
            messagebox.showinfo("Éxito", f"Dato '{dato}' desapilado correctamente")
        except IndexError:
            messagebox.showerror("Error", "No se puede desapilar: la pila está vacía")
    
    def _ver_cima(self):
        """Muestra el elemento en la cima de la pila."""
        try:
            dato = self.pila.cima()
            messagebox.showinfo("Cima de la pila", f"El elemento en la cima es: '{dato}'")
        except IndexError:
            messagebox.showerror("Error", "La pila está vacía")
    
    def _mostrar_tamanio(self):
        """Muestra el tamaño actual de la pila."""
        tamanio = self.pila.tamanio()
        messagebox.showinfo("Tamaño de la pila", f"La pila contiene {tamanio} elementos")
    
    def _verificar_vacia(self):
        """Verifica y muestra si la pila está vacía."""
        vacia = self.pila.esta_vacia()
        estado = "vacía" if vacia else "no vacía"
        messagebox.showinfo("Estado de la pila", f"La pila está {estado}")
    
    def _actualizar_visualizacion(self):
        """Actualiza la representación gráfica de la pila."""
        self.canvas.delete("all")
        elementos = self.pila.obtener_elementos()
        
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        
        # Dimensiones de cada elemento de la pila
        elem_ancho = ancho - 40
        elem_alto = 30
        margen = 5
        
        # Posición inicial (parte inferior)
        y = alto - margen
        
        # Dibujar cada elemento de la pila (de abajo hacia arriba, sin reversed)
        for i, dato in enumerate(elementos):
            y -= elem_alto + margen
            if y < margen:  # No dibujar si no hay espacio
                break
                
            # Dibujar rectángulo
            self.canvas.create_rectangle(
                margen, y, 
                margen + elem_ancho, y + elem_alto,
                fill="#4CAF50", outline="#2E7D32"
            )
            
            # Texto del dato
            self.canvas.create_text(
                ancho / 2, y + elem_alto / 2,
                text=str(dato),
                fill="white",
                font=("Arial", 10, "bold")
            )
            
            # Flecha indicando la cima (solo para el último elemento)
            if i == len(elementos) - 1:
                self.canvas.create_text(
                    margen + elem_ancho + 10, y + elem_alto / 2,
                    text="↑ CIMA",
                    fill="black",
                    font=("Arial", 8)
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionPilas(root)
    root.mainloop()