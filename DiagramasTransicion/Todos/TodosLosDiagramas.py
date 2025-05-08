import re
import sys

class AnalizadorLexico:
    # Definir los operadores relacionales, números, palabras clave e identificadores
    operadores_relacionales = {"==", "!=", "<", ">", "<=", ">="}
    palabras_clave = {"if", "else", "while", "for", "return"}
    patron_numero = r'^\d+$'  # Para números sin signo
    patron_identificador = r'^[a-zA-Z_][a-zA-Z0-9_]*$'  # Para identificadores

    @staticmethod
    def main():
        print("Ingrese una cadena para analizar:")
        entrada = sys.stdin.readline().strip()
        AnalizadorLexico.analizar_cadena(entrada)

    @staticmethod
    def analizar_cadena(entrada):
        # Usamos expresiones regulares para extraer tokens de manera más inteligente
        tokens = re.findall(r'==|!=|<=|>=|[a-zA-Z_][a-zA-Z0-9_]*|\d+|[<>!=]|\S+', entrada)
        
        for token in tokens:
            resultado = AnalizadorLexico.evaluar_token(token)
            print(f"'{token}' => {resultado}")

    @staticmethod
    def evaluar_token(token):
        if token in AnalizadorLexico.operadores_relacionales:
            return "Operador relacional válido"
        if token in AnalizadorLexico.palabras_clave:
            return "Palabra clave válida"
        if re.fullmatch(AnalizadorLexico.patron_numero, token):
            return "Número sin signo válido"
        if re.fullmatch(AnalizadorLexico.patron_identificador, token):
            return "Identificador válido"
        return "Token inválido"


if __name__ == "__main__":
    AnalizadorLexico.main()