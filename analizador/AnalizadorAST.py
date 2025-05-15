import ast
import tkinter as tk
from tkinter import messagebox, scrolledtext

# === Tokens ===
NUMBER, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, ASSIGN, ID, EOF = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'ASSIGN', 'ID', 'EOF'
)

# === Lexer ===
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def identifier(self):
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return (NUMBER, self.number())
            if self.current_char.isalpha() or self.current_char == '_':
                return (ID, self.identifier())
            if self.current_char == '+':
                self.advance()
                return (PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return (MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return (TIMES, '*')
            if self.current_char == '/':
                self.advance()
                return (DIVIDE, '/')
            if self.current_char == '(':
                self.advance()
                return (LPAREN, '(')
            if self.current_char == ')':
                self.advance()
                return (RPAREN, ')')
            if self.current_char == '=':
                self.advance()
                return (ASSIGN, '=')

            raise Exception(f'Carácter no válido: {self.current_char}')
        return (EOF, None)

# === Parser ===
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f'Error de sintaxis: se esperaba {token_type}, se recibió {self.current_token[0]}')

    def factor(self):
        token_type, value = self.current_token
        if token_type == NUMBER:
            self.eat(NUMBER)
            return ast.Constant(value=value)
        elif token_type == ID:
            self.eat(ID)
            return ast.Name(id=value, ctx=ast.Load())
        elif token_type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            raise Exception(f'Factor inesperado {token_type}')

    def term(self):
        node = self.factor()
        while self.current_token[0] in (TIMES, DIVIDE):
            token_type = self.current_token[0]
            self.eat(token_type)
            right = self.factor()
            op = ast.Mult() if token_type == TIMES else ast.Div()
            node = ast.BinOp(left=node, op=op, right=right)
        return node

    def expr(self):
        node = self.term()
        while self.current_token[0] in (PLUS, MINUS):
            token_type = self.current_token[0]
            self.eat(token_type)
            right = self.term()
            op = ast.Add() if token_type == PLUS else ast.Sub()
            node = ast.BinOp(left=node, op=op, right=right)
        return node

    def assignment(self):
        if self.current_token[0] == ID:
            var_name = self.current_token[1]
            self.eat(ID)
            if self.current_token[0] == ASSIGN:
                self.eat(ASSIGN)
                value = self.expr()
                return ast.Assign(
                    targets=[ast.Name(id=var_name, ctx=ast.Store())],
                    value=value
                )
            else:
                # No era asignación, tratamos el identificador como parte de una expresión
                left = ast.Name(id=var_name, ctx=ast.Load())
                return self.expr_rest(left)
        else:
            return self.expr()

    def expr_rest(self, left):
        while self.current_token[0] in (PLUS, MINUS):
            token_type = self.current_token[0]
            self.eat(token_type)
            right = self.term()
            op = ast.Add() if token_type == PLUS else ast.Sub()
            left = ast.BinOp(left=left, op=op, right=right)
        return left

    def parse(self):
        node = self.assignment()
        return ast.Expression(body=node)

# === Función del botón ===
def analizar_expresion():
    entrada = entry.get()
    try:
        lexer = Lexer(entrada)
        parser = Parser(lexer)
        tree = parser.parse()
        resultado = ast.dump(tree, indent=4)
        salida.config(state='normal')
        salida.delete(1.0, tk.END)
        salida.insert(tk.END, resultado)
        salida.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error de análisis", str(e))

# === Interfaz gráfica ===
ventana = tk.Tk()
ventana.title("Analizador Sintáctico - AST Visualizer")
ventana.geometry("700x500")
ventana.config(bg="#e0f7fa")

titulo = tk.Label(ventana, text="Analizador Descendente Recursivo", font=("Helvetica", 18, "bold"), bg="#00acc1", fg="white", pady=10)
titulo.pack(fill=tk.X)

frame_input = tk.Frame(ventana, bg="#e0f7fa")
frame_input.pack(pady=20)

lbl = tk.Label(frame_input, text="Expresión:", font=("Helvetica", 12), bg="#e0f7fa")
lbl.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame_input, width=40, font=("Consolas", 14), bd=2, relief="groove")
entry.grid(row=0, column=1, padx=5)

btn = tk.Button(frame_input, text="Analizar", font=("Helvetica", 12), bg="#00796b", fg="white", padx=20, command=analizar_expresion)
btn.grid(row=0, column=2, padx=5)

salida = scrolledtext.ScrolledText(ventana, width=80, height=20, font=("Courier New", 10), bg="#f1f8e9", state='disabled')
salida.pack(padx=10, pady=10)

ventana.mainloop()
