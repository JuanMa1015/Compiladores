import tkinter as tk
from tkinter import messagebox

# Función para convertir infija a postfija (con actualización en la interfaz)
def infija_a_postfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    salida = []  # Aquí guardaremos el resultado final
    pila = []  # Pila para manejar los operadores
    tokens = list(expresion.replace(" ", ""))  # Separamos cada elemento

    # Limpiamos la caja de texto antes de empezar
    pasos_texto.delete("1.0", tk.END)

    for token in tokens:
        if token.isalnum():  # Si es un número o una variable
            salida.append(token)
            pasos_texto.insert(tk.END, f"Agregado a la salida: {token}\n")
        elif token in precedencia:  # Si es un operador
            while pila and pila[-1] != '(' and precedencia.get(pila[-1], 0) >= precedencia[token]:
                salida.append(pila.pop())  # Sacamos operadores con mayor prioridad
                pasos_texto.insert(tk.END, f"Operador sacado y agregado a la salida\n")
            pila.append(token)  # Ponemos el operador actual en la pila
            pasos_texto.insert(tk.END, f"Operador {token} agregado a la pila\n")
        elif token == '(':
            pila.append(token)
            pasos_texto.insert(tk.END, "Paréntesis de apertura agregado a la pila\n")
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())  # Sacamos operadores hasta encontrar '('
                pasos_texto.insert(tk.END, "Operador sacado y agregado a la salida\n")
            pila.pop()  # Quitamos el '(' de la pila
            pasos_texto.insert(tk.END, "Paréntesis de apertura eliminado de la pila\n")

        # 🔹 Mostramos el estado actual después de cada paso
        pasos_texto.insert(tk.END, f"Salida actual: {' '.join(salida)}\n")
        pasos_texto.insert(tk.END, f"Pila actual: {pila}\n\n")
        ventana.update()  # 🔹 Actualiza la interfaz en cada paso

    while pila:  # Al final, vaciamos la pila
        salida.append(pila.pop())
        pasos_texto.insert(tk.END, f"Operador final sacado y agregado a la salida\n")
        pasos_texto.insert(tk.END, f"Salida actual: {' '.join(salida)}\n")
        pasos_texto.insert(tk.END, f"Pila actual: {pila}\n\n")
        ventana.update()

    return " ".join(salida)


# Función para convertir postfija a infija (con actualización en la interfaz)
def postfija_a_infija(expresion):
    pila = []
    tokens = expresion.split()

    # Limpiamos la caja de texto antes de empezar
    pasos_texto.delete("1.0", tk.END)

    for token in tokens:
        if token.isalnum():  # Si es un número o variable, lo agregamos a la pila
            pila.append(token)
            pasos_texto.insert(tk.END, f"Operando {token} agregado a la pila\n")
        elif token in "+-*/^":  # Si es un operador
            if len(pila) < 2:
                messagebox.showerror("Error", "Expresión postfija inválida")
                return ""
            b = pila.pop()
            a = pila.pop()
            nueva_expr = f"({a} {token} {b})"
            pila.append(nueva_expr)
            pasos_texto.insert(tk.END, f"Se combinaron '{a}' y '{b}' con operador '{token}' -> {nueva_expr}\n")

        # 🔹 Mostramos el estado actual después de cada paso
        pasos_texto.insert(tk.END, f"Pila actual: {pila}\n\n")
        ventana.update()

    if len(pila) != 1:
        messagebox.showerror("Error", "Expresión postfija inválida")
        return ""

    return pila[0]


# Función para convertir la expresión ingresada a postfija y mostrar los pasos
def convertir_a_postfija():
    expresion = entrada.get()
    if not expresion:
        messagebox.showerror("Error", "Ingrese una expresión")
        return
    resultado = infija_a_postfija(expresion)
    resultado_label.config(text=f"Postfija: {resultado}")


# Función para convertir la expresión ingresada a infija y mostrar los pasos
def convertir_a_infija():
    expresion = entrada.get()
    if not expresion:
        messagebox.showerror("Error", "Ingrese una expresión")
        return
    resultado = postfija_a_infija(expresion)
    if resultado:
        resultado_label.config(text=f"Infija: {resultado}")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor Infija ↔ Postfija")
ventana.geometry("600x500")

# Entrada de expresión
tk.Label(ventana, text="Ingrese expresión:").pack()
entrada = tk.Entry(ventana, width=40)
entrada.pack()

# Botones de conversión
tk.Button(ventana, text="A Postfija", command=convertir_a_postfija).pack()
tk.Button(ventana, text="A Infija", command=convertir_a_infija).pack()

# Etiqueta de resultado
resultado_label = tk.Label(ventana, text="Resultado: ")
resultado_label.pack()

# Cuadro de texto para mostrar pasos
pasos_texto = tk.Text(ventana, height=20, width=70)
pasos_texto.pack()

ventana.mainloop()
