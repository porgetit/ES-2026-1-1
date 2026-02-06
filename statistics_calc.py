#!/usr/bin/env python3
"""
Módulo para el cálculo de estadísticas descriptivas básicas.

Este script permite calcular la media aritmética, varianza y desviación
estándar de un conjunto de números enteros proporcionados por el usuario.
"""

import math
import sys
from typing import List


def calculate_mean(numbers: List[int]) -> float:
    """
    Calcula la media aritmética de una lista de enteros.

    Args:
        numbers: Una lista de números enteros.

    Returns:
        La media aritmética como un valor flotante.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def calculate_variance(numbers: List[int], sample: bool = True) -> float:
    """
    Calcula la varianza de una lista de enteros.

    Args:
        numbers: Una lista de números enteros.
        sample: Si es True, calcula la varianza muestral (n-1). 
                Si es False, calcula la varianza poblacional (n).

    Returns:
        La varianza como un valor flotante.
    """
    if not numbers:
        return 0.0
    
    n = len(numbers)
    if sample and n <= 1:
        return 0.0

    mean = calculate_mean(numbers)
    # Suma de los cuadrados de las diferencias respecto a la media
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    
    denominator = n - 1 if sample else n
    return sum(squared_diffs) / denominator


def calculate_std_deviation(numbers: List[int], sample: bool = True) -> float:
    """
    Calcula la desviación estándar de una lista de enteros.

    Args:
        numbers: Una lista de números enteros.
        sample: Si es True, usa varianza muestral. Si es False, poblacional.

    Returns:
        La desviación estándar como un valor flotante.
    """
    variance = calculate_variance(numbers, sample=sample)
    return math.sqrt(variance)


def process_set(numbers: List[int], label: str = ""):
    """
    Calcula y muestra los resultados para un conjunto individual de datos.
    """
    if not numbers:
        print(f"\nConjunto {label}: La lista está vacía.")
        return

    mean = calculate_mean(numbers)
    
    # Cálculos muestrales (n-1)
    v_muestral = calculate_variance(numbers, sample=True)
    sd_muestral = calculate_std_deviation(numbers, sample=True)
    
    # Cálculos poblacionales (n)
    v_poblacional = calculate_variance(numbers, sample=False)
    sd_poblacional = calculate_std_deviation(numbers, sample=False)

    print(f"\nResultados {label}:")
    print(f"Datos: {numbers}")
    print(f"{'-' * 45}")
    print(f"Media aritmética:          {mean:.4f}")
    print(f"{'-' * 45}")
    print(f"Varianza (Muestral n-1):   {v_muestral:.4f}")
    print(f"Desv. Estándar (Muestral): {sd_muestral:.4f}")
    print(f"{'-' * 45}")
    print(f"Varianza (Poblacional n):  {v_poblacional:.4f}")
    print(f"Desv. Estándar (Poblac.):  {sd_poblacional:.4f}")
    print(f"{'-' * 45}")


def main():
    """
    Función principal que maneja la entrada de usuario para uno o más conjuntos de datos.
    """
    raw_input = ""
    
    # Si se pasan argumentos por línea de comandos
    if len(sys.argv) > 1:
        raw_input = " ".join(sys.argv[1:])
    else:
        # De lo contrario, pedir entrada interactiva
        print("Calculadora de Estadísticas Multi-Conjunto")
        print("Ingrese los números separados por espacios.")
        print("Para múltiples conjuntos, sepárelos por COMAS (ej: 1 2 3, 4 5 6)")
        print("Entrada:", end=" ")
        try:
            raw_input = sys.stdin.readline().strip()
            if not raw_input:
                print("Error: No se ingresaron datos.")
                sys.exit(1)
        except EOFError:
            sys.exit(0)

    # Dividir por comas para obtener los conjuntos
    set_strings = raw_input.split(",")
    
    for i, s in enumerate(set_strings):
        try:
            # Limpiar espacios y convertir a enteros
            numbers = [int(x) for x in s.strip().split() if x]
            if not numbers:
                continue
            
            label = f"#{i+1}" if len(set_strings) > 1 else ""
            process_set(numbers, label)
            
        except ValueError:
            print(f"\nError en conjunto {i+1}: Asegúrese de ingresar solo números enteros.")


if __name__ == "__main__":
    main()
