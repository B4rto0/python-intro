#!/usr/bin/env python3
"""
Przykład użycia biblioteki DataFlow
===================================

Ten plik demonstruje podstawowe funkcjonalności wszystkich modułów biblioteki.
"""

from dataflow import (
    # Data utils
    DataProcessor, load_csv_data, filter_data, group_by_column,
    # Math tools
    calculate_statistics, normalize_data, calculate_correlation, MathCalculator,
    # Text processing
    clean_text, extract_keywords, count_words, TextAnalyzer
)

def demo_data_processing():
    """Demonstracja przetwarzania danych"""
    print("=" * 50)
    print("DEMONSTRACJA PRZETWARZANIA DANYCH")
    print("=" * 50)
    
    # Przykładowe dane
    sample_data = [
        {'name': 'Jan', 'age': 25, 'city': 'Warszawa', 'salary': 5000},
        {'name': 'Anna', 'age': 30, 'city': 'Kraków', 'salary': 6000},
        {'name': 'Piotr', 'age': 25, 'city': 'Warszawa', 'salary': 5500},
        {'name': 'Maria', 'age': 35, 'city': 'Gdańsk', 'salary': 7000},
        {'name': 'Tomasz', 'age': 28, 'city': 'Kraków', 'salary': 5800}
    ]
    
    print("Dane początkowe:")
    for row in sample_data:
        print(f"  {row}")
    
    # Filtrowanie danych
    young_people = filter_data(sample_data, {'age': 25})
    print(f"\nOsoby w wieku 25 lat: {len(young_people)}")
    for person in young_people:
        print(f"  {person['name']} z {person['city']}")
    
    # Grupowanie danych
    by_city = group_by_column(sample_data, 'city')
    print(f"\nGrupowanie według miast:")
    for city, people in by_city.items():
        print(f"  {city}: {len(people)} osób")
    
    # Użycie DataProcessor
    processor = DataProcessor(sample_data)
    warsaw_people = processor.filter({'city': 'Warszawa'})
    
    print(f"\nOsoby z Warszawy (DataProcessor): {processor.count_rows()}")
    salaries = processor.get_column_values('salary')
    print(f"Pensje w Warszawie: {salaries}")
    
    unique_cities = DataProcessor(sample_data).get_unique_values('city')
    print(f"Unikalne miasta: {unique_cities}")


def demo_math_tools():
    """Demonstracja narzędzi matematycznych"""
    print("\n" + "=" * 50)
    print("DEMONSTRACJA NARZĘDZI MATEMATYCZNYCH")
    print("=" * 50)
    
    # Dane do analizy
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data2 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    
    print(f"Dane 1: {data1}")
    print(f"Dane 2: {data2}")
    
    # Statystyki opisowe
    stats1 = calculate_statistics(data1)
    print(f"\nStatystyki dla danych 1:")
    print(f"  Średnia: {stats1['mean']:.2f}")
    print(f"  Mediana: {stats1['median']}")
    print(f"  Odchylenie standardowe: {stats1['std']:.2f}")
    print(f"  Min: {stats1['min']}, Max: {stats1['max']}")
    
    # Normalizacja danych
    normalized_minmax = normalize_data(data1, 'min-max')
    normalized_zscore = normalize_data(data1, 'z-score')
    
    print(f"\nNormalizacja min-max (pierwsze 5): {normalized_minmax[:5]}")
    print(f"Normalizacja z-score (pierwsze 5): {[round(x, 3) for x in normalized_zscore[:5]]}")
    
    # Korelacja
    correlation = calculate_correlation(data1, data2)
    print(f"\nKorelacja między data1 i data2: {correlation:.4f}")
    
    # MathCalculator
    calc = MathCalculator()
    print(f"\nFunkcje matematyczne:")
    print(f"  5! = {calc.factorial(5)}")
    print(f"  10. liczba Fibonacciego: {calc.fibonacci(10)}")
    print(f"  Czy 17 jest liczbą pierwszą? {calc.is_prime(17)}")
    print(f"  NWD(48, 18) = {calc.gcd(48, 18)}")
    print(f"  NWW(12, 15) = {calc.lcm(12, 15)}")


