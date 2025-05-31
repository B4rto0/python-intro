"""
Moduł math_tools - narzędzia matematyczne i statystyczne
=======================================================

Ten moduł zawiera funkcje i klasy do:
- Obliczeń statystycznych
- Normalizacji danych
- Podstawowych operacji matematycznych
"""

import math
from typing import List, Union, Dict, Tuple
from statistics import mean, median, mode, stdev


def calculate_statistics(data: List[Union[int, float]]) -> Dict[str, float]:
    """
    Oblicza podstawowe statystyki dla listy liczb.
    
    Args:
        data (List[Union[int, float]]): Lista liczb
    
    Returns:
        Dict[str, float]: Słownik ze statystykami
    
    Raises:
        ValueError: Gdy lista jest pusta lub zawiera nieprawidłowe dane
    
    Example:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'mean': 3.0, 'median': 3, 'min': 1, 'max': 5, 'std': 1.58...}
    """
    if not data:
        raise ValueError("Lista danych nie może być pusta")
    
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Wszystkie elementy muszą być liczbami")
    
    stats = {
        'mean': mean(data),
        'median': median(data),
        'min': min(data),
        'max': max(data),
        'count': len(data),
        'sum': sum(data)
    }
    
    # Odchylenie standardowe tylko dla więcej niż jednego elementu
    if len(data) > 1:
        stats['std'] = stdev(data)
        stats['variance'] = stdev(data) ** 2
    else:
        stats['std'] = 0.0
        stats['variance'] = 0.0
    
    # Moda - obsługa wyjątku gdy brak unikalnej mody
    try:
        stats['mode'] = mode(data)
    except:
        stats['mode'] = None
    
    return stats


def normalize_data(data: List[Union[int, float]], 
                  method: str = 'min-max') -> List[float]:
    """
    Normalizuje dane używając wybranej metody.
    
    Args:
        data (List[Union[int, float]]): Dane do normalizacji
        method (str): Metoda normalizacji ('min-max' lub 'z-score')
    
    Returns:
        List[float]: Znormalizowane dane
    
    Raises:
        ValueError: Gdy metoda jest nieznana lub dane nieprawidłowe
    """
    if not data:
        raise ValueError("Lista danych nie może być pusta")
    
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Wszystkie elementy muszą być liczbami")
    
    if method == 'min-max':
        min_val = min(data)
        max_val = max(data)
        
        if min_val == max_val:
            return [0.0] * len(data)
        
        return [(x - min_val) / (max_val - min_val) for x in data]
    
    elif method == 'z-score':
        if len(data) < 2:
            return [0.0] * len(data)
        
        data_mean = mean(data)
        data_std = stdev(data)
        
        if data_std == 0:
            return [0.0] * len(data)
        
        return [(x - data_mean) / data_std for x in data]
    
    else:
        raise ValueError("Nieznana metoda normalizacji. Użyj 'min-max' lub 'z-score'")


def calculate_correlation(x: List[Union[int, float]], 
                         y: List[Union[int, float]]) -> float:
    """
    Oblicza współczynnik korelacji Pearsona między dwoma zmiennymi.
    
    Args:
        x (List[Union[int, float]]): Pierwsza zmienna
        y (List[Union[int, float]]): Druga zmienna
    
    Returns:
        float: Współczynnik korelacji (-1 do 1)
    
    Raises:
        ValueError: Gdy listy mają różne długości lub są puste
    """
    if len(x) != len(y):
        raise ValueError("Listy muszą mieć tę samą długość")
    
    if len(x) < 2:
        raise ValueError("Potrzeba co najmniej 2 punktów danych")
    
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y2 = sum(yi ** 2 for yi in y)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
    
    if denominator == 0:
        return 0.0
    
    return numerator / denominator


class MathCalculator:
    """
    Klasa do zaawansowanych obliczeń matematycznych.
    
    Zawiera metody do różnych typów obliczeń matematycznych i statystycznych.
    """
    
    @staticmethod
    def factorial(n: int) -> int:
        """
        Oblicza silnię liczby.
        
        Args:
            n (int): Liczba nieujemna
        
        Returns:
            int: Silnia liczby n
        
        Raises:
            ValueError: Gdy n jest ujemne
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("Argument musi być nieujemną liczbą całkowitą")
        
        if n <= 1:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """
        Oblicza n-ty element ciągu Fibonacciego.
        
        Args:
            n (int): Pozycja w ciągu (0-indexed)
        
        Returns:
            int: N-ty element ciągu Fibonacciego
        
        Raises:
            ValueError: Gdy n jest ujemne
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("Argument musi być nieujemną liczbą całkowitą")
        
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Sprawdza czy liczba jest liczbą pierwszą.
        
        Args:
            n (int): Liczba do sprawdzenia
        
        Returns:
            bool: True jeśli liczba jest pierwsza
        """
        if not isinstance(n, int) or n < 2:
            return False
        
        if n == 2:
            return True
        
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        
        return True
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        Oblicza największy wspólny dzielnik dwóch liczb.
        
        Args:
            a (int): Pierwsza liczba
            b (int): Druga liczba
        
        Returns:
            int: Największy wspólny dzielnik
        """
        while b:
            a, b = b, a % b
        return abs(a)
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """
        Oblicza najmniejszą wspólną wielokrotność dwóch liczb.
        
        Args:
            a (int): Pierwsza liczba
            b (int): Druga liczba
        
        Returns:
            int: Najmniejsza wspólna wielokrotność
        """
        return abs(a * b) // MathCalculator.gcd(a, b) if a and b else 0