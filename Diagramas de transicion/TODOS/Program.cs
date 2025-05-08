using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text.RegularExpressions;

class AnalizadorLexico
{
    static readonly HashSet<string> operadoresRelacionales = new HashSet<string> { "==", "!=", "<", ">", "<=", ">=" };
    static readonly HashSet<string> palabrasClave = new HashSet<string> { "if", "else", "while", "for", "return" };
    static readonly string patronNumero = @"^\d+$";
    static readonly string patronIdentificador = @"^[a-zA-Z_][a-zA-Z0-9_]*$";

    static int contadorEspacios = 0;
    static int contadorTabulaciones = 0;
    static int contadorPalabrasClave = 0;
    static int contadorOperadoresRelacionales = 0;
    static int contadorNumeros = 0;
    static int contadorIdentificadores = 0;

    static void Main()
    {
        Console.WriteLine("Ingrese varias líneas de código (deje una línea vacía para terminar):");

        string linea;
        List<string> lineasEntrada = new List<string>();
        while ((linea = Console.ReadLine()) != null && linea != "")
        {
            lineasEntrada.Add(linea);
        }

        string entradaCompleta = string.Join("\n", lineasEntrada);
        AnalizarCadena(entradaCompleta);
    }

    public static void AnalizarCadena(string entrada)
    {
        // Contar espacios y tabulaciones
        contadorEspacios = Regex.Matches(entrada, " ").Count;
        contadorTabulaciones = Regex.Matches(entrada, "\t").Count;

        Console.WriteLine($"Espacios encontrados: {contadorEspacios}");
        Console.WriteLine($"Tabulaciones encontradas: {contadorTabulaciones}");

        // Tokenización más robusta: incluye delimitadores comunes
        string[] tokens = entrada.Split(new[] { ' ', '\t', '\n', '\r', ';', ',', '(', ')', '{', '}', '[', ']' }, StringSplitOptions.RemoveEmptyEntries);
        List<(string Token, string Resultado)> tokensAnalizados = new List<(string Token, string Resultado)>();

        foreach (var token in tokens)
        {
            string resultado = EvaluarToken(token);
            Console.WriteLine($"{token} => {resultado}");
            tokensAnalizados.Add((token, resultado));
        }

        // Mostrar conteo
        Console.WriteLine("\nResumen:");
        Console.WriteLine($"Palabras clave encontradas: {contadorPalabrasClave}");
        Console.WriteLine($"Operadores relacionales encontrados: {contadorOperadoresRelacionales}");
        Console.WriteLine($"Números válidos encontrados: {contadorNumeros}");
        Console.WriteLine($"Identificadores válidos encontrados: {contadorIdentificadores}");

        // Generar archivo .dot como antes
        CrearArchivoDotGlobal("diagrama_transiciones.dot", tokensAnalizados);
    }

    private static string EvaluarToken(string token)
    {
        if (operadoresRelacionales.Contains(token))
        {
            contadorOperadoresRelacionales++;
            return "Operador relacional válido";
        }

        if (palabrasClave.Contains(token))
        {
            contadorPalabrasClave++;
            return "Palabra clave válida";
        }

        if (Regex.IsMatch(token, patronNumero))
        {
            contadorNumeros++;
            return "Número sin signo válido";
        }

        if (Regex.IsMatch(token, patronIdentificador))
        {
            contadorIdentificadores++;
            return "Identificador válido";
        }

        return "Token inválido";
    }

    public static void CrearArchivoDotGlobal(string nombreArchivo, List<(string Token, string Resultado)> tokensAnalizados)
    {
        using (StreamWriter writer = new StreamWriter(nombreArchivo))
        {
            writer.WriteLine("digraph automata {");
            writer.WriteLine("    rankdir=LR;");
            writer.WriteLine("    size=\"10,5\";");
            writer.WriteLine("    node [shape = circle, style=filled, fillcolor=white];");

            writer.WriteLine("    S0 [label=\"S0\"]");
            writer.WriteLine("    S1 [label=\"S1\"]");
            writer.WriteLine("    ERROR [shape=doublecircle, color=red, fillcolor=mistyrose, label=\"ERROR\"]");
            writer.WriteLine("    S1 [shape=doublecircle, color=green, fillcolor=lightgreen]");

            writer.WriteLine("    S0 -> S1 [label=\"Palabra clave, Identificador, Número, Operador\", color=gray]");

            string[] colores = { "blue", "orange", "green", "purple", "brown", "cyan" };

            for (int i = 0; i < tokensAnalizados.Count; i++)
            {
                var (token, resultado) = tokensAnalizados[i];
                string color = colores[i % colores.Length];

                if (resultado.Contains("válido"))
                {
                    writer.WriteLine($"    S0 -> S1 [label=\"{token}\", color={color}, penwidth=2.0]");
                }
                else
                {
                    writer.WriteLine($"    S0 -> ERROR [label=\"{token}\", color={color}, penwidth=2.0]");
                }
            }

            writer.WriteLine("    labelloc=\"t\";");
            writer.WriteLine("    label=\"Tokens procesados: ");
            foreach (var (token, resultado) in tokensAnalizados)
            {
                writer.WriteLine($"  {token} => {resultado}\\n");
            }
            writer.WriteLine("\";");
            writer.WriteLine("}");
        }
    }
}
