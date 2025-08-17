import sympy as sp
import numpy as np
from sympy import symbols, integrate, diff, solve, limit, series, exp, sin, cos, ln, sqrt, oo, pi
from sympy.abc import x, y, z, t, n, q, p
import matplotlib.pyplot as plt

class CalculadoraAnalisisII:
    """
    Calculadora para resolver ejercicios de Análisis Matemático II
    Incluye: Integrales, Ecuaciones Diferenciales, Funciones Multivariables, Series
    """
    
    def __init__(self):
        self.x = sp.Symbol('x')
        self.y = sp.Symbol('y')
        self.z = sp.Symbol('z')
        self.q = sp.Symbol('q')
        self.p = sp.Symbol('p')
        
    # ============= INTEGRALES INDEFINIDAS =============
    
    def integral_indefinida(self, expresion_str):
        """Calcula integral indefinida"""
        try:
            expr = sp.sympify(expresion_str)
            resultado = sp.integrate(expr, self.x)
            return f"∫ {expr} dx = {resultado} + C"
        except Exception as e:
            return f"Error: {e}"
    
    def integral_sustitucion(self, expresion_str, u_str, du_dx_str):
        """Resuelve integral por sustitución"""
        try:
            expr = sp.sympify(expresion_str)
            u = sp.sympify(u_str)
            du_dx = sp.diff(u, self.x)
            
            # Intentar expresar la integral en términos de u
            resultado = sp.integrate(expr, self.x)
            return f"Con u = {u}, du = {du_dx}dx\n∫ {expr} dx = {resultado} + C"
        except Exception as e:
            return f"Error: {e}"
    
    def integral_por_partes(self, u_str, dv_str):
        """Resuelve integral por partes: ∫u dv = uv - ∫v du"""
        try:
            u = sp.sympify(u_str)
            dv = sp.sympify(dv_str)
            
            du = sp.diff(u, self.x)
            v = sp.integrate(dv, self.x)
            
            resultado = u * v - sp.integrate(v * du, self.x)
            return f"u = {u}, dv = {dv}dx\ndu = {du}dx, v = {v}\n∫ u dv = {resultado} + C"
        except Exception as e:
            return f"Error: {e}"
    
    # ============= INTEGRALES DEFINIDAS =============
    
    def integral_definida(self, expresion_str, a, b):
        """Calcula integral definida entre a y b"""
        try:
            expr = sp.sympify(expresion_str)
            resultado = sp.integrate(expr, (self.x, a, b))
            return f"∫[{a},{b}] {expr} dx = {resultado} = {float(resultado):.4f}"
        except Exception as e:
            return f"Error: {e}"
    
    def area_entre_curvas(self, f1_str, f2_str, a=None, b=None):
        """Calcula el área entre dos curvas"""
        try:
            f1 = sp.sympify(f1_str)
            f2 = sp.sympify(f2_str)
            
            # Encontrar puntos de intersección si no se dan límites
            if a is None or b is None:
                intersecciones = sp.solve(f1 - f2, self.x)
                if len(intersecciones) >= 2:
                    a = min(intersecciones)
                    b = max(intersecciones)
                else:
                    return "No se encontraron suficientes puntos de intersección"
            
            # Calcular el área
            area = sp.integrate(sp.Abs(f1 - f2), (self.x, a, b))
            return f"Área entre {f1} y {f2} desde x={a} hasta x={b}: {area} u.A."
        except Exception as e:
            return f"Error: {e}"
    
    # ============= ECUACIONES DIFERENCIALES =============
    
    def ecuacion_diferencial_separable(self, ec_str, condicion_inicial=None):
        """Resuelve EDO de variables separables"""
        try:
            y_func = sp.Function('y')
            eq = sp.sympify(ec_str)
            
            # Resolver la ecuación diferencial
            if condicion_inicial:
                x0, y0 = condicion_inicial
                solucion = sp.dsolve(eq, y_func(self.x), ics={y_func(x0): y0})
                return f"Solución particular: {solucion}"
            else:
                solucion = sp.dsolve(eq, y_func(self.x))
                return f"Solución general: {solucion}"
        except Exception as e:
            return f"Error: {e}"
    
    # ============= FUNCIONES MULTIVARIABLES =============
    
    def derivada_parcial(self, funcion_str, variable='x'):
        """Calcula derivada parcial respecto a una variable"""
        try:
            f = sp.sympify(funcion_str)
            var = self.x if variable == 'x' else self.y if variable == 'y' else self.z
            derivada = sp.diff(f, var)
            return f"∂f/∂{variable} = {derivada}"
        except Exception as e:
            return f"Error: {e}"
    
    def gradiente(self, funcion_str):
        """Calcula el gradiente de una función"""
        try:
            f = sp.sympify(funcion_str)
            grad_x = sp.diff(f, self.x)
            grad_y = sp.diff(f, self.y)
            return f"∇f = ({grad_x}, {grad_y})"
        except Exception as e:
            return f"Error: {e}"
    
    def puntos_criticos(self, funcion_str):
        """Encuentra puntos críticos de una función de dos variables"""
        try:
            f = sp.sympify(funcion_str)
            
            # Derivadas parciales
            fx = sp.diff(f, self.x)
            fy = sp.diff(f, self.y)
            
            # Resolver sistema fx = 0, fy = 0
            puntos = sp.solve([fx, fy], [self.x, self.y])
            
            if not puntos:
                return "No se encontraron puntos críticos"
            
            # Clasificar puntos usando el criterio de la segunda derivada
            fxx = sp.diff(fx, self.x)
            fyy = sp.diff(fy, self.y)
            fxy = sp.diff(fx, self.y)
            
            resultado = f"Puntos críticos de f = {f}:\n"
            for punto in puntos if isinstance(puntos, list) else [puntos]:
                x_val = punto[self.x] if isinstance(punto, dict) else punto[0]
                y_val = punto[self.y] if isinstance(punto, dict) else punto[1]
                
                # Evaluar en el punto
                D = fxx.subs([(self.x, x_val), (self.y, y_val)]) * \
                    fyy.subs([(self.x, x_val), (self.y, y_val)]) - \
                    fxy.subs([(self.x, x_val), (self.y, y_val)])**2
                
                if D > 0:
                    if fxx.subs([(self.x, x_val), (self.y, y_val)]) > 0:
                        tipo = "Mínimo"
                    else:
                        tipo = "Máximo"
                elif D < 0:
                    tipo = "Punto silla"
                else:
                    tipo = "No concluyente"
                
                resultado += f"({x_val}, {y_val}): {tipo}\n"
            
            return resultado
        except Exception as e:
            return f"Error: {e}"
    
    def lagrange(self, funcion_str, restriccion_str):
        """Método de multiplicadores de Lagrange"""
        try:
            f = sp.sympify(funcion_str)
            g = sp.sympify(restriccion_str)
            lam = sp.Symbol('lambda')
            
            # Formar el Lagrangiano
            L = f - lam * g
            
            # Derivadas parciales
            Lx = sp.diff(L, self.x)
            Ly = sp.diff(L, self.y)
            Llam = sp.diff(L, lam)
            
            # Resolver sistema
            soluciones = sp.solve([Lx, Ly, Llam], [self.x, self.y, lam])
            
            resultado = f"Optimización con restricción:\n"
            resultado += f"f = {f}, sujeto a {g} = 0\n"
            resultado += f"Puntos críticos: {soluciones}"
            
            return resultado
        except Exception as e:
            return f"Error: {e}"
    
    # ============= SERIES Y SUCESIONES =============
    
    def limite_sucesion(self, an_str, n_var='n'):
        """Calcula el límite de una sucesión"""
        try:
            n = sp.Symbol(n_var)
            an = sp.sympify(an_str)
            lim = sp.limit(an, n, sp.oo)
            
            if lim.is_finite:
                return f"lim(n→∞) {an} = {lim} (Converge)"
            else:
                return f"lim(n→∞) {an} = {lim} (Diverge)"
        except Exception as e:
            return f"Error: {e}"
    
    def suma_serie_geometrica(self, a, r, n_terminos=None):
        """Calcula la suma de una serie geométrica"""
        try:
            if n_terminos:
                # Serie finita
                suma = a * (1 - r**n_terminos) / (1 - r)
                return f"Suma de {n_terminos} términos: {suma}"
            else:
                # Serie infinita
                if abs(r) < 1:
                    suma = a / (1 - r)
                    return f"Suma infinita: {suma} (|r| < 1, converge)"
                else:
                    return "Serie divergente (|r| ≥ 1)"
        except Exception as e:
            return f"Error: {e}"
    
    def serie_taylor(self, funcion_str, punto=0, orden=5):
        """Calcula la serie de Taylor/Maclaurin"""
        try:
            f = sp.sympify(funcion_str)
            serie = sp.series(f, self.x, punto, orden + 1)
            return f"Serie de Taylor en x={punto}: {serie.removeO()}"
        except Exception as e:
            return f"Error: {e}"
    
    # ============= APLICACIONES ECONÓMICAS =============
    
    def excedente_consumidor(self, demanda_str, q0=None, p0=None):
        """Calcula el excedente del consumidor"""
        try:
            demanda = sp.sympify(demanda_str)
            
            if q0 is not None:
                p0 = demanda.subs(self.q, q0)
                p_max = demanda.subs(self.q, 0)
                excedente = sp.integrate(demanda - p0, (self.q, 0, q0))
            elif p0 is not None:
                q0 = sp.solve(demanda - p0, self.q)[0]
                excedente = sp.integrate(demanda - p0, (self.q, 0, q0))
            else:
                return "Debe especificar q0 o p0"
            
            return f"Excedente del consumidor: {excedente} = {float(excedente):.2f}"
        except Exception as e:
            return f"Error: {e}"
    
    def excedente_productor(self, oferta_str, q0=None, p0=None):
        """Calcula el excedente del productor"""
        try:
            oferta = sp.sympify(oferta_str)
            
            if q0 is not None:
                p0 = oferta.subs(self.q, q0)
                excedente = sp.integrate(p0 - oferta, (self.q, 0, q0))
            elif p0 is not None:
                q0 = sp.solve(oferta - p0, self.q)[0]
                excedente = sp.integrate(p0 - oferta, (self.q, 0, q0))
            else:
                return "Debe especificar q0 o p0"
            
            return f"Excedente del productor: {excedente} = {float(excedente):.2f}"
        except Exception as e:
            return f"Error: {e}"
    
    def interes_compuesto(self, capital, tasa, tiempo, n_periodos=1):
        """Calcula el monto con interés compuesto"""
        try:
            monto = capital * (1 + tasa/n_periodos)**(n_periodos * tiempo)
            return f"Capital inicial: ${capital}\nTasa: {tasa*100}%\nTiempo: {tiempo}\nMonto final: ${monto:.2f}"
        except Exception as e:
            return f"Error: {e}"

