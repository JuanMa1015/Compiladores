"""
Aplicación gráfica para manipular listas enlazadas simples y doblemente enlazadas.

Este programa permite realizar operaciones básicas como inserción, eliminación, recorrido
y visualización en ambos tipos de listas, mostrando los resultados en una interfaz gráfica
desarrollada con Tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox

class NodoSimple:
    """
    Clase que representa un nodo de una lista simplemente enlazada.
    
    Atributos:
        dato: Valor almacenado en el nodo.
        siguiente: Referencia al siguiente nodo en la lista.
    """
    def __init__(self, dato):
        """Inicializa un nodo con el dato proporcionado."""
        self.dato = dato
        self.siguiente = None  # Apuntador al siguiente nodo (inicialmente None)

class ListaSimple:
    """
    Clase que implementa una lista simplemente enlazada.
    
    Atributos:
        cabeza: Referencia al primer nodo de la lista.
    """
    def __init__(self):
        """Inicializa una lista vacía."""
        self.cabeza = None  # La lista comienza vacía
    
    def esta_vacia(self):
        """Verifica si la lista está vacía.
        
        Returns:
            bool: True si la lista está vacía, False en caso contrario.
        """
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        """Inserta un nuevo nodo al inicio de la lista.
        
        Args:
            dato: Valor a insertar en la lista.
        """
        nuevo = NodoSimple(dato)  # Crear nuevo nodo
        nuevo.siguiente = self.cabeza  # El nuevo nodo apunta a la antigua cabeza
        self.cabeza = nuevo  # El nuevo nodo se convierte en la cabeza
    
    def insertar_final(self, dato):
        """Inserta un nuevo nodo al final de la lista.
        
        Args:
            dato: Valor a insertar en la lista.
        """
        nuevo = NodoSimple(dato)
        if self.esta_vacia():
            self.cabeza = nuevo  # Si está vacía, el nuevo nodo es la cabeza
        else:
            actual = self.cabeza
            # Recorrer hasta encontrar el último nodo
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo  # El último nodo apunta al nuevo
    
    def eliminar(self, dato):
        """Elimina la primera ocurrencia del dato en la lista.
        
        Args:
            dato: Valor a eliminar de la lista.
            
        Returns:
            bool: True si se eliminó el dato, False si no se encontró.
        """
        if self.esta_vacia():
            return False  # Lista vacía, no hay nada que eliminar
        
        # Caso especial: eliminar el primer nodo
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return True
        
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        # Buscar el nodo a eliminar
        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente  # Saltar el nodo a eliminar
                return True
            anterior = actual
            actual = actual.siguiente
        
        return False  # Dato no encontrado
    
    def obtener_lista(self):
        """Obtiene todos los elementos de la lista en orden.
        
        Returns:
            list: Lista con los elementos en orden de la lista enlazada.
        """
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return elementos

class NodoDoble:
    """
    Clase que representa un nodo de una lista doblemente enlazada.
    
    Atributos:
        dato: Valor almacenado en el nodo.
        siguiente: Referencia al siguiente nodo en la lista.
        anterior: Referencia al nodo anterior en la lista.
    """
    def __init__(self, dato):
        """Inicializa un nodo con el dato proporcionado."""
        self.dato = dato
        self.siguiente = None  # Apuntador al siguiente nodo
        self.anterior = None  # Apuntador al nodo anterior

class ListaDoble:
    """
    Clase que implementa una lista doblemente enlazada.
    
    Atributos:
        cabeza: Referencia al primer nodo de la lista.
        cola: Referencia al último nodo de la lista.
    """
    def __init__(self):
        """Inicializa una lista vacía."""
        self.cabeza = None
        self.cola = None
    
    def esta_vacia(self):
        """Verifica si la lista está vacía.
        
        Returns:
            bool: True si la lista está vacía, False en caso contrario.
        """
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        """Inserta un nuevo nodo al inicio de la lista.
        
        Args:
            dato: Valor a insertar en la lista.
        """
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo  # Lista vacía, cabeza y cola son el nuevo nodo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo  # El nuevo nodo se convierte en la cabeza
    
    def insertar_final(self, dato):
        """Inserta un nuevo nodo al final de la lista.
        
        Args:
            dato: Valor a insertar en la lista.
        """
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo  # El nuevo nodo se convierte en la cola
    
    def eliminar(self, dato):
        """Elimina la primera ocurrencia del dato en la lista.
        
        Args:
            dato: Valor a eliminar de la lista.
            
        Returns:
            bool: True si se eliminó el dato, False si no se encontró.
        """
        if self.esta_vacia():
            return False  # Lista vacía
        
        # Caso 1: Eliminar el primer nodo
        if self.cabeza.dato == dato:
            if self.cabeza == self.cola:  # Solo hay un nodo
                self.cabeza = self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            return True
        
        # Caso 2: Eliminar el último nodo
        if self.cola.dato == dato:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            return True
        
        # Caso 3: Eliminar un nodo intermedio
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.dato == dato:
                actual.anterior.siguiente = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        
        return False  # Dato no encontrado
    
    def obtener_lista_adelante(self):
        """Obtiene todos los elementos de la lista en orden de inicio a fin.
        
        Returns:
            list: Lista con los elementos en orden de inicio a fin.
        """
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return elementos
    
    def obtener_lista_atras(self):
        """Obtiene todos los elementos de la lista en orden de fin a inicio.
        
        Returns:
            list: Lista con los elementos en orden de fin a inicio.
        """
        elementos = []
        actual = self.cola
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.anterior
        return elementos

class AplicacionListas:
    """
    Clase principal que maneja la interfaz gráfica de la aplicación.
    
    Atributos:
        root: Ventana principal de Tkinter.
        lista_simple: Instancia de ListaSimple.
        lista_doble: Instancia de ListaDoble.
    """
    def __init__(self, root):
        """Inicializa la aplicación con la ventana principal."""
        self.root = root
        self.root.title("Listas Encadenadas - Documentado")
        self.root.geometry("600x400")
        
        # Inicializar las estructuras de datos
        self.lista_simple = ListaSimple()
        self.lista_doble = ListaDoble()
        
        # Configurar la interfaz gráfica
        self._configurar_interfaz()
    
    def _configurar_interfaz(self):
        """Configura todos los elementos de la interfaz gráfica."""
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña para Lista Simple
        self._crear_pestana_lista_simple()
        
        # Pestaña para Lista Doble
        self._crear_pestana_lista_doble()
    
    def _crear_pestana_lista_simple(self):
        """Crea y configura la pestaña para la lista simplemente enlazada."""
        self.tab_simple = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_simple, text="Lista Simple")
        
        # Frame para controles
        frame_controles = ttk.Frame(self.tab_simple)
        frame_controles.pack(fill=tk.X, pady=5)
        
        # Etiqueta y campo de entrada
        ttk.Label(frame_controles, text="Dato:").pack(side=tk.LEFT, padx=5)
        self.entry_dato_simple = ttk.Entry(frame_controles, width=15)
        self.entry_dato_simple.pack(side=tk.LEFT, padx=5)
        
        # Botones de operaciones
        ttk.Button(frame_controles, text="Insertar inicio", 
                  command=lambda: self._insertar_inicio("simple")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Insertar final", 
                  command=lambda: self._insertar_final("simple")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Eliminar", 
                  command=lambda: self._eliminar("simple")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Recorrer", 
                  command=lambda: self._recorrer("simple")).pack(side=tk.LEFT, padx=2)
        
        # Frame para visualización
        frame_visual = ttk.Frame(self.tab_simple)
        frame_visual.pack(fill=tk.BOTH, expand=True)
        
        # Listbox para mostrar elementos
        self.listbox_simple = tk.Listbox(frame_visual)
        self.listbox_simple.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_visual, orient=tk.VERTICAL, command=self.listbox_simple.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox_simple.config(yscrollcommand=scrollbar.set)
    
    def _crear_pestana_lista_doble(self):
        """Crea y configura la pestaña para la lista doblemente enlazada."""
        self.tab_doble = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_doble, text="Lista Doble")
        
        # Frame para controles
        frame_controles = ttk.Frame(self.tab_doble)
        frame_controles.pack(fill=tk.X, pady=5)
        
        # Etiqueta y campo de entrada
        ttk.Label(frame_controles, text="Dato:").pack(side=tk.LEFT, padx=5)
        self.entry_dato_doble = ttk.Entry(frame_controles, width=15)
        self.entry_dato_doble.pack(side=tk.LEFT, padx=5)
        
        # Botones de operaciones
        ttk.Button(frame_controles, text="Insertar inicio", 
                  command=lambda: self._insertar_inicio("doble")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Insertar final", 
                  command=lambda: self._insertar_final("doble")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Eliminar", 
                  command=lambda: self._eliminar("doble")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="Recorrer", 
                  command=lambda: self._recorrer("doble")).pack(side=tk.LEFT, padx=2)
        
        # Frame para visualización
        frame_visual = ttk.Frame(self.tab_doble)
        frame_visual.pack(fill=tk.BOTH, expand=True)
        
        # Listbox para recorrido hacia adelante
        ttk.Label(frame_visual, text="Recorrido hacia adelante:").pack()
        self.listbox_doble_adelante = tk.Listbox(frame_visual)
        self.listbox_doble_adelante.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        # Listbox para recorrido hacia atrás
        ttk.Label(frame_visual, text="Recorrido hacia atrás:").pack()
        self.listbox_doble_atras = tk.Listbox(frame_visual)
        self.listbox_doble_atras.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        # Scrollbar compartida
        scrollbar = ttk.Scrollbar(frame_visual, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configurar scrollbar para ambos listbox
        self.listbox_doble_adelante.config(yscrollcommand=scrollbar.set)
        self.listbox_doble_atras.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self._on_scroll)
    
    def _on_scroll(self, *args):
        """Maneja el evento de scroll para sincronizar ambos listbox de la lista doble."""
        self.listbox_doble_adelante.yview(*args)
        self.listbox_doble_atras.yview(*args)
    
    def _insertar_inicio(self, tipo):
        """Maneja la inserción al inicio para ambos tipos de lista.
        
        Args:
            tipo: Tipo de lista ("simple" o "doble").
        """
        # Obtener el dato del campo de entrada apropiado
        dato = self.entry_dato_simple.get() if tipo == "simple" else self.entry_dato_doble.get()
        
        if not dato:
            messagebox.showwarning("Advertencia", "Por favor ingrese un dato")
            return
        
        if tipo == "simple":
            self.lista_simple.insertar_inicio(dato)
            self._actualizar_listbox_simple()
        else:
            self.lista_doble.insertar_inicio(dato)
            self._actualizar_listbox_doble()
        
        # Limpiar el campo de entrada
        if tipo == "simple":
            self.entry_dato_simple.delete(0, tk.END)
        else:
            self.entry_dato_doble.delete(0, tk.END)
    
    def _insertar_final(self, tipo):
        """Maneja la inserción al final para ambos tipos de lista.
        
        Args:
            tipo: Tipo de lista ("simple" o "doble").
        """
        dato = self.entry_dato_simple.get() if tipo == "simple" else self.entry_dato_doble.get()
        
        if not dato:
            messagebox.showwarning("Advertencia", "Por favor ingrese un dato")
            return
        
        if tipo == "simple":
            self.lista_simple.insertar_final(dato)
            self._actualizar_listbox_simple()
        else:
            self.lista_doble.insertar_final(dato)
            self._actualizar_listbox_doble()
        
        if tipo == "simple":
            self.entry_dato_simple.delete(0, tk.END)
        else:
            self.entry_dato_doble.delete(0, tk.END)
    
    def _eliminar(self, tipo):
        """Maneja la eliminación para ambos tipos de lista.
        
        Args:
            tipo: Tipo de lista ("simple" o "doble").
        """
        dato = self.entry_dato_simple.get() if tipo == "simple" else self.entry_dato_doble.get()
        
        if not dato:
            messagebox.showwarning("Advertencia", "Por favor ingrese un dato")
            return
        
        if tipo == "simple":
            if self.lista_simple.eliminar(dato):
                messagebox.showinfo("Éxito", f"Dato '{dato}' eliminado")
                self._actualizar_listbox_simple()
            else:
                messagebox.showerror("Error", f"Dato '{dato}' no encontrado")
        else:
            if self.lista_doble.eliminar(dato):
                messagebox.showinfo("Éxito", f"Dato '{dato}' eliminado")
                self._actualizar_listbox_doble()
            else:
                messagebox.showerror("Error", f"Dato '{dato}' no encontrado")
        
        if tipo == "simple":
            self.entry_dato_simple.delete(0, tk.END)
        else:
            self.entry_dato_doble.delete(0, tk.END)
    
    def _recorrer(self, tipo):
        """Muestra todos los elementos de la lista en un cuadro de mensaje.
        
        Args:
            tipo: Tipo de lista ("simple" o "doble").
        """
        if tipo == "simple":
            elementos = self.lista_simple.obtener_lista()
            titulo = "Recorrido Lista Simple"
            mensaje = "Elementos en la lista simple:\n\n" + "\n".join(elementos) if elementos else "La lista está vacía"
        else:
            elementos_adelante = self.lista_doble.obtener_lista_adelante()
            elementos_atras = self.lista_doble.obtener_lista_atras()
            titulo = "Recorrido Lista Doble"
            mensaje = "Recorrido hacia adelante:\n" + "\n".join(elementos_adelante) if elementos_adelante else "La lista está vacía"
            mensaje += "\n\nRecorrido hacia atrás:\n" + "\n".join(elementos_atras) if elementos_atras else ""
        
        messagebox.showinfo(titulo, mensaje)
    
    def _actualizar_listbox_simple(self):
        """Actualiza el ListBox de la lista simple con los datos actuales."""
        self.listbox_simple.delete(0, tk.END)
        elementos = self.lista_simple.obtener_lista()
        for elemento in elementos:
            self.listbox_simple.insert(tk.END, elemento)
    
    def _actualizar_listbox_doble(self):
        """Actualiza los ListBox de la lista doble con los datos actuales."""
        self.listbox_doble_adelante.delete(0, tk.END)
        self.listbox_doble_atras.delete(0, tk.END)
        
        elementos_adelante = self.lista_doble.obtener_lista_adelante()
        elementos_atras = self.lista_doble.obtener_lista_atras()
        
        for elemento in elementos_adelante:
            self.listbox_doble_adelante.insert(tk.END, elemento)
        
        for elemento in elementos_atras:
            self.listbox_doble_atras.insert(tk.END, elemento)

if __name__ == "__main__":
    # Punto de entrada principal de la aplicación
    root = tk.Tk()
    app = AplicacionListas(root)
    root.mainloop()