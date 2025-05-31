import unittest
import datetime
from app import (
    validate_email,
    calculate_circle_area,
    filter_even_numbers,
    convert_date_format,
    is_palindrome,
    get_function_info
)


class TestAppFunctions(unittest.TestCase):
    """
    Klasa testowa dla wszystkich funkcji aplikacji.
    Implementuje testy zgodnie z podejściem TDD.
    """
    
    def setUp(self):
        """
        Metoda setUp() do przygotowania środowiska testowego.
        Wywoływana przed każdym testem.
        """
        self.valid_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "admin123@company.org"
        ]
        self.invalid_emails = [
            "invalid-email",
            "@example.com",
            "test@",
            "test.example.com",
            ""
        ]
        
        self.test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.empty_list = []
        self.mixed_numbers = [-2, -1, 0, 1, 2, 3]
    

    
    def test_validate_email_valid_addresses(self):
        """Test sprawdza poprawne adresy email"""
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email), f"Email {email} powinien być poprawny")
    
    def test_validate_email_invalid_addresses(self):
        """Test sprawdza niepoprawne adresy email"""
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email), f"Email {email} powinien być niepoprawny")
    
    def test_validate_email_non_string_input(self):
        """Test sprawdza czy funkcja zwraca False dla nie-stringów"""
        self.assertFalse(validate_email(None))
        self.assertFalse(validate_email(123))
        self.assertFalse(validate_email([])) 
    
    def test_validate_email_edge_cases(self):
        """Test przypadków brzegowych dla walidacji email"""

        long_email = "a" * 250 + "@example.com"
        self.assertFalse(validate_email(long_email))
        

        self.assertTrue(validate_email("test.user.name@example.com"))

        self.assertTrue(validate_email("user123@domain456.com"))
    

    
    def test_calculate_circle_area_positive_radius(self):
        """Test obliczania pola koła dla dodatnich promieni"""
        test_cases = [
            (1, 3.141592653589793),
            (2, 12.566370614359172),
            (5, 78.53981633974483)
        ]
        
        for radius, expected in test_cases:
            with self.subTest(radius=radius):
                result = calculate_circle_area(radius)
                self.assertAlmostEqual(result, expected, places=10)
    
    def test_calculate_circle_area_zero_radius(self):
        """Test obliczania pola koła dla promienia równego zero"""
        self.assertEqual(calculate_circle_area(0), 0)
    
    def test_calculate_circle_area_negative_radius(self):
        """Test sprawdza czy funkcja rzuca wyjątek dla ujemnego promienia"""
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)
        
        with self.assertRaises(ValueError):
            calculate_circle_area(-5.5)
    
    def test_calculate_circle_area_non_numeric_input(self):
        """Test sprawdza czy funkcja rzuca wyjątek dla niepoprawnych typów danych"""
        with self.assertRaises(TypeError):
            calculate_circle_area("abc")
        
        with self.assertRaises(TypeError):
            calculate_circle_area(None)
    

    
    def test_filter_even_numbers_mixed_list(self):
        """Test filtrowania liczb parzystych z mieszanej listy"""
        result = filter_even_numbers(self.test_numbers)
        expected = [2, 4, 6, 8, 10]
        self.assertEqual(result, expected)
    
    def test_filter_even_numbers_empty_list(self):
        """Test filtrowania z pustej listy"""
        result = filter_even_numbers(self.empty_list)
        self.assertEqual(result, [])
    
    def test_filter_even_numbers_no_even_numbers(self):
        """Test listy zawierającej tylko liczby nieparzyste"""
        odd_numbers = [1, 3, 5, 7, 9]
        result = filter_even_numbers(odd_numbers)
        self.assertEqual(result, [])
    
    def test_filter_even_numbers_negative_numbers(self):
        """Test filtrowania liczb ujemnych"""
        result = filter_even_numbers(self.mixed_numbers)
        expected = [-2, 0, 2]
        self.assertEqual(result, expected)
    
    def test_filter_even_numbers_float_numbers(self):
        """Test filtrowania liczb zmiennoprzecinkowych - pokrywa linię 75"""
        
        float_numbers = [1.5, 2.0, 3.7, 4.0]
        result = filter_even_numbers(float_numbers)
        expected = [2, 4]  
        self.assertEqual(result, expected)
    
    def test_filter_even_numbers_invalid_input(self):
        """Test sprawdza czy funkcja rzuca wyjątek dla niepoprawnych danych"""
        with self.assertRaises(TypeError):
            filter_even_numbers("not a list")
        
        with self.assertRaises(TypeError):
            filter_even_numbers([1, "two", 3])
    

    
    def test_convert_date_format_valid_dates(self):
        """Test konwersji poprawnych dat"""
        test_cases = [
            ("2023-12-25", "25/12/2023"),
            ("2024-01-01", "01/01/2024"),
            ("2023-06-15", "15/06/2023")
        ]
        
        for input_date, expected in test_cases:
            with self.subTest(date=input_date):
                result = convert_date_format(input_date)
                self.assertEqual(result, expected)
    
    def test_convert_date_format_non_string_input(self):
        """Test konwersji dla danych które nie są stringami - pokrywa linię 97"""
        with self.assertRaises(ValueError):
            convert_date_format(None)
        
        with self.assertRaises(ValueError):
            convert_date_format(123)
    
    def test_convert_date_format_invalid_format(self):
        """Test konwersji dat w niepoprawnym formacie"""
        invalid_dates = [
            "25-12-2023",
            "2023/12/25",
            "12/25/2023",
            "invalid-date"
        ]
        
        for date in invalid_dates:
            with self.subTest(date=date):
                with self.assertRaises(ValueError):
                    convert_date_format(date)
    
    def test_convert_date_format_edge_cases(self):
        """Test przypadków brzegowych dla konwersji dat"""

        future_date = "2030-12-31"
        result = convert_date_format(future_date)
        self.assertEqual(result, "31/12/2030")
        
        
        old_date = "1900-01-01"
        result = convert_date_format(old_date)
        self.assertEqual(result, "01/01/1900")
    
  
    
    def test_is_palindrome_valid_palindromes(self):
        """Test sprawdza poprawne palindromy"""
        palindromes = [
            "racecar",
            "level",
            "radar",
            "madam",
            "A man a plan a canal Panama",
            "Was it a car or a cat I saw"  
        ]
        
        for palindrome in palindromes:
            with self.subTest(text=palindrome):
                self.assertTrue(is_palindrome(palindrome))
    
    def test_is_palindrome_non_palindromes(self):
        """Test sprawdza teksty które nie są palindromami"""
        non_palindromes = [
            "hello",
            "python",
            "programming",
            "test123"
        ]
        
        for text in non_palindromes:
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text))
    
    def test_is_palindrome_non_string_input(self):
        """Test sprawdza czy funkcja zwraca False dla nie-stringów - pokrywa linię 122"""
        self.assertFalse(is_palindrome(None))
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome([]))
    
    def test_is_palindrome_edge_cases(self):
        """Test przypadków brzegowych dla palindromów"""

        self.assertTrue(is_palindrome(""))
        

        self.assertTrue(is_palindrome("a"))
        

        self.assertTrue(is_palindrome("   "))
        

        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12345"))
    
    def test_is_palindrome_case_insensitive(self):
        """Test sprawdza czy funkcja ignoruje wielkość liter"""
        test_cases = [
            ("Racecar", True),
            ("Level", True),
            ("RaceCar", True),
            ("Hello", False)
        ]
        
        for text, expected in test_cases:
            with self.subTest(text=text):
                self.assertEqual(is_palindrome(text), expected)


    
    def test_get_function_info(self):
        """Test sprawdza czy funkcja zwraca poprawne informacje o funkcjach - pokrywa linie 139, 150-173"""
        result = get_function_info()
        
        self.assertIsInstance(result, dict)
        

        expected_keys = [
            'validate_email',
            'calculate_circle_area', 
            'filter_even_numbers',
            'convert_date_format',
            'is_palindrome'
        ]
        
        for key in expected_keys:
            self.assertIn(key, result)
        

        self.assertEqual(result['validate_email'], 'Sprawdza poprawność adresu e-mail')
        self.assertEqual(result['calculate_circle_area'], 'Oblicza pole koła na podstawie promienia')
        self.assertEqual(result['filter_even_numbers'], 'Filtruje listę zwracając tylko liczby parzyste')
        self.assertEqual(result['convert_date_format'], 'Konwertuje datę z formatu YYYY-MM-DD na DD/MM/YYYY')
        self.assertEqual(result['is_palindrome'], 'Sprawdza czy tekst jest palindromem')



class TestParametrized(unittest.TestCase):
    """
    Klasa demonstrująca testy parametryzowane.
    """
    
    def test_circle_area_multiple_values(self):
        """Test parametryzowany dla obliczania pola koła"""
        test_data = [
            (1, 3.141592653589793),
            (2, 12.566370614359172),
            (3, 28.274333882308138),
            (0.5, 0.7853981633974483)
        ]
        
        for radius, expected_area in test_data:
            with self.subTest(radius=radius):
                result = calculate_circle_area(radius)
                self.assertAlmostEqual(result, expected_area, places=10)


if __name__ == '__main__':

    unittest.main(verbosity=2)