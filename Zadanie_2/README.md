# Zadanie 2 - Test-Driven Development (TDD)

## Opis
Projekt implementuje 5 funkcji z wykorzystaniem podejścia Test-Driven Development w Pythonie.

## Pliki
- `app.py` - implementacja funkcji
- `test_app.py` - testy jednostkowe
- `README.md` - dokumentacja

## Funkcje

### 1. validate_email(email)
Sprawdza poprawność adresu e-mail.

### 2. calculate_circle_area(radius)
Oblicza pole koła na podstawie promienia.

### 3. filter_even_numbers(numbers)
Filtruje listę zwracając tylko liczby parzyste.

### 4. convert_date_format(date_string)
Konwertuje datę z formatu YYYY-MM-DD na DD/MM/YYYY.

### 5. is_palindrome(text)
Sprawdza czy tekst jest palindromem.

## Uruchamianie testów

```bash
python test_app.py
```

lub

```bash
python -m unittest test_app.py -v
```

## Pokrycie testów

Instalacja:
```bash
pip install coverage
```

Uruchomienie:
```bash
coverage run test_app.py
coverage report
```

## Demonstracja
```bash
python app.py
```