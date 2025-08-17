import sympy as sp
from sympy import symbols, integrate, sqrt, cos, sin, exp, log, pi, oo
from sympy.parsing.sympy_parser import parse_expr
import re

def limpiar_expresion(expr_str):
    """
    Limpia y prepara la expresión para SymPy
    """
    # Reemplazos comunes
    expr_str = expr_str.replace('^', '**')  # Potencias
    expr_str = expr_str.replace('√', 'sqrt')  # Raíz cuadrada
    expr_str = expr_str.replace('sen', 'sin')  # Seno en español
    expr_str = expr_str.replace('tg', 'tan')  # Tangente
    expr_str = expr_str.replace('ln', 'log')  # Logaritmo natural
    expr_str = expr_str.replace('e^', 'exp(') # Exponencial
    
    # Contar paréntesis para e^
    if 'exp(' in expr_str and expr_str.count('exp(') > expr_str.count(')'):
        expr_str += ')'
    
    return expr_str

def resolver_integral_predefinida(opcion):
    """
    Resuelve las integrales específicas de la tarea
    """
    x = symbols('x')
    
    integrales = {
        'a': 1 + x,
        'b': x * sqrt(x),
        'c': (sqrt(x) - x**3 * exp(x) + x**2) / x**3,
        'd': 4*cos(x) - 1/cos(x)**2,
        'e': (1 + x**2) / sqrt(x),
        'f': 3*x**4 + 5*x**9,
        'g': (1 - x**5) / (1 - x),
        'h': (1 - sqrt(x))**2,
        'i': (x**3 - 2*x**2 + 4*x) / x,
        'j': 2*sqrt(x) - 3*x**(1/3) - x**4,
        'k': (1 - sqrt(x)*exp(x)) / sqrt(x)
    }
    
    if opcion.lower() in integrales:
        expr = integrales[opcion.lower()]
        return expr
    return None

def mostrar_integrales_disponibles():
    """
    Muestra las integrales de la tarea disponibles
    """
    print("\n=== INTEGRALES DE LA TAREA DISPONIBLES ===")
    opciones = {
        'a': '∫(1 + x) dx',
        'b': '∫x√x dx',
        'c': '∫(√x - x³eˣ + x²)/x³ dx',
        'd': '∫(4cos(x) - 1/cos²(x)) dx',
        'e': '∫(1 + x²)/√x dx',
        'f': '∫(3x⁴ + 5x⁹) dx',
        'g': '∫(1 - x⁵)/(1 - x) dx',
        'h': '∫(1 - √x)² dx',
        'i': '∫(x³ - 2x² + 4x)/x dx',
        'j': '∫(2√x - ³√x - x⁴) dx',
        'k': '∫(1 - √x·eˣ)/√x dx'
    }
    
    for letra, integral in opciones.items():
        print(f"{letra}) {integral}")

def main():
    print("🧮 CALCULADORA DE INTEGRALES SIMBÓLICAS")
    print("=" * 50)
    
    x = symbols('x')
    
    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Resolver integral de la tarea (a-k)")
        print("2. Ingresar integral personalizada")
        print("3. Ver todas las integrales de la tarea")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ").strip()
        
        if opcion == '1':
            mostrar_integrales_disponibles()
            letra = input("\n¿Cuál integral quieres resolver? (a-k): ").strip()
            
            expr = resolver_integral_predefinida(letra)
            if expr:
                print(f"\nResolviendo integral {letra.upper()}...")
                print(f"Expresión: {expr}")
                
                try:
                    resultado = integrate(expr, x)
                    print(f"\n✅ RESULTADO:")
                    print(f"∫({expr}) dx = {resultado} + C")
                    
                    # Mostrar resultado simplificado si es posible
                    resultado_simplificado = sp.simplify(resultado)
                    if resultado != resultado_simplificado:
                        print(f"Simplificado: {resultado_simplificado} + C")
                        
                except Exception as e:
                    print(f"❌ Error al resolver: {e}")
            else:
                print("❌ Opción inválida. Usa letras de 'a' a 'k'.")
        
        elif opcion == '2':
            print("\n📝 INTEGRAL PERSONALIZADA")
            print("Ejemplo de formato: 'x**2 + sin(x)' o '1/(x**2 + 1)'")
            print("Usa: ** para potencias, sqrt() para raíz, sin(), cos(), exp(), log()")
            
            expr_input = input("\nIngresa la expresión a integrar: ").strip()
            
            if expr_input:
                try:
                    # Limpiar y parsear la expresión
                    expr_limpia = limpiar_expresion(expr_input)
                    expr = parse_expr(expr_limpia)
                    
                    print(f"\nExpresión interpretada: {expr}")
                    print("Resolviendo...")
                    
                    resultado = integrate(expr, x)
                    print(f"\n✅ RESULTADO:")
                    print(f"∫({expr}) dx = {resultado} + C")
                    
                    # Mostrar resultado simplificado
                    resultado_simplificado = sp.simplify(resultado)
                    if resultado != resultado_simplificado:
                        print(f"Simplificado: {resultado_simplificado} + C")
                    
                except Exception as e:
                    print(f"❌ Error al procesar la expresión: {e}")
                    print("Verifica la sintaxis. Ejemplos válidos:")
                    print("- x**2 + 1")
                    print("- sin(x)*cos(x)")
                    print("- sqrt(x)")
                    print("- exp(x)")
        
        elif opcion == '3':
            mostrar_integrales_disponibles()
        
        elif opcion == '4':
            print("\n👋 ¡Hasta luego! Que tengas éxito en tu tarea.")
            break
        
        else:
            print("❌ Opción inválida. Por favor elige 1, 2, 3 o 4.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    # Verificar si SymPy está instalado
    try:
        import sympy
        main()
    except ImportError:
        print("❌ Error: SymPy no está instalado.")
        print("Para instalarlo ejecuta: pip install sympy")