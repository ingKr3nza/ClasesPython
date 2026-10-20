"""Módulo de Estructuras Dinámicas: Lista Enlazada de Sensores.
Implementación limpia en Python bajo estándar PEP 8 con Type Hints.
"""

class NodoSensor:
    """Nodo individual para almacenar datos de sensores e interconectarse en RAM."""
    def __init__(self, lectura: float):
        self.lectura: float = lectura
        self.siguiente: "NodoSensor" | None = None


class ListaEnlazadaSensores:
    """Clase gestora que encapsula las operaciones de la lista enlazada."""
    def __init__(self):
        self.cabeza: NodoSensor | None = None

    def insertar_inicio(self, lectura: float) -> None:
        """Inserta una nueva lectura al principio de la lista (O(1))."""
        nuevo_nodo = NodoSensor(lectura)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, lectura: float) -> None:
        """Inserta una nueva lectura al final de la lista (O(N))."""
        nuevo_nodo = NodoSensor(lectura)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def buscar(self, valor_buscado: float) -> bool:
        """Busca si existe una lectura específica en la estructura."""
        actual = self.cabeza
        while actual is not None:
            if actual.lectura == valor_buscado:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, valor_a_eliminar: float) -> bool:
        """Elimina la primera ocurrencia de un valor en la lista."""
        actual = self.cabeza
        anterior: NodoSensor | None = None

        # Caso 1: La lista está vacía
        if actual is None:
            return False

        # Caso 2: El elemento a eliminar es la cabeza
        if actual.lectura == valor_a_eliminar:
            self.cabeza = actual.siguiente
            return True

        # Caso 3: Buscar en el resto de la lista
        while actual is not None and actual.lectura != valor_a_eliminar:
            anterior = actual
            actual = actual.siguiente

        # Si no se encontró el valor
        if actual is None:
            return False

        # Reconectar referencias para "desenganchar" el nodo
        anterior.siguiente = actual.siguiente
        return True

    def mostrar(self) -> None:
        """Muestra por consola la secuencia completa de lecturas."""
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(f"[{actual.lectura}°C]")
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

