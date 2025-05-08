def evaluar_token(token):
    estado = 0
    for c in token:
        if estado == 0:
            if c in [' ', '\t', '\n', '\r']:
                estado = 1
            else:
                return "Token inválido"
        elif estado == 1:
            if c in [' ', '\t', '\n', '\r']:
                estado = 1
            else:
                return "Token inválido"
    return "Espacio en blanco" if estado == 1 else "Token inválido"

def analizar_cadena(entrada):
    tokens_analizados = []
    current_token = ""

    for c in entrada:
        if c in [' ', '\t', '\n', '\r']:
            if current_token:
                resultado = evaluar_token(current_token)
                tokens_analizados.append((current_token, resultado))
                current_token = ""
            current_token += c
        else:
            if current_token:
                resultado = evaluar_token(current_token)
                tokens_analizados.append((current_token, resultado))
                current_token = ""
            current_token += c

    if current_token:
        resultado = evaluar_token(current_token)
        tokens_analizados.append((current_token, resultado))

    return tokens_analizados

def main():
    print("Analizador de espacios en blanco. Escribe 'salir' para terminar.")
    while True:
        entrada = input("\nIngrese una cadena para analizar:\n")
        if entrada.lower() == "salir":
            print("Programa finalizado.")
            break

        tokens_analizados = analizar_cadena(entrada)
        print("\nResultados del análisis:")
        for token, resultado in tokens_analizados:
            print(f"'{token}' => {resultado}")

if __name__ == "__main__":
    main()
