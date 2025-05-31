"""
Testy jednostkowe dla modułu math_tools
"""

import unittest
import math
from dataflow.math_tools import (
    calculate_statistics, normalize_data, calculate_correlation, MathCalculator
)


class TestMathTools(unittest.TestCase):
    
    def setUp(self):
        """Przygotowanie danych testowych"""
        self.sample_data = [1, 2, 3, 4, 5]
        self.sample_data_2 = [2, 4, 6, 8, 10]
    
    def test_calculate_statistics_basic(self):
        """Test podstawowych statystyk"""
        stats = calculate_statistics(self.sample_data)
        
        self.assertEqual(stats['mean'], 3.0)
        self.assertEqual(stats['median'], 3)
        self.assertEqual(stats['min'], 1)
        self.assertEqual(stats['max'], 5)
        self.assertEqual(stats['count'], 5)
        self.assertEqual(stats['sum'], 15)
        self.assertAlmostEqual(stats['std'], 1.5811, places=3)
    
    def test_calculate_statistics_single_value(self):
        """Test statystyk dla pojedynczej wartości"""
        stats = calculate_statistics([5])
        
        self.assertEqual(stats['mean'], 5.0)
        self.assertEqual(stats['median'], 5)
        self.assertEqual(stats['std'], 0.0)
        self.assertEqual(stats['variance'], 0.0)
    
    def test_calculate_statistics_empty_list(self):
        """Test statystyk dla pustej listy"""
        with self.assertRaises(ValueError):
            calculate_statistics([])
    
    def test_calculate_statistics_invalid_data(self):
        """Test statystyk dla nieprawidłowych danych"""
        with self.assertRaises(ValueError):
            calculate_statistics([1, 2, 'invalid', 4])
    
    def test_normalize_data_min_max(self):
        """Test normalizacji min-max"""
        normalized = normalize_data(self.sample_data, 'min-max')
        
        self.assertEqual(normalized[0], 0.0)  # min
        self.assertEqual(normalized[-1], 1.0)  # max
        self.assertTrue(all(0 <= x <= 1 for x in normalized))
    
    def test_normalize_data_z_score(self):
        """Test normalizacji z-score"""
        normalized = normalize_data(self.sample_data, 'z-score')
        
        # Sprawdzenie czy średnia jest bliska 0
        mean_normalized = sum(normalized) / len(normalized)
        self.assertAlmostEqual(mean_normalized, 0.0, places=10)
    
    def test_normalize_data_constant_values(self):
        """Test normalizacji dla stałych wartości"""
        constant_data = [5, 5, 5, 5]
        
        # Min-max dla stałych wartości
        normalized_minmax = normalize_data(constant_data, 'min-max')
        self.assertEqual(normalized_minmax, [0.0, 0.0, 0.0, 0.0])
        
        # Z-score dla stałych wartości
        normalized_zscore = normalize_data(constant_data, 'z-score')
        self.assertEqual(normalized_zscore, [0.0, 0.0, 0.0, 0.0])
    
    def test_normalize_data_invalid_method(self):
        """Test normalizacji z nieprawidłową metodą"""
        with self.assertRaises(ValueError):
            normalize_data(self.sample_data, 'invalid_method')
    
    def test_calculate_correlation_perfect_positive(self):
        """Test korelacji doskonale pozytywnej"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        
        correlation = calculate_correlation(x, y)
        self.assertAlmostEqual(correlation, 1.0, places=10)
    
    def test_calculate_correlation_perfect_negative(self):
        """Test korelacji doskonale negatywnej"""
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]
        
        correlation = calculate_correlation(x, y)
        self.assertAlmostEqual(correlation, -1.0, places=10)
    
    def test_calculate_correlation_no_correlation(self):
        """Test braku korelacji"""
        x = [1, 2, 3, 4, 5]
        y = [1, 1, 1, 1, 1]  # stałe wartości
        
        correlation = calculate_correlation(x, y)
        self.assertEqual(correlation, 0.0)
    
    def test_calculate_correlation_different_lengths(self):
        """Test korelacji dla list o różnych długościach"""
        x = [1, 2, 3]
        y = [1, 2, 3, 4]
        
        with self.assertRaises(ValueError):
            calculate_correlation(x, y)
    
    def test_calculate_correlation_insufficient_data(self):
        """Test korelacji dla zbyt małej ilości danych"""
        x = [1]
        y = [2]
        
        with self.assertRaises(ValueError):
            calculate_correlation(x, y)


class TestMathCalculator(unittest.TestCase):
    
    def test_factorial(self):
        """Test obliczania silni"""
        self.assertEqual(MathCalculator.factorial(0), 1)
        self.assertEqual(MathCalculator.factorial(1), 1)
        self.assertEqual(MathCalculator.factorial(5), 120)
        self.assertEqual(MathCalculator.factorial(10), 3628800)
    
    def test_factorial_negative(self):
        """Test silni dla liczby ujemnej"""
        with self.assertRaises(ValueError):
            MathCalculator.factorial(-1)
    
    def test_factorial_non_integer(self):
        """Test silni dla nie-liczby całkowitej"""
        with self.assertRaises(ValueError):
            MathCalculator.factorial(3.5)
    
    def test_fibonacci(self):
        """Test ciągu Fibonacciego"""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        
        for i, expected_value in enumerate(expected):
            self.assertEqual(MathCalculator.fibonacci(i), expected_value)
    
    def test_fibonacci_negative(self):
        """Test Fibonacciego dla liczby ujemnej"""
        with self.assertRaises(ValueError):
            MathCalculator.fibonacci(-1)
    
    def test_is_prime(self):
        """Test sprawdzania liczb pierwszych"""
        # Liczby pierwsze
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            self.assertTrue(MathCalculator.is_prime(prime))
        
        # Liczby złożone
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
        for composite in composites:
            self.assertFalse(MathCalculator.is_prime(composite))
        
        # Przypadki brzegowe
        self.assertFalse(MathCalculator.is_prime(0))
        self.assertFalse(MathCalculator.is_prime(1))
        self.assertFalse(MathCalculator.is_prime(-5))
    
    def test_gcd(self):
        """Test największego wspólnego dzielnika"""
        self.assertEqual(MathCalculator.gcd(12, 8), 4)
        self.assertEqual(MathCalculator.gcd(17, 13), 1)
        self.assertEqual(MathCalculator.gcd(100, 25), 25)
        self.assertEqual(MathCalculator.gcd(-12, 8), 4)
        self.assertEqual(MathCalculator.gcd(0, 5), 5)
    
    def test_lcm(self):
        """Test najmniejszej wspólnej wielokrotności"""
        self.assertEqual(MathCalculator.lcm(12, 8), 24)
        self.assertEqual(MathCalculator.lcm(17, 13), 221)
        self.assertEqual(MathCalculator.lcm(4, 6), 12)
        self.assertEqual(MathCalculator.lcm(0, 5), 0)


if __name__ == '__main__':
    unittest.main()