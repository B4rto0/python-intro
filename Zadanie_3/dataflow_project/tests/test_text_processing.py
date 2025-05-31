"""
Testy jednostkowe dla modułu text_processing
"""

import unittest
from dataflow.text_processing import (
    clean_text, extract_keywords, count_words, TextAnalyzer
)


class TestTextProcessing(unittest.TestCase):
    
    def setUp(self):
        """Przygotowanie danych testowych"""
        self.sample_text = "Hello, World! This is a test text with numbers 123."
        self.polish_text = "To jest przykładowy tekst w języku polskim. Zawiera różne słowa."
    
    def test_clean_text_default(self):
        """Test domyślnego czyszczenia tekstu"""
        result = clean_text(self.sample_text)
        expected = "hello world this is a test text with numbers 123"
        self.assertEqual(result, expected)
    
    def test_clean_text_keep_punctuation(self):
        """Test czyszczenia z zachowaniem interpunkcji"""
        result = clean_text(self.sample_text, remove_punctuation=False)
        expected = "hello, world! this is a test text with numbers 123."
        self.assertEqual(result, expected)
    
    def test_clean_text_keep_case(self):
        """Test czyszczenia z zachowaniem wielkości liter"""
        result = clean_text(self.sample_text, to_lowercase=False)
        expected = "Hello World This is a test text with numbers 123"
        self.assertEqual(result, expected)
    
    def test_clean_text_remove_digits(self):
        """Test czyszczenia z usunięciem cyfr"""
        result = clean_text(self.sample_text, remove_digits=True)
        expected = "hello world this is a test text with numbers"
        self.assertEqual(result, expected)
    
    def test_clean_text_invalid_input(self):
        """Test czyszczenia z nieprawidłowym wejściem"""
        with self.assertRaises(TypeError):
            clean_text(123)
    
    def test_extract_keywords_basic(self):
        """Test podstawowego wyodrębniania słów kluczowych"""
        keywords = extract_keywords(self.sample_text)
        
        # Sprawdzenie czy zawiera oczekiwane słowa
        self.assertIn("hello", keywords)
        self.assertIn("world", keywords)
        self.assertIn("test", keywords)
        self.assertIn("text", keywords)
        
        # Sprawdzenie czy nie zawiera słów pomijanych
        self.assertNotIn("is", keywords)
        self.assertNotIn("a", keywords)
    
    def test_extract_keywords_min_length(self):
        """Test wyodrębniania z minimalną długością"""
        keywords = extract_keywords(self.sample_text, min_length=5)
        
        # Tylko słowa o długości >= 5
        self.assertTrue(all(len(word) >= 5 for word in keywords))
        self.assertIn("hello", keywords)
        self.assertIn("world", keywords)
        self.assertIn("numbers", keywords)
    
    def test_extract_keywords_max_keywords(self):
        """Test ograniczenia liczby słów kluczowych"""
        keywords = extract_keywords(self.sample_text, max_keywords=3)
        self.assertEqual(len(keywords), 3)
    
    def test_extract_keywords_custom_stop_words(self):
        """Test z niestandardowymi słowami pomijanymi"""
        custom_stop_words = {"hello", "world"}
        keywords = extract_keywords(self.sample_text, stop_words=custom_stop_words)
        
        self.assertNotIn("hello", keywords)
        self.assertNotIn("world", keywords)
    
    def test_extract_keywords_invalid_input(self):
        """Test wyodrębniania z nieprawidłowym wejściem"""
        with self.assertRaises(TypeError):
            extract_keywords(123)
    
    def test_count_words(self):
        """Test liczenia słów"""
        word_counts = count_words("hello world hello test")
        
        expected = {"hello": 2, "world": 1, "test": 1}
        self.assertEqual(word_counts, expected)
    
    def test_count_words_empty(self):
        """Test liczenia słów w pustym tekście"""
        word_counts = count_words("")
        self.assertEqual(word_counts, {})
    
    def test_count_words_invalid_input(self):
        """Test liczenia słów z nieprawidłowym wejściem"""
        with self.assertRaises(TypeError):
            count_words(None)


