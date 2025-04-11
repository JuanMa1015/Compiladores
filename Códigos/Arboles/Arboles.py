import tkinter as tk
from tkinter import simpledialog, messagebox

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def inorden(self):
        recorrido = []
        self._inorden_recursivo(self.raiz, recorrido)
        return recorrido

    def _inorden_recursivo(self, nodo, recorrido):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, recorrido)
            recorrido.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, recorrido)

    def preorden(self):
        recorrido = []
        self._preorden_recursivo(self.raiz, recorrido)
        return recorrido

    def _preorden_recursivo(self, nodo, recorrido):
        if nodo:
            recorrido.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, recorrido)
            self._preorden_recursivo(nodo.derecha, recorrido)

    def postorden(self):
        recorrido = []
        self._postorden_recursivo(self.raiz, recorrido)
        return recorrido

    def _postorden_recursivo(self, nodo, recorrido):
        if nodo:
            self._postorden_recursivo(nodo.izquierda, recorrido)
            self._postorden_recursivo(nodo.derecha, recorrido)
            recorrido.append(nodo.valor)

class InterfazGrafica:
    def __init__(self, arbol):
        self.arbol = arbol
        self.root = tk.Tk()
        self.root.title("Árbol Binario - Recorridos")
        self.root.geometry("1200x800")
        self.nodos_pos = {}

        self.canvas = tk.Canvas(self.root, width=1200, height=650, bg="white")
        self.canvas.pack()

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Inorden", command=self.mostrar_inorden).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Preorden", command=self.mostrar_preorden).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Postorden", command=self.mostrar_postorden).pack(side=tk.LEFT, padx=10)

        self.dibujar_arbol(self.arbol.raiz, 600, 60, 250)
        self.root.mainloop()

    def dibujar_arbol(self, nodo, x, y, distancia):
        if nodo is None:
            return

        radio = 25
        # Dibuja el nodo
        self.canvas.create_oval(x-radio, y-radio, x+radio, y+radio, fill="#d3e9ff", outline="black")
        self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 12, "bold"))
        self.nodos_pos[nodo.valor] = (x, y)

        # Dibuja la rama izquierda
        if nodo.izquierda:
            x_izq = x - distancia
            y_izq = y + 100
            # Línea desde lateral inferior izquierdo del nodo
            self.canvas.create_line(x - 15, y + radio, x_izq + 15, y_izq - radio, arrow=tk.LAST, width=3)
            self.dibujar_arbol(nodo.izquierda, x_izq, y_izq, distancia // 2)

        # Dibuja la rama derecha
        if nodo.derecha:
            x_der = x + distancia
            y_der = y + 100
            # Línea desde lateral inferior derecho del nodo
            self.canvas.create_line(x + 15, y + radio, x_der - 15, y_der - radio, arrow=tk.LAST, width=3)
            self.dibujar_arbol(nodo.derecha, x_der, y_der, distancia // 2)

    def limpiar_canvas(self):
        self.canvas.delete("all")
        self.nodos_pos.clear()
        self.dibujar_arbol(self.arbol.raiz, 600, 60, 250)

    def dibujar_recorrido(self, recorrido, color):
        recorrido_numerado = ""
        for i, valor in enumerate(recorrido):
            x, y = self.nodos_pos[valor]
            # Dibuja el número debajo del nodo
            self.canvas.create_text(x, y + 35, text=f"{i+1}", fill=color, font=("Arial", 11, "bold"))
            recorrido_numerado += f"{i+1}. {valor}\n"

            # Dibuja flechas del recorrido
            if i < len(recorrido) - 1:
                x2, y2 = self.nodos_pos[recorrido[i + 1]]
                # Apunta desde una posición inferior del nodo hacia una posición lateral del siguiente
                self.canvas.create_line(x, y + 25, x2, y2 - 25, arrow=tk.LAST, fill=color, width=3)

        return recorrido_numerado

    def mostrar_inorden(self):
        self.limpiar_canvas()
        recorrido = self.arbol.inorden()
        enumerado = self.dibujar_recorrido(recorrido, "blue")
        messagebox.showinfo("Recorrido Inorden", f"Recorrido paso a paso:\n\n{enumerado}")
        messagebox.showinfo("Valores Inorden", f"Inorden: {recorrido}")

    def mostrar_preorden(self):
        self.limpiar_canvas()
        recorrido = self.arbol.preorden()
        enumerado = self.dibujar_recorrido(recorrido, "green")
        messagebox.showinfo("Recorrido Preorden", f"Recorrido paso a paso:\n\n{enumerado}")
        messagebox.showinfo("Valores Preorden", f"Preorden: {recorrido}")

    def mostrar_postorden(self):
        self.limpiar_canvas()
        recorrido = self.arbol.postorden()
        enumerado = self.dibujar_recorrido(recorrido, "orange")
        messagebox.showinfo("Recorrido Postorden", f"Recorrido paso a paso:\n\n{enumerado}")
        messagebox.showinfo("Valores Postorden", f"Postorden: {recorrido}")

# === Programa principal ===
def main():
    arbol = ArbolBinario()
    root = tk.Tk()
    root.withdraw()

    entrada = simpledialog.askstring("Entrada", "Ingresa los valores separados por comas (ej: 8,3,10,1,6,14):")
    if entrada:
        try:
            valores = [int(x.strip()) for x in entrada.split(",")]
            for val in valores:
                arbol.insertar(val)
            InterfazGrafica(arbol)
        except ValueError:
            messagebox.showerror("Error", "Asegúrate de ingresar solo números separados por comas.")

if __name__ == "__main__":
    main()
