import tkinter as tk
from tkinter import ttk, messagebox

class Cola:
    """
    Clase que implementa una estructura de datos Cola (FIFO).
    
    Atributos:
        elementos: Lista que almacena los elementos de la cola.
    """
    def __init__(self):
        """Inicializa una cola vacía."""
        self.elementos = []
    
    def encolar(self, dato):
        """Agrega un elemento al final de la cola.
        
        Args:
            dato: Elemento a agregar a la cola.
        """
        self.elementos.append(dato)
    
    def desencolar(self):
        """Elimina y retorna el primer elemento de la cola.
        
        Returns:
            El elemento removido de la cola.
            
        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.elementos.pop(0)
    
    def frente(self):
        """Retorna el primer elemento de la cola sin eliminarlo.
        
        Returns:
            El elemento al frente de la cola.
            
        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.elementos[0]
    
    def esta_vacia(self):
        """Verifica si la cola está vacía.
        
        Returns:
            bool: True si la cola está vacía, False en caso contrario.
        """
        return len(self.elementos) == 0
    
    def tamanio(self):
        """Retorna el número de elementos en la cola.
        
        Returns:
            int: Cantidad de elementos en la cola.
        """
        return len(self.elementos)
    
    def obtener_elementos(self):
        """Retorna una lista con todos los elementos de la cola.
        
        Returns:
            list: Elementos de la cola en orden (frente a final).
        """
        return self.elementos.copy()

class AplicacionColas:
    """
    Clase principal que maneja la interfaz gráfica de la aplicación de colas.
    """
    def __init__(self, root):
        """Inicializa la aplicación con la ventana principal."""
        self.root = root
        self.root.title("Aplicación de Colas")
        self.root.geometry("600x450")
        
        # Inicializar la cola
        self.cola = Cola()
        
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
        ttk.Button(frame_controles, text="Encolar", command=self._encolar).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Desencolar", command=self._desencolar).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Ver Frente", command=self._ver_frente).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Tamaño", command=self._mostrar_tamanio).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Recorrer", command=self._recorrer).pack(side=tk.LEFT, padx=2)  # Cambiado de ¿Vacía? a Recorrer
        ttk.Button(frame_controles, text="Limpiar", command=self._limpiar_cola).pack(side=tk.LEFT, padx=2)
        
        # Frame de visualización
        frame_visual = ttk.Frame(self.main_frame)
        frame_visual.pack(fill=tk.BOTH, expand=True)
        
        # Canvas para representación gráfica de la cola
        self.canvas = tk.Canvas(frame_visual, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Actualizar visualización inicial
        self._actualizar_visualizacion()
    
    def _encolar(self):
        """Maneja la operación de encolar un elemento."""
        dato = self.entry_dato.get()
        if not dato:
            messagebox.showwarning("Advertencia", "Por favor ingrese un dato")
            return
        
        self.cola.encolar(dato)
        self._actualizar_visualizacion()
        self.entry_dato.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Dato '{dato}' encolado correctamente")
    
    def _desencolar(self):
        """Maneja la operación de desencolar un elemento."""
        try:
            dato = self.cola.desencolar()
            self._actualizar_visualizacion()
            messagebox.showinfo("Éxito", f"Dato '{dato}' desencolado correctamente")
        except IndexError:
            messagebox.showerror("Error", "No se puede desencolar: la cola está vacía")
    
    def _ver_frente(self):
        """Muestra el elemento al frente de la cola."""
        try:
            dato = self.cola.frente()
            messagebox.showinfo("Frente de la cola", f"El elemento al frente es: '{dato}'")
        except IndexError:
            messagebox.showerror("Error", "La cola está vacía")
    
    def _mostrar_tamanio(self):
        """Muestra el tamaño actual de la cola."""
        tamanio = self.cola.tamanio()
        messagebox.showinfo("Tamaño de la cola", f"La cola contiene {tamanio} elementos")
    
    def _recorrer(self):
        """Muestra todos los elementos de la cola en un cuadro de mensaje."""
        elementos = self.cola.obtener_elementos()
        if not elementos:
            messagebox.showinfo("Recorrido de la cola", "La cola está vacía")
        else:
            mensaje = "Elementos de la cola (desde el frente hasta el final):\n\n"
            mensaje += "\n".join([f"• {elemento}" for elemento in elementos])
            messagebox.showinfo("Recorrido de la cola", mensaje)
    
    def _limpiar_cola(self):
        """Limpia todos los elementos de la cola."""
        if not self.cola.esta_vacia():
            self.cola = Cola()  # Crear una nueva cola vacía
            self._actualizar_visualizacion()
            messagebox.showinfo("Éxito", "La cola ha sido vaciada completamente")
        else:
            messagebox.showwarning("Advertencia", "La cola ya está vacía")
    
    def _actualizar_visualizacion(self):
        """Actualiza la representación gráfica de la cola."""
        self.canvas.delete("all")
        elementos = self.cola.obtener_elementos()
        
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        
        # Dimensiones de cada elemento de la cola
        elem_ancho = 80
        elem_alto = 40
        margen = 10
        espacio = 5
        
        # Posición inicial (centro horizontal)
        x = (ancho - (elem_ancho + espacio) * len(elementos)) / 2 if len(elementos) > 0 else ancho / 2
        y = alto / 2 - elem_alto / 2
        
        # Dibujar cada elemento de la cola (de izquierda a derecha)
        for i, dato in enumerate(elementos):
            # Dibujar rectángulo
            self.canvas.create_rectangle(
                x, y, 
                x + elem_ancho, y + elem_alto,
                fill="#2196F3", outline="#0D47A1",
                width=2
            )
            
            # Texto del dato
            self.canvas.create_text(
                x + elem_ancho / 2, y + elem_alto / 2,
                text=str(dato),
                fill="white",
                font=("Arial", 10, "bold")
            )
            
            # Flechas entre elementos (excepto para el último)
            if i < len(elementos) - 1:
                self.canvas.create_line(
                    x + elem_ancho, y + elem_alto / 2,
                    x + elem_ancho + espacio, y + elem_alto / 2,
                    arrow=tk.LAST,
                    width=2
                )
            
            # Indicar frente y final
            if i == 0:
                self.canvas.create_text(
                    x + elem_ancho / 2, y - 10,
                    text="FRENTE",
                    fill="black",
                    font=("Arial", 8, "bold")
                )
            if i == len(elementos) - 1:
                self.canvas.create_text(
                    x + elem_ancho / 2, y + elem_alto + 15,
                    text="FINAL",
                    fill="black",
                    font=("Arial", 8, "bold")
                )
            
            x += elem_ancho + espacio

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionColas(root)
    root.mainloop()