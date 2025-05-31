# DataFlow - Biblioteka do przetwarzania i analizy danych

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)


DataFlow to wszechstronna biblioteka Python do przetwarzania danych, obliczeń matematycznych i analizy tekstu. Została zaprojektowana z myślą o łatwości użycia i wysokiej funkcjonalności.

## 🚀 Główne funkcjonalności

### 📊 Przetwarzanie danych (`data_utils`)
- Ładowanie danych z plików CSV
- Filtrowanie i grupowanie danych
- Klasa `DataProcessor` do zaawansowanej manipulacji danych

### 🔢 Narzędzia matematyczne (`math_tools`)
- Obliczenia statystyczne (średnia, mediana, odchylenie standardowe)
- Normalizacja danych (min-max, z-score)
- Obliczanie korelacji Pearsona
- Klasa `MathCalculator` z funkcjami matematycznymi (silnia, Fibonacci, liczby pierwsze)

### 📝 Przetwarzanie tekstu (`text_processing`)
- Czyszczenie i normalizacja tekstu
- Wyodrębnianie słów kluczowych
- Klasa `TextAnalyzer` do zaawansowanej analizy tekstu
- Statystyki czytelności




### Wymagania
- Python 3.7+
- Brak zewnętrznych dependencji (używa tylko biblioteki standardowej)

## 🔧 Szybki start

### Przetwarzanie danych
```python
from dataflow import DataProcessor, load_csv_data, filter_data

# Ładowanie danych z CSV
data = load_csv_data('dane.csv')

# Filtrowanie danych
filtered = filter_data(data, {'age': 25, 'city': 'Warszawa'})

# Użycie DataProcessor z chainingiem
processor = DataProcessor()
result = processor.load_from_csv('dane.csv').filter({'age': 25}).data
```

### Obliczenia matematyczne
```python
from dataflow import calculate_statistics, normalize_data, MathCalculator

# Statystyki
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = calculate_statistics(data)
print(f"Średnia: {stats['mean']}, Mediana: {stats['median']}")

# Normalizacja
normalized = normalize_data(data, method='min-max')

# Funkcje matematyczne
calc = MathCalculator()
print(f"5! = {calc.factorial(5)}")
print(f"10. liczba Fibonacciego: {calc.fibonacci(10)}")
print(f"Czy 17 jest liczbą pierwszą? {calc.is_prime(17)}")
```

### Analiza tekstu
```python
from dataflow import TextAnalyzer, clean_text, extract_keywords

# Czyszczenie tekstu
tekst = "Hello, World! This is a TEST text with numbers 123."
czysty = clean_text(tekst)
print(czysty)  # "hello world this is a test text with numbers"

# Słowa kluczowe
keywords = extract_keywords(tekst, max_keywords=5)
print(keywords)

# Zaawansowana analiza
analyzer = TextAnalyzer(tekst)
stats = analyzer.get_readability_stats()
print(f"Liczba słów: {stats['word_count']}")
print(f"Średnia długość słowa: {stats['avg_word_length']}")
```

## 📚 Dokumentacja API

### data_utils

#### Funkcje
- `load_csv_data(filepath, delimiter=',', encoding='utf-8')` - Ładuje dane z pliku CSV
- `filter_data(data, conditions)` - Filtruje dane według warunków
- `group_by_column(data, column)` - Grupuje dane według kolumny

#### Klasa DataProcessor
- `load_from_csv(filepath)` - Ładuje dane z CSV
- `filter(conditions)` - Filtruje dane
- `get_column_values(column)` - Pobiera wartości kolumny
- `get_unique_values(column)` - Pobiera unikalne wartości
- `count_rows()` - Liczy wiersze

### math_tools

#### Funkcje
- `calculate_statistics(data)` - Oblicza statystyki opisowe
- `normalize_data(data, method='min-max')` - Normalizuje dane
- `calculate_correlation(x, y)` - Oblicza korelację Pearsona

#### Klasa MathCalculator
- `factorial(n)` - Oblicza silnię
- `fibonacci(n)` - N-ty element ciągu Fibonacciego
- `is_prime(n)` - Sprawdza czy liczba jest pierwsza
- `gcd(a, b)` - Największy wspólny dzielnik
- `lcm(a, b)` - Najmniejsza wspólna wielokrotność

### text_processing

#### Funkcje
- `clean_text(text, **options)` - Czyści tekst
- `extract_keywords(text, min_length=3, max_keywords=None)` - Wyodrębnia słowa kluczowe
- `count_words(text)` - Liczy wystąpienia słów

#### Klasa TextAnalyzer
- `set_text(text)` - Ustawia tekst do analizy
- `get_word_count()` - Liczy słowa
- `get_character_count(include_spaces=True)` - Liczy znaki
- `get_sentence_count()` - Liczy zdania
- `get_most_common_words(n=10)` - Najczęstsze słowa
- `find_patterns(pattern)` - Znajduje wzorce regex
- `get_readability_stats()` - Statystyki czytelności

## 🧪 Testy

Biblioteka zawiera kompletny zestaw testów jednostkowych:

```bash
# Uruchomienie wszystkich testów
python -m pytest tests/

# Uruchomienie testów dla konkretnego modułu
python -m pytest tests/test_data_utils.py
python -m pytest tests/test_math_tools.py
python -m pytest tests/test_text_processing.py

# Z pokryciem kodu
python -m pytest tests/ --cov=dataflow
```

## 📁 Struktura projektu

```
dataflow/
├── dataflow/
│   ├── __init__.py
│   ├── data_utils.py
│   ├── math_tools.py
│   └── text_processing.py
├── tests/
│   ├── test_data_utils.py
│   ├── test_math_tools.py
│   └── test_text_processing.py
├── README.md
├── setup.py (opcjonalnie)
└── .gitignore
```




### Uruchomienie testów
```bash
# Wszystkie testy
python -m pytest

# Z verbose output
python -m pytest -v

# Z pokryciem kodu
python -m pytest --cov=dataflow --cov-report=html
```

### Formatowanie kodu
```bash
# Instalacja narzędzi (opcjonalnie)
pip install black flake8 pylint

# Formatowanie
black dataflow/

# Linting
flake8 dataflow/
pylint dataflow/
```


**DataFlow** - Twoje narzędzie do efektywnego przetwarzania danych w Python! 🐍✨