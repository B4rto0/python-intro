"""
Moduł text_processing - narzędzia do przetwarzania tekstu
========================================================

Ten moduł zawiera funkcje i klasy do:
- Czyszczenia i normalizacji tekstu
- Analizy tekstu i wyodrębniania słów kluczowych
- Podstawowych operacji na ciągach znaków
"""

import re
import string
from typing import List, Dict, Set, Optional
from collections import Counter


def clean_text(text: str, remove_punctuation: bool = True, 
               to_lowercase: bool = True, remove_digits: bool = False) -> str:
    """
    Czyści tekst z niepotrzebnych znaków i normalizuje go.
    
    Args:
        text (str): Tekst do oczyszczenia
        remove_punctuation (bool): Czy usunąć znaki interpunkcyjne
        to_lowercase (bool): Czy przekonwertować na małe litery
        remove_digits (bool): Czy usunąć cyfry
    
    Returns:
        str: Oczyszczony tekst
    
    Example:
        >>> clean_text("Hello, World! 123")
        'hello world'
    """
    if not isinstance(text, str):
        raise TypeError("Argument musi być typu string")
    
    # Konwersja na małe litery
    if to_lowercase:
        text = text.lower()
    
    # Usunięcie cyfr
    if remove_digits:
        text = re.sub(r'\d+', '', text)
    
    # Usunięcie znaków interpunkcyjnych
    if remove_punctuation:
        text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Usunięcie nadmiarowych spacji
    text = ' '.join(text.split())
    
    return text


def extract_keywords(text: str, min_length: int = 3, 
                    max_keywords: Optional[int] = None,
                    stop_words: Optional[Set[str]] = None) -> List[str]:
    """
    Wyodrębnia słowa kluczowe z tekstu.
    
    Args:
        text (str): Tekst do analizy
        min_length (int): Minimalna długość słowa
        max_keywords (Optional[int]): Maksymalna liczba słów kluczowych
        stop_words (Optional[Set[str]]): Zbiór słów do pominięcia
    
    Returns:
        List[str]: Lista słów kluczowych posortowana według częstotliwości
    """
    if not isinstance(text, str):
        raise TypeError("Argument musi być typu string")
    
    # Domyślne słowa pomijane (polskie i angielskie)
    default_stop_words = {
        'i', 'a', 'w', 'z', 'na', 'do', 'o', 'się', 'to', 'że', 'lub', 'oraz',
        'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with'
    }
    
    if stop_words is None:
        stop_words = default_stop_words
    else:
        stop_words = stop_words.union(default_stop_words)
    
    # Oczyszczenie tekstu
    cleaned = clean_text(text, remove_punctuation=True, to_lowercase=True)
    
    # Podział na słowa i filtrowanie
    words = [
        word for word in cleaned.split()
        if len(word) >= min_length and word not in stop_words
    ]
    
    # Liczenie częstotliwości
    word_freq = Counter(words)
    
    # Sortowanie według częstotliwości
    keywords = [word for word, freq in word_freq.most_common()]
    
    # Ograniczenie liczby słów kluczowych
    if max_keywords:
        keywords = keywords[:max_keywords]
    
    return keywords


def count_words(text: str) -> Dict[str, int]:
    """
    Liczy wystąpienia słów w tekście.
    
    Args:
        text (str): Tekst do analizy
    
    Returns:
        Dict[str, int]: Słownik {słowo: liczba_wystąpień}
    """
    if not isinstance(text, str):
        raise TypeError("Argument musi być typu string")
    
    cleaned = clean_text(text)
    words = cleaned.split()
    
    return dict(Counter(words))


class TextAnalyzer:
    """
    Klasa do zaawansowanej analizy tekstu.
    
    Attributes:
        text (str): Analizowany tekst
    """
    
    def __init__(self, text: str = ""):
        """
        Inicjalizuje analizator tekstu.
        
        Args:
            text (str): Tekst do analizy
        """
        self.text = text
        self._cleaned_text = None
    
    def set_text(self, text: str) -> 'TextAnalyzer':
        """
        Ustawia nowy tekst do analizy.
        
        Args:
            text (str): Nowy tekst
        
        Returns:
            TextAnalyzer: Zwraca siebie dla chaining
        """
        self.text = text
        self._cleaned_text = None  # Reset cache
        return self
    
    def get_cleaned_text(self) -> str:
        """
        Zwraca oczyszczony tekst (z cache).
        
        Returns:
            str: Oczyszczony tekst
        """
        if self._cleaned_text is None:
            self._cleaned_text = clean_text(self.text)
        return self._cleaned_text
    
    def get_word_count(self) -> int:
        """
        Zwraca liczbę słów w tekście.
        
        Returns:
            int: Liczba słów
        """
        cleaned = self.get_cleaned_text()
        return len(cleaned.split()) if cleaned else 0
    
    def get_character_count(self, include_spaces: bool = True) -> int:
        """
        Zwraca liczbę znaków w tekście.
        
        Args:
            include_spaces (bool): Czy liczyć spacje
        
        Returns:
            int: Liczba znaków
        """
        text_to_count = self.text if include_spaces else self.text.replace(' ', '')
        return len(text_to_count)
    
    def get_sentence_count(self) -> int:
        """
        Zwraca liczbę zdań w tekście.
        
        Returns:
            int: Liczba zdań
        """
        # Proste zliczanie na podstawie znaków interpunkcyjnych
        sentence_endings = re.findall(r'[.!?]+', self.text)
        return len(sentence_endings)
    
    def get_most_common_words(self, n: int = 10) -> List[tuple]:
        """
        Zwraca najczęściej występujące słowa.
        
        Args:
            n (int): Liczba słów do zwrócenia
        
        Returns:
            List[tuple]: Lista krotek (słowo, liczba_wystąpień)
        """
        word_counts = count_words(self.text)
        return Counter(word_counts).most_common(n)
    
    def find_patterns(self, pattern: str) -> List[str]:
        """
        Znajduje wszystkie wystąpienia wzorca w tekście.
        
        Args:
            pattern (str): Wzorzec regex
        
        Returns:
            List[str]: Lista znalezionych wystąpień
        """
        try:
            return re.findall(pattern, self.text)
        except re.error as e:
            raise ValueError(f"Nieprawidłowy wzorzec regex: {e}")
    
    def get_readability_stats(self) -> Dict[str, float]:
        """
        Zwraca podstawowe statystyki czytelności tekstu.
        
        Returns:
            Dict[str, float]: Statystyki czytelności
        """
        word_count = self.get_word_count()
        char_count = self.get_character_count(include_spaces=False)
        sentence_count = self.get_sentence_count()
        
        if word_count == 0:
            return {
                'avg_word_length': 0.0,
                'avg_sentence_length': 0.0,
                'word_count': 0,
                'sentence_count': 0
            }
        
        avg_word_length = char_count / word_count if word_count > 0 else 0
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else word_count
        
        return {
            'avg_word_length': round(avg_word_length, 2),
            'avg_sentence_length': round(avg_sentence_length, 2),
            'word_count': word_count,
            'sentence_count': sentence_count
        }