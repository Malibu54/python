# Sistema de Cuenta Bancaria

Un sistema simple y robusto para manejar operaciones bancarias básicas implementado en Python.

## Características

- ✅ **Operaciones básicas**: Depósitos, retiros y transferencias
- ✅ **Validación de datos**: Verificación de tipos y valores
- ✅ **Historial de transacciones**: Registro detallado con timestamps
- ✅ **Manejo de errores**: Excepciones apropiadas para casos de error
- ✅ **Encapsulación**: Atributos privados con acceso controlado
- ✅ **Documentación**: Docstrings detallados y type hints

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/malib54/cuenta-bancaria.git
cd cuenta-bancaria
```

2. Ejecuta el programa:
```bash
python cuenta_bancaria.py
```

## Uso

### Crear una cuenta

```python
from cuenta_bancaria import CuentaBancaria

# Crear cuenta con balance inicial
cuenta = CuentaBancaria("100-222-333", "Lady Vader", 1000)

# Crear cuenta sin balance inicial (por defecto 0)
cuenta_nueva = CuentaBancaria("200-333-444", "Juan Pérez")
```

### Operaciones básicas

```python
# Depositar dinero
cuenta.depositar(500)

# Retirar dinero
cuenta.retirar(200)

# Transferir dinero
cuenta.transferir(100, "200-333-444")

# Consultar balance
cuenta.generar_balance()
```

### Consultar historial

```python
# Ver todo el historial
cuenta.consultar_historial()

# Ver solo las últimas 5 transacciones
cuenta.consultar_historial(5)
```

### Propiedades de solo lectura

```python
print(f"Número de cuenta: {cuenta.num_cuenta}")
print(f"Titular: {cuenta.nombre_titular}")
print(f"Balance: ${cuenta.balance:,.2f}")
```

## Manejo de errores

El sistema maneja los siguientes errores:

- **TypeError**: Cuando se intenta usar un tipo de dato incorrecto
- **ValueError**: Cuando se usan valores inválidos (negativos, insuficientes fondos, etc.)

```python
try:
    cuenta.depositar(-100)  # Error: monto negativo
except ValueError as e:
    print(f"Error: {e}")

try:
    cuenta.retirar(10000)  # Error: fondos insuficientes
except ValueError as e:
    print(f"Error: {e}")
```

## Estructura del proyecto

```
cuenta-bancaria/
├── cuenta_bancaria.py    # Código principal
└──README.md            # Este archivo
```

## Ejemplo de salida

```
=== Sistema de Cuenta Bancaria ===

Cuenta creada: Cuenta: 100-222-333 | Titular: Lady Vader | Balance: $666.00

--- Operaciones ---
Balance actual: $666.00
Depósito exitoso. Nuevo balance: $766.00
Retiro exitoso. Nuevo balance: $716.00
Transferencia exitosa de $66.00 a 200-333-444
Nuevo balance: $650.00

--- Historial ---
1. [2025-07-15 10:30:15] DEPOSITO: $100.00 (Balance: $666.00 → $766.00)
2. [2025-07-15 10:30:15] RETIRO: $50.00 (Balance: $766.00 → $716.00)
3. [2025-07-15 10:30:15] TRANSFERENCIA: $66.00 (Balance: $716.00 → $650.00)

Estado final: Cuenta: 100-222-333 | Titular: Lady Vader | Balance: $650.00
```

## Requisitos

- Python 3.7+
- No requiere librerías externas

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commitea tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## Autor

**Lady Vader** - Desarrollo inicial

## Changelog

### v1.0.0 (2025-07-15)
- Implementación inicial del sistema de cuenta bancaria
- Operaciones básicas: depositar, retirar, transferir
- Historial de transacciones con timestamps
- Validación completa de datos
- Manejo robusto de errores