class TestTextAnalyzer(unittest.TestCase):
    
    def setUp(self):
        """Przygotowanie danych testowych"""
        self.sample_text = "Hello world! This is a test. Another sentence here."
        self.analyzer = TextAnalyzer(self.sample_text)
    
    def test_init_with_text(self):
        """Test inicjalizacji z tekstem"""
        self.assertEqual(self.analyzer.text, self.sample_text)
    
    def test_init_without_text(self):
        """Test inicjalizacji bez tekstu"""
        analyzer = TextAnalyzer()
        self.assertEqual(analyzer.text, "")
    
    def test_set_text_chaining(self):
        """Test ustawiania tekstu z chainingiem"""
        result = self.analyzer.set_text("New text")
        self.assertIsInstance(result, TextAnalyzer)
        self.assertEqual(self.analyzer.text, "New text")
    
    def test_get_cleaned_text(self):
        """Test pobierania oczyszczonego tekstu"""
        cleaned = self.analyzer.get_cleaned_text()
        expected = "hello world this is a test another sentence here"
        self.assertEqual(cleaned, expected)
    
    def test_get_word_count(self):
        """Test liczenia słów"""
        word_count = self.analyzer.get_word_count()
        self.assertEqual(word_count, 9)  # po oczyszczeniu
    
    def test_get_word_count_empty(self):
        """Test liczenia słów w pustym tekście"""
        analyzer = TextAnalyzer("")
        self.assertEqual(analyzer.get_word_count(), 0)
    
    def test_get_character_count(self):
        """Test liczenia znaków"""
        char_count_with_spaces = self.analyzer.get_character_count(include_spaces=True)
        char_count_without_spaces = self.analyzer.get_character_count(include_spaces=False)
        
        self.assertEqual(char_count_with_spaces, len(self.sample_text))
        self.assertLess(char_count_without_spaces, char_count_with_spaces)
    
    def test_get_sentence_count(self):
        """Test liczenia zdań"""
        sentence_count = self.analyzer.get_sentence_count()
        # Tekst: "Hello world! This is a test. Another sentence here."
        # 3 zdania: "Hello world!" + "This is a test." + "Another sentence here."
        self.assertEqual(sentence_count, 3)
    
    def test_get_most_common_words(self):
        """Test najczęstszych słów"""
        most_common = self.analyzer.get_most_common_words(3)
        self.assertEqual(len(most_common), 3)
        
        # Sprawdzenie struktury wyników
        for word, count in most_common:
            self.assertIsInstance(word, str)
            self.assertIsInstance(count, int)
            self.assertGreater(count, 0)
    
    def test_find_patterns(self):
        """Test znajdowania wzorców"""
        # Znajdowanie słów zaczynających się na wielką literę
        patterns = self.analyzer.find_patterns(r'\b[A-Z][a-z]+')
        self.assertIn("Hello", patterns)
        self.assertIn("This", patterns)
        self.assertIn("Another", patterns)
    
    def test_find_patterns_invalid_regex(self):
        """Test nieprawidłowego wzorca regex"""
        with self.assertRaises(ValueError):
            self.analyzer.find_patterns('[invalid regex')
    
    def test_get_readability_stats(self):
        """Test statystyk czytelności"""
        stats = self.analyzer.get_readability_stats()
        
        # Sprawdzenie struktury wyników
        expected_keys = ['avg_word_length', 'avg_sentence_length', 'word_count', 'sentence_count']
        for key in expected_keys:
            self.assertIn(key, stats)
        
        # Sprawdzenie typów wartości
        self.assertIsInstance(stats['avg_word_length'], float)
        self.assertIsInstance(stats['avg_sentence_length'], float)
        self.assertIsInstance(stats['word_count'], int)
        self.assertIsInstance(stats['sentence_count'], int)
        
        # Sprawdzenie wartości logicznych
        self.assertGreater(stats['word_count'], 0)
        self.assertGreater(stats['sentence_count'], 0)
        self.assertGreater(stats['avg_word_length'], 0)
    
    def test_get_readability_stats_empty_text(self):
        """Test statystyk dla pustego tekstu"""
        analyzer = TextAnalyzer("")
        stats = analyzer.get_readability_stats()
        
        expected = {
            'avg_word_length': 0.0,
            'avg_sentence_length': 0.0,
            'word_count': 0,
            'sentence_count': 0
        }
        
        self.assertEqual(stats, expected)


if __name__ == '__main__':
    unittest.main()