from datetime import datetime
from typing import List, Dict, Optional, Union


class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria con operaciones básicas.
    
    Attributes:
        _num_cuenta (str): Número único de la cuenta
        _nombre_titular (str): Nombre del titular de la cuenta
        _balance (float): Balance actual de la cuenta
        _historial (List[Dict]): Historial de transacciones
    """
    
    def __init__(self, num_cuenta: str, nombre_titular: str, balance: Union[int, float] = 0):
        """
        Inicializa una nueva cuenta bancaria.
        
        Args:
            num_cuenta (str): Número único de la cuenta
            nombre_titular (str): Nombre del titular
            balance (Union[int, float], optional): Balance inicial. Por defecto 0.
            
        Raises:
            TypeError: Si el balance no es un número
            ValueError: Si el balance es negativo
        """
        self._num_cuenta = num_cuenta
        self._nombre_titular = nombre_titular
        self._balance = self._validar_balance_inicial(balance)
        self._historial: List[Dict] = []

    def _validar_balance_inicial(self, balance: Union[int, float]) -> float:
        """
        Valida que el balance inicial sea válido.
        
        Args:
            balance (Union[int, float]): Balance a validar
            
        Returns:
            float: Balance validado
            
        Raises:
            TypeError: Si el balance no es un número
            ValueError: Si el balance es negativo
        """
        if not isinstance(balance, (int, float)):
            raise TypeError("El balance debe ser un número")
        if balance < 0:
            raise ValueError("El balance inicial no puede ser negativo")
        return float(balance)

    def _registrar_transaccion(self, tipo: str, monto: float, balance_anterior: float) -> None:
        """
        Registra una transacción en el historial.
        
        Args:
            tipo (str): Tipo de transacción (DEPOSITO, RETIRO, TRANSFERENCIA)
            monto (float): Monto de la transacción
            balance_anterior (float): Balance antes de la transacción
        """
        transaccion = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'tipo': tipo,
            'monto': monto,
            'balance_anterior': balance_anterior,
            'balance_nuevo': self._balance
        }
        self._historial.append(transaccion)

    @property
    def balance(self) -> float:
        """
        Getter para el balance actual.
        
        Returns:
            float: Balance actual de la cuenta
        """
        return self._balance

    @property
    def num_cuenta(self) -> str:
        """
        Getter para el número de cuenta.
        
        Returns:
            str: Número de cuenta
        """
        return self._num_cuenta

    @property
    def nombre_titular(self) -> str:
        """
        Getter para el nombre del titular.
        
        Returns:
            str: Nombre del titular
        """
        return self._nombre_titular

    def generar_balance(self) -> float:
        """
        Muestra el balance actual en consola.
        
        Returns:
            float: Balance actual
        """
        print(f"Balance actual: ${self._balance:,.2f}")
        return self._balance

    def depositar(self, monto: Union[int, float]) -> bool:
        """
        Deposita dinero en la cuenta.
        
        Args:
            monto (Union[int, float]): Cantidad a depositar
            
        Returns:
            bool: True si el depósito fue exitoso
            
        Raises:
            TypeError: Si el monto no es un número
            ValueError: Si el monto no es positivo
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")
        
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo")
        
        balance_anterior = self._balance
        self._balance += monto
        self._registrar_transaccion('DEPOSITO', monto, balance_anterior)
        print(f"Depósito exitoso. Nuevo balance: ${self._balance:,.2f}")
        return True

    def retirar(self, monto: Union[int, float]) -> bool:
        """
        Retira dinero de la cuenta.
        
        Args:
            monto (Union[int, float]): Cantidad a retirar
            
        Returns:
            bool: True si el retiro fue exitoso
            
        Raises:
            TypeError: Si el monto no es un número
            ValueError: Si el monto no es positivo o excede el balance
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")
        
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo")
        
        if monto > self._balance:
            raise ValueError("Fondos insuficientes")
        
        balance_anterior = self._balance
        self._balance -= monto
        self._registrar_transaccion('RETIRO', monto, balance_anterior)
        print(f"Retiro exitoso. Nuevo balance: ${self._balance:,.2f}")
        return True

    def transferir(self, monto: Union[int, float], cuenta_destino: Optional[str] = None) -> bool:
        """
        Transfiere dinero de la cuenta (simula transferencia).
        
        Args:
            monto (Union[int, float]): Cantidad a transferir
            cuenta_destino (Optional[str]): Cuenta de destino (opcional)
            
        Returns:
            bool: True si la transferencia fue exitosa
            
        Raises:
            TypeError: Si el monto no es un número
            ValueError: Si el monto no es positivo o excede el balance
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")
        
        if monto <= 0:
            raise ValueError("El monto a transferir debe ser positivo")
        
        if monto > self._balance:
            raise ValueError("Fondos insuficientes para la transferencia")
        
        balance_anterior = self._balance
        self._balance -= monto
        self._registrar_transaccion('TRANSFERENCIA', monto, balance_anterior)
        
        destino = cuenta_destino if cuenta_destino else "cuenta externa"
        print(f"Transferencia exitosa de ${monto:,.2f} a {destino}")
        print(f"Nuevo balance: ${self._balance:,.2f}")
        return True

    def consultar_historial(self, ultimas_n: Optional[int] = None) -> List[Dict]:
        """
        Consulta el historial de transacciones.
        
        Args:
            ultimas_n (Optional[int]): Número de transacciones más recientes a mostrar
            
        Returns:
            List[Dict]: Lista de transacciones
        """
        if not self._historial:
            print("No hay transacciones registradas")
            return []
        
        transacciones = self._historial[-ultimas_n:] if ultimas_n else self._historial
        
        print(f"\n--- Historial de transacciones ---")
        for i, trans in enumerate(transacciones, 1):
            print(f"{i}. [{trans['timestamp']}] {trans['tipo']}: ${trans['monto']:,.2f} "
                  f"(Balance: ${trans['balance_anterior']:,.2f} → ${trans['balance_nuevo']:,.2f})")
        
        return transacciones

    def __str__(self) -> str:
        """
        Representación en string de la cuenta.
        
        Returns:
            str: Información básica de la cuenta
        """
        return (f"Cuenta: {self._num_cuenta} | "
                f"Titular: {self._nombre_titular} | "
                f"Balance: ${self._balance:,.2f}")

    def __repr__(self) -> str:
        """
        Representación técnica de la cuenta.
        
        Returns:
            str: Representación técnica para debugging
        """
        return (f"CuentaBancaria('{self._num_cuenta}', "
                f"'{self._nombre_titular}', {self._balance})")


def main():
    """
    Función principal con ejemplo de uso del sistema.
    """
    try:
        # Crear cuenta
        print("=== Sistema de Cuenta Bancaria ===\n")
        mi_cuenta = CuentaBancaria("100-222-333", "Lady Vader", 666)
        print(f"Cuenta creada: {mi_cuenta}\n")
        
        # Operaciones básicas
        print("--- Operaciones ---")
        mi_cuenta.generar_balance()
        mi_cuenta.depositar(100)
        mi_cuenta.retirar(50)
        mi_cuenta.transferir(66, "200-333-444")
        
        # Consultar historial
        print("\n--- Historial ---")
        mi_cuenta.consultar_historial()
        
        # Información final
        print(f"\nEstado final: {mi_cuenta}")
        
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()