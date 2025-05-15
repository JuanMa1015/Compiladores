import argparse

def suma(x, y, z):
    return x + y + z

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("No se puede dividir entre cero.")
    return x / y

def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de línea de comandos: suma, resta, multiplicación y división."
    )

    parser.add_argument("operacion", choices=["suma", "resta", "multiplicacion", "division"],
                        help="Operación a realizar.")
    parser.add_argument("x", type=float, help="Primer número.")
    parser.add_argument("y", type=float, help="Segundo número.")
    parser.add_argument("z", type=float, help="Tercer número.")

    args = parser.parse_args()

    if args.operacion == "suma":
        resultado = suma(args.x, args.y, args.z)
    elif args.operacion == "resta":
        resultado = resta(args.x, args.y)
    elif args.operacion == "multiplicacion":
        resultado = multiplicacion(args.x, args.y)
    elif args.operacion == "division":
        try:
            resultado = division(args.x, args.y)
        except ValueError as e:
            print(f"Error: {e}")
            return

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()

#¿Cómo ejecutar?
#python Calculadora.py <operacion> <x> <y>
#Ejemplo:
# python Calculadora.py suma 5 3