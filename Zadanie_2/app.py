import re
import math
import datetime


def validate_email(email):
    """
    Sprawdza poprawność adresu e-mail.
    
    Args:
        email (str): Adres e-mail do sprawdzenia
        
    Returns:
        bool: True jeśli adres jest poprawny, False w przeciwnym przypadku
    """
    if not isinstance(email, str) or not email:
        return False
    

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    

    if len(email) > 254:
        return False
    
    return bool(re.match(pattern, email))


def calculate_circle_area(radius):
    """
    Oblicza pole koła na podstawie promienia.
    
    Args:
        radius (float): Promień koła
        
    Returns:
        float: Pole koła
        
    Raises:
        ValueError: Gdy promień jest ujemny
        TypeError: Gdy promień nie jest liczbą
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Promień musi być liczbą")
    
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    
    return math.pi * radius ** 2


def filter_even_numbers(numbers):
    """
    Filtruje listę zwracając tylko liczby parzyste.
    
    Args:
        numbers (list): Lista liczb do przefiltrowania
        
    Returns:
        list: Lista zawierająca tylko liczby parzyste
        
    Raises:
        TypeError: Gdy argument nie jest listą lub zawiera nieprawidłowe elementy
    """
    if not isinstance(numbers, list):
        raise TypeError("Argument musi być listą")
    
    result = []
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("Wszystkie elementy listy muszą być liczbami")
        
        if isinstance(num, float) and not num.is_integer():

            continue
            
        if int(num) % 2 == 0:
            result.append(int(num))
    
    return result


def convert_date_format(date_string):
    """
    Konwertuje datę z formatu YYYY-MM-DD na DD/MM/YYYY.
    
    Args:
        date_string (str): Data w formacie YYYY-MM-DD
        
    Returns:
        str: Data w formacie DD/MM/YYYY
        
    Raises:
        ValueError: Gdy format daty jest niepoprawny
    """
    if not isinstance(date_string, str):
        raise ValueError("Data musi być stringiem")
    
    try:

        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        

        return date_obj.strftime('%d/%m/%Y')
        
    except ValueError:
        raise ValueError(f"Niepoprawny format daty: {date_string}. Oczekiwany format: YYYY-MM-DD")


def is_palindrome(text):
    """
    Sprawdza, czy tekst jest palindromem (czyta się tak samo od przodu i tyłu).
    Ignoruje spacje, znaki interpunkcyjne i wielkość liter.
    
    Args:
        text (str): Tekst do sprawdzenia
        
    Returns:
        bool: True jeśli tekst jest palindromem, False w przeciwnym przypadku
    """
    if not isinstance(text, str):
        return False
    

    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    

    return cleaned_text == cleaned_text[::-1]


def get_function_info():
    """
    Zwraca informacje o zaimplementowanych funkcjach.
    
    Returns:
        dict: Słownik z opisami funkcji
    """
    return {
        'validate_email': 'Sprawdza poprawność adresu e-mail',
        'calculate_circle_area': 'Oblicza pole koła na podstawie promienia',
        'filter_even_numbers': 'Filtruje listę zwracając tylko liczby parzyste',
        'convert_date_format': 'Konwertuje datę z formatu YYYY-MM-DD na DD/MM/YYYY',
        'is_palindrome': 'Sprawdza czy tekst jest palindromem'
    }


def run_demo():
    """
    Funkcja demonstracyjna pokazująca użycie wszystkich zaimplementowanych funkcji.
    
    Returns:
        dict: Słownik z wynikami demonstracji
    """
    results = {}
    

    test_email = "test@example.com"
    results['email_validation'] = validate_email(test_email)
    

    radius = 5
    results['circle_area'] = calculate_circle_area(radius)
    

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results['even_numbers'] = filter_even_numbers(numbers)
    

    date_input = "2023-12-25"
    results['converted_date'] = convert_date_format(date_input)
    

    test_text = "racecar"
    results['is_palindrome_result'] = is_palindrome(test_text)
    
    return results


if __name__ == "__main__":

    print("=== Demonstracja funkcji aplikacji ===")
    
    demo_results = run_demo()
    
    print(f"Email 'test@example.com' jest {'poprawny' if demo_results['email_validation'] else 'niepoprawny'}")
    print(f"Pole koła o promieniu 5 wynosi: {demo_results['circle_area']:.2f}")
    print(f"Liczby parzyste z listy [1-10]: {demo_results['even_numbers']}")
    print(f"Data 2023-12-25 skonwertowana: {demo_results['converted_date']}")
    print(f"Tekst 'racecar' {'jest' if demo_results['is_palindrome_result'] else 'nie jest'} palindromem")