def demo_text_processing():
    """Demonstracja przetwarzania tekstu"""
    print("\n" + "=" * 50)
    print("DEMONSTRACJA PRZETWARZANIA TEKSTU")
    print("=" * 50)
    
    # Przykładowy tekst
    sample_text = """
    Witaj w świecie programowania w Pythonie! Python jest językiem programowania 
    wysokiego poziomu. Jest łatwy do nauki i bardzo wszechstronny. Python może być 
    używany do tworzenia stron internetowych, analizy danych, sztucznej inteligencji 
    i wielu innych zastosowań. Programowanie w Pythonie jest przyjemne!
    """
    
    print(f"Tekst oryginalny:\n{sample_text}")
    
    # Czyszczenie tekstu
    cleaned = clean_text(sample_text)
    print(f"\nTekst oczyszczony:\n{cleaned}")
    
    # Słowa kluczowe
    keywords = extract_keywords(sample_text, max_keywords=10)
    print(f"\nSłowa kluczowe (10 najważniejszych):")
    for i, keyword in enumerate(keywords, 1):
        print(f"  {i}. {keyword}")
    
    # Liczenie słów
    word_counts = count_words(sample_text)
    most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"\nNajczęściej występujące słowa:")
    for word, count in most_common:
        print(f"  '{word}': {count} razy")
    
    # TextAnalyzer
    analyzer = TextAnalyzer(sample_text)
    stats = analyzer.get_readability_stats()
    
    print(f"\nStatystyki czytelności:")
    print(f"  Liczba słów: {stats['word_count']}")
    print(f"  Liczba zdań: {stats['sentence_count']}")
    print(f"  Średnia długość słowa: {stats['avg_word_length']:.2f} znaków")
    print(f"  Średnia długość zdania: {stats['avg_sentence_length']:.2f} słów")
    
    # Wyszukiwanie wzorców
    python_mentions = analyzer.find_patterns(r'[Pp]ython[a-z]*')
    print(f"\nWzmiany o Python*: {python_mentions}")
    
    # Najczęstsze słowa
    most_common_words = analyzer.get_most_common_words(5)
    print(f"\nNajczęstsze słowa (TextAnalyzer):")
    for word, count in most_common_words:
        print(f"  '{word}': {count}")


def demo_advanced_usage():
    """Demonstracja zaawansowanego użycia - łączenie modułów"""
    print("\n" + "=" * 50)
    print("DEMONSTRACJA ZAAWANSOWANEGO UŻYCIA")
    print("=" * 50)
    
    # Symulacja analizy danych z tekstu
    text_data = [
        "Excellent product, highly recommended! Quality is amazing.",
        "Good value for money. Service could be better.",
        "Poor quality, not worth the price. Disappointed.",
        "Amazing experience! Will definitely buy again.",
        "Average product, nothing special but okay."
    ]
    
    print("Analiza opinii klientów:")
    print("-" * 30)
    
    # Analiza każdej opinii
    sentiment_scores = []
    all_keywords = []
    
    for i, review in enumerate(text_data, 1):
        analyzer = TextAnalyzer(review)
        stats = analyzer.get_readability_stats()
        keywords = extract_keywords(review, min_length=4, max_keywords=3)
        
        # Prosty scoring sentymentu na podstawie pozytywnych/negatywnych słów
        positive_words = ['excellent', 'amazing', 'good', 'definitely', 'recommended']
        negative_words = ['poor', 'disappointed', 'bad', 'terrible']
        
        cleaned_review = clean_text(review)
        words = cleaned_review.split()
        
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)
        sentiment = positive_count - negative_count
        
        sentiment_scores.append(sentiment)
        all_keywords.extend(keywords)
        
        print(f"Opinia {i}:")
        print(f"  Tekst: {review}")
        print(f"  Liczba słów: {stats['word_count']}")
        print(f"  Słowa kluczowe: {keywords}")
        print(f"  Sentyment: {sentiment} ({'pozytywny' if sentiment > 0 else 'negatywny' if sentiment < 0 else 'neutralny'})")
        print()
    
    # Analiza zagregowana
    stats = calculate_statistics(sentiment_scores)
    print(f"Statystyki sentymentu:")
    print(f"  Średni sentyment: {stats['mean']:.2f}")
    print(f"  Mediana: {stats['median']}")
    print(f"  Zakres: {stats['min']} do {stats['max']}")
    
    # Najczęstsze słowa kluczowe
    keyword_counts = count_words(' '.join(all_keywords))
    top_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    
    print(f"\nNajczęstsze słowa kluczowe we wszystkich opiniach:")
    for keyword, count in top_keywords:
        print(f"  '{keyword}': {count} razy")


def main():
    """Główna funkcja demonstracyjna"""
    print("BIBLIOTEKA DATAFLOW - DEMONSTRACJA FUNKCJONALNOŚCI")
    print("=" * 60)
    
    try:
        demo_data_processing()
        demo_math_tools()
        demo_text_processing()
        demo_advanced_usage()
        
        print("\n" + "=" * 60)
        print("DEMONSTRACJA ZAKOŃCZONA POMYŚLNIE!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nBłąd podczas demonstracji: {e}")
        print("Sprawdź czy wszystkie moduły są poprawnie zainstalowane.")


if __name__ == "__main__":
    main()