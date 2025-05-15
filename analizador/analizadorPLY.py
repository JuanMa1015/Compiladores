import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from tkinter import messagebox

# === 1. DEFINICIÓN DEL ANALIZADOR LÉXICO ===
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'EQUAL'
)

# Definimos las expresiones regulares para cada token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'='

def t_NUMBER(t):
    r'\d+(\.\d*)?'  # Números enteros o flotantes
    t.value = float(t.value)
    return t

# Caracteres que vamos a ignorar (espacios y saltos de línea)
t_ignore = ' \t\n'

# Definir la regla para manejar los errores en el análisis léxico
def t_error(t):
    print(f"Carácter no reconocido {t.value[0]}")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()

# === 2. DEFINICIÓN DEL ANALIZADOR SINTÁCTICO ===

# Definimos la gramática
def p_expression_binop(p):
    '''expression : expression PLUS expression
        | expression MINUS expression
        | expression TIMES expression
        | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            raise ValueError("Error: División por cero.")
        p[0] = p[1] / p[3]

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

# Regla de error
def p_error(p):
    print("Error de sintaxis: Expresión no válida.")

# Crear el parser
parser = yacc.yacc()

# === 3. FUNCIONES DE EVALUACIÓN ===
def evaluar_expresion(expresion):
    lexer.input(expresion)
    return parser.parse(expresion)

# === 4. INTERFAZ GRÁFICA DE USUARIO ===

def on_calcular():
    expresion = entry.get()
    try:
        resultado = evaluar_expresion(expresion)
        resultado_label.config(text=f"Resultado: {resultado}", fg="white", bg="#4CAF50")
    except Exception as e:
        messagebox.showerror("Error", f"Error al evaluar la expresión: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Matemática")

# Establecer un color de fondo atractivo
root.config(bg="#1E2A47")

# Establecer un tamaño mínimo
root.minsize(400, 400)

# Crear el campo de entrada para la expresión
entry_label = tk.Label(root, text="Ingresa una expresión matemática:",
font=("Arial", 14), fg="#ffffff", bg="#1E2A47")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 16), bd=5, relief="solid", justify="center")
entry.pack(pady=10)

# Botón para calcular la expresión
calcular_button = tk.Button(root, text="Calcular", command=on_calcular, font=("Arial", 16),
                            bg="#4CAF50", fg="white", bd=0, relief="solid", width=15)
calcular_button.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="Resultado: ", font=("Arial", 16), fg="white", bg="#1E2A47")
resultado_label.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
