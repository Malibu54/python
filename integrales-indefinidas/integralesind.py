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
    
    # Ejercicio 1 - Integrales inmediatas
    integrales_ej1 = {
        '1a': 1 + x,
        '1b': x * sqrt(x),
        '1c': (sqrt(x) - x**3 * exp(x) + x**2) / x**3,
        '1d': 4*cos(x) - 1/cos(x)**2,
        '1e': (1 + x**2) / sqrt(x),
        '1f': 3*x**4 + 5*x**9,
        '1g': (1 - x**5) / (1 - x),
        '1h': (1 - sqrt(x))**2,
        '1i': (x**3 - 2*x**2 + 4*x) / x,
        '1j': 2*sqrt(x) - 3*x**(1/3) - x**4,
        '1k': (1 - sqrt(x)*exp(x)) / sqrt(x)
    }
    
    # Ejercicio 2 - Integrales por sustitución
    integrales_ej2 = {
        '2a': (2*x**4) / (x**5 + 3),
        '2b': (x**5 + 7)**8 * 5*x**4,
        '2c': (3*x + 1) / sqrt(9*x**2 + 6*x + 2),
        '2d': exp(1/x) / x**2,
        '2e': 5 / (x * log(x)**2),
        '2f': (x**2 + 1) / (x**3 + 3*x),
        '2g': (log(x))**(-2) * (1/x),
        '2h': 1 / (x * log(2*x)**2),
        '2i': (x**2 + x)**2 * (2*x + 1),
        '2j': (x - 3) / sqrt(9 - 18*x + 3*x**2),
        '2k': (2*x - 1) / sqrt(5 + 4*x - 4*x**2),
        '2l': x * sqrt(1 + 4*x**2),
        '2m': x**3 * sqrt(x**4 + 3),
        '2n': exp(-x**2) * x**2,
        '2o': 2*x * sqrt(x**2 + 29),
        '2p': log(x + 1) / (x + 1)
    }
    
    # Combinar ambos diccionarios
    todas_integrales = {**integrales_ej1, **integrales_ej2}
    
    # También mantener compatibilidad con formato anterior (solo letras)
    integrales_compatibilidad = {
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
    
    todas_integrales.update(integrales_compatibilidad)
    
    if opcion.lower() in todas_integrales:
        expr = todas_integrales[opcion.lower()]
        return expr
    return None

def mostrar_integrales_disponibles():
    """
    Muestra las integrales de la tarea disponibles
    """
    print("\n=== EJERCICIO 1: INTEGRALES INMEDIATAS ===")
    opciones_ej1 = {
        '1a': '∫(1 + x) dx',
        '1b': '∫x√x dx', 
        '1c': '∫(√x - x³eˣ + x²)/x³ dx',
        '1d': '∫(4cos(x) - 1/cos²(x)) dx',
        '1e': '∫(1 + x²)/√x dx',
        '1f': '∫(3x⁴ + 5x⁹) dx',
        '1g': '∫(1 - x⁵)/(1 - x) dx',
        '1h': '∫(1 - √x)² dx',
        '1i': '∫(x³ - 2x² + 4x)/x dx',
        '1j': '∫(2√x - ³√x - x⁴) dx',
        '1k': '∫(1 - √x·eˣ)/√x dx'
    }
    
    for codigo, integral in opciones_ej1.items():
        print(f"{codigo}) {integral}")
    
    print("\n=== EJERCICIO 2: INTEGRALES POR SUSTITUCIÓN ===")
    opciones_ej2 = {
        '2a': '∫(2x⁴)/(x⁵ + 3) dx',
        '2b': '∫(x⁵ + 7)⁸ · 5x⁴ dx',
        '2c': '∫(3x + 1)/√(9x² + 6x + 2) dx',
        '2d': '∫e^(1/x)/x² dx',
        '2e': '∫5/(x·ln²(x)) dx',
        '2f': '∫(x² + 1)/(x³ + 3x) dx',
        '2g': '∫(ln(x))⁻² · (1/x) dx',
        '2h': '∫1/(x·ln²(2x)) dx',
        '2i': '∫(x² + x)² · (2x + 1) dx',
        '2j': '∫(x - 3)/√(9 - 18x + 3x²) dx',
        '2k': '∫(2x - 1)/√(5 + 4x - 4x²) dx',
        '2l': '∫x·√(1 + 4x²) dx',
        '2m': '∫x³·√(x⁴ + 3) dx',
        '2n': '∫e^(-x²)·x² dx',
        '2o': '∫2x·√(x² + 29) dx',
        '2p': '∫ln(x + 1)/(x + 1) dx'
    }
    
    for codigo, integral in opciones_ej2.items():
        print(f"{codigo}) {integral}")
    
    print("\n💡 También puedes usar solo la letra para el Ejercicio 1:")
    print("   Ejemplo: 'a' = '1a', 'b' = '1b', etc.")

def main():
    print("🧮 CALCULADORA DE INTEGRALES SIMBÓLICAS")
    print("=" * 50)
    
    x = symbols('x')
    
    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Resolver integral de la tarea (Ejercicio 1: a-k, Ejercicio 2: 2a-2p)")
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