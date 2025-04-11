import tkinter as tk
from tkinter import simpledialog

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
        self.root.title("Árbol Binario - Recorrido Postorden")
        self.canvas = tk.Canvas(self.root, width=1000, height=600, bg="white")
        self.canvas.pack()
        self.nodos_pos = {}

        self.dibujar_arbol(self.arbol.raiz, 500, 50, 200)
        self.dibujar_recorrido_postorden()

        self.root.mainloop()

    def dibujar_arbol(self, nodo, x, y, distancia):
        if nodo is None:
            return

        radio = 20
        self.canvas.create_oval(x-radio, y-radio, x+radio, y+radio, fill="lightyellow")
        self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 12, "bold"))
        self.nodos_pos[nodo.valor] = (x, y)

        if nodo.izquierda:
            x_izq = x - distancia
            y_izq = y + 80
            self.canvas.create_line(x, y+radio, x_izq, y_izq-radio, arrow=tk.LAST)
            self.dibujar_arbol(nodo.izquierda, x_izq, y_izq, distancia//2)

        if nodo.derecha:
            x_der = x + distancia
            y_der = y + 80
            self.canvas.create_line(x, y+radio, x_der, y_der-radio, arrow=tk.LAST)
            self.dibujar_arbol(nodo.derecha, x_der, y_der, distancia//2)

    def dibujar_recorrido_postorden(self):
        recorrido = self.arbol.postorden()
        for i in range(len(recorrido)-1):
            x1, y1 = self.nodos_pos[recorrido[i]]
            x2, y2 = self.nodos_pos[recorrido[i+1]]
            self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="orange", width=2)
            self.canvas.create_text((x1 + x2)//2, (y1 + y2)//2 - 10, text=str(i+1), fill="orange", font=("Arial", 10, "bold"))

        if recorrido:
            print("Recorrido postorden:", recorrido)

# === Programa principal ===
def main():
    arbol = ArbolBinario()

    root = tk.Tk()
    root.withdraw()
    entrada = simpledialog.askstring("Entrada", "Ingresa los valores separados por comas (ej: 8,3,10,1,6,14):")
    if entrada:
        valores = [int(x.strip()) for x in entrada.split(",")]
        for val in valores:
            arbol.insertar(val)

    InterfazGrafica(arbol)

if __name__ == "__main__":
    main()