# ============= INTERFAZ DE USUARIO =============

def menu_principal():
    """Menú principal de la calculadora"""
    calc = CalculadoraAnalisisII()
    
    while True:
        print("\n" + "="*50)
        print("CALCULADORA DE ANÁLISIS MATEMÁTICO II")
        print("="*50)
        print("1. Integrales Indefinidas")
        print("2. Integrales Definidas")
        print("3. Ecuaciones Diferenciales")
        print("4. Funciones Multivariables")
        print("5. Series y Sucesiones")
        print("6. Aplicaciones Económicas")
        print("0. Salir")
        print("-"*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "0":
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            menu_integrales_indefinidas(calc)
        elif opcion == "2":
            menu_integrales_definidas(calc)
        elif opcion == "3":
            menu_ecuaciones_diferenciales(calc)
        elif opcion == "4":
            menu_funciones_multivariables(calc)
        elif opcion == "5":
            menu_series(calc)
        elif opcion == "6":
            menu_aplicaciones_economicas(calc)
        else:
            print("Opción no válida")

def menu_integrales_indefinidas(calc):
    """Submenú para integrales indefinidas"""
    print("\n--- INTEGRALES INDEFINIDAS ---")
    print("1. Integral simple")
    print("2. Integral por sustitución")
    print("3. Integral por partes")
    
    sub_opcion = input("Seleccione método: ")
    
    if sub_opcion == "1":
        expr = input("Ingrese la función a integrar (ej: x**2 + 3*x): ")
        print(calc.integral_indefinida(expr))
    elif sub_opcion == "2":
        expr = input("Ingrese la función: ")
        u = input("Ingrese la sustitución u (ej: x**2 + 1): ")
        print(calc.integral_sustitucion(expr, u, ""))
    elif sub_opcion == "3":
        u = input("Ingrese u (ej: x): ")
        dv = input("Ingrese dv (ej: exp(x)): ")
        print(calc.integral_por_partes(u, dv))

def menu_integrales_definidas(calc):
    """Submenú para integrales definidas"""
    print("\n--- INTEGRALES DEFINIDAS ---")
    print("1. Integral definida")
    print("2. Área entre curvas")
    
    sub_opcion = input("Seleccione opción: ")
    
    if sub_opcion == "1":
        expr = input("Ingrese la función: ")
        a = float(input("Límite inferior: "))
        b = float(input("Límite superior: "))
        print(calc.integral_definida(expr, a, b))
    elif sub_opcion == "2":
        f1 = input("Primera función: ")
        f2 = input("Segunda función: ")
        usar_limites = input("¿Especificar límites? (s/n): ")
        if usar_limites.lower() == 's':
            a = float(input("Límite inferior: "))
            b = float(input("Límite superior: "))
            print(calc.area_entre_curvas(f1, f2, a, b))
        else:
            print(calc.area_entre_curvas(f1, f2))

def menu_ecuaciones_diferenciales(calc):
    """Submenú para ecuaciones diferenciales"""
    print("\n--- ECUACIONES DIFERENCIALES ---")
    print("Ingrese la ecuación diferencial")
    print("Ejemplo: Eq(y(x).diff(x), x*y(x))")
    
    ec = input("Ecuación: ")
    cond_inicial = input("¿Tiene condición inicial? (s/n): ")
    
    if cond_inicial.lower() == 's':
        x0 = float(input("x0: "))
        y0 = float(input("y0: "))
        print(calc.ecuacion_diferencial_separable(ec, (x0, y0)))
    else:
        print(calc.ecuacion_diferencial_separable(ec))

def menu_funciones_multivariables(calc):
    """Submenú para funciones multivariables"""
    print("\n--- FUNCIONES MULTIVARIABLES ---")
    print("1. Derivada parcial")
    print("2. Gradiente")
    print("3. Puntos críticos")
    print("4. Multiplicadores de Lagrange")
    
    sub_opcion = input("Seleccione opción: ")
    
    if sub_opcion == "1":
        f = input("Ingrese f(x,y): ")
        var = input("Variable de derivación (x/y): ")
        print(calc.derivada_parcial(f, var))
    elif sub_opcion == "2":
        f = input("Ingrese f(x,y): ")
        print(calc.gradiente(f))
    elif sub_opcion == "3":
        f = input("Ingrese f(x,y): ")
        print(calc.puntos_criticos(f))
    elif sub_opcion == "4":
        f = input("Función objetivo f(x,y): ")
        g = input("Restricción g(x,y) = 0 (ingrese solo g): ")
        print(calc.lagrange(f, g))

def menu_series(calc):
    """Submenú para series y sucesiones"""
    print("\n--- SERIES Y SUCESIONES ---")
    print("1. Límite de sucesión")
    print("2. Serie geométrica")
    print("3. Serie de Taylor")
    
    sub_opcion = input("Seleccione opción: ")
    
    if sub_opcion == "1":
        an = input("Término general an (use n como variable): ")
        print(calc.limite_sucesion(an))
    elif sub_opcion == "2":
        a = float(input("Primer término a: "))
        r = float(input("Razón r: "))
        finita = input("¿Serie finita? (s/n): ")
        if finita.lower() == 's':
            n = int(input("Número de términos: "))
            print(calc.suma_serie_geometrica(a, r, n))
        else:
            print(calc.suma_serie_geometrica(a, r))
    elif sub_opcion == "3":
        f = input("Función: ")
        punto = float(input("Punto de expansión (0 para Maclaurin): "))
        orden = int(input("Orden de la serie: "))
        print(calc.serie_taylor(f, punto, orden))

def menu_aplicaciones_economicas(calc):
    """Submenú para aplicaciones económicas"""
    print("\n--- APLICACIONES ECONÓMICAS ---")
    print("1. Excedente del consumidor")
    print("2. Excedente del productor")
    print("3. Interés compuesto")
    
    sub_opcion = input("Seleccione opción: ")
    
    if sub_opcion == "1":
        demanda = input("Función de demanda p(q): ")
        tipo = input("Especificar q0 o p0? (q/p): ")
        if tipo.lower() == 'q':
            q0 = float(input("q0: "))
            print(calc.excedente_consumidor(demanda, q0=q0))
        else:
            p0 = float(input("p0: "))
            print(calc.excedente_consumidor(demanda, p0=p0))
    elif sub_opcion == "2":
        oferta = input("Función de oferta p(q): ")
        tipo = input("Especificar q0 o p0? (q/p): ")
        if tipo.lower() == 'q':
            q0 = float(input("q0: "))
            print(calc.excedente_productor(oferta, q0=q0))
        else:
            p0 = float(input("p0: "))
            print(calc.excedente_productor(oferta, p0=p0))
    elif sub_opcion == "3":
        capital = float(input("Capital inicial: $"))
        tasa = float(input("Tasa de interés (en %): ")) / 100
        tiempo = float(input("Tiempo: "))
        n = int(input("Períodos de capitalización por unidad de tiempo (1 para anual): "))
        print(calc.interes_compuesto(capital, tasa, tiempo, n))

# ============= EJEMPLOS DE USO =============

def ejemplos_de_uso():
    """Muestra ejemplos de uso de la calculadora"""
    calc = CalculadoraAnalisisII()
    
    print("\n" + "="*50)
    print("EJEMPLOS DE USO")
    print("="*50)
    
    # Ejemplo 1: Integral indefinida
    print("\n1. Integral indefinida:")
    print(calc.integral_indefinida("x**2 + 3*x + 1"))
    
    # Ejemplo 2: Integral definida
    print("\n2. Integral definida:")
    print(calc.integral_definida("x**2", 0, 2))
    
    # Ejemplo 3: Área entre curvas
    print("\n3. Área entre curvas:")
    print(calc.area_entre_curvas("x**2", "x + 2"))
    
    # Ejemplo 4: Derivada parcial
    print("\n4. Derivada parcial:")
    print(calc.derivada_parcial("x**2 + 3*x*y + y**2", 'x'))
    
    # Ejemplo 5: Puntos críticos
    print("\n5. Puntos críticos:")
    print(calc.puntos_criticos("x**2 + y**2 - 2*x - 4*y"))
    
    # Ejemplo 6: Serie geométrica
    print("\n6. Serie geométrica:")
    print(calc.suma_serie_geometrica(1, 0.5))
    
    # Ejemplo 7: Excedente del consumidor
    print("\n7. Excedente del consumidor:")
    print(calc.excedente_consumidor("10 - q", q0=5))
    
    # Ejemplo 8: Interés compuesto
    print("\n8. Interés compuesto:")
    print(calc.interes_compuesto(1000, 0.05, 3, 12))

if __name__ == "__main__":
    print("Bienvenido a la Calculadora de Análisis Matemático II")
    print("Seleccione una opción:")
    print("1. Usar calculadora interactiva")
    print("2. Ver ejemplos de uso")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        menu_principal()
    elif opcion == "2":
        ejemplos_de_uso()
    else:
        print("Opción no válida")