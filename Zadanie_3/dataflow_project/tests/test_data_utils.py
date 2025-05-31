"""
Testy jednostkowe dla modułu data_utils
"""

import unittest
import tempfile
import os
from dataflow.data_utils import (
    load_csv_data, filter_data, group_by_column, DataProcessor
)


class TestDataUtils(unittest.TestCase):
    
    def setUp(self):
        """Przygotowanie danych testowych"""
        self.sample_data = [
            {'name': 'Jan', 'age': 25, 'city': 'Warszawa'},
            {'name': 'Anna', 'age': 30, 'city': 'Kraków'},
            {'name': 'Piotr', 'age': 25, 'city': 'Warszawa'},
            {'name': 'Maria', 'age': 35, 'city': 'Gdańsk'}
        ]
    
    def test_load_csv_data_success(self):
        """Test poprawnego ładowania danych CSV"""
        # Utworzenie tymczasowego pliku CSV
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write('name,age,city\n')
            f.write('Jan,25,Warszawa\n')
            f.write('Anna,30,Kraków\n')
            temp_file = f.name
        
        try:
            data = load_csv_data(temp_file)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]['name'], 'Jan')
            self.assertEqual(data[0]['age'], 25)
            self.assertEqual(data[1]['name'], 'Anna')
            self.assertEqual(data[1]['age'], 30)
        finally:
            os.unlink(temp_file)
    
    def test_load_csv_data_file_not_found(self):
        """Test obsługi błędu gdy plik nie istnieje"""
        with self.assertRaises(FileNotFoundError):
            load_csv_data('nieistniejacy_plik.csv')
    
    def test_filter_data_single_condition(self):
        """Test filtrowania z jednym warunkiem"""
        result = filter_data(self.sample_data, {'age': 25})
        self.assertEqual(len(result), 2)
        self.assertTrue(all(row['age'] == 25 for row in result))
    
    def test_filter_data_multiple_conditions(self):
        """Test filtrowania z wieloma warunkami"""
        result = filter_data(self.sample_data, {'age': 25, 'city': 'Warszawa'})
        self.assertEqual(len(result), 2)
        self.assertTrue(all(row['age'] == 25 and row['city'] == 'Warszawa' for row in result))
    
    def test_filter_data_no_match(self):
        """Test filtrowania gdy brak dopasowań"""
        result = filter_data(self.sample_data, {'age': 100})
        self.assertEqual(len(result), 0)
    
    def test_filter_data_empty_conditions(self):
        """Test filtrowania z pustymi warunkami"""
        result = filter_data(self.sample_data, {})
        self.assertEqual(result, self.sample_data)
    
    def test_group_by_column_success(self):
        """Test poprawnego grupowania danych"""
        result = group_by_column(self.sample_data, 'city')
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result['Warszawa']), 2)
        self.assertEqual(len(result['Kraków']), 1)
        self.assertEqual(len(result['Gdańsk']), 1)
    
    def test_group_by_column_nonexistent(self):
        """Test grupowania po nieistniejącej kolumnie"""
        with self.assertRaises(KeyError):
            group_by_column(self.sample_data, 'nonexistent')
    
    def test_group_by_column_empty_data(self):
        """Test grupowania pustych danych"""
        result = group_by_column([], 'any_column')
        self.assertEqual(result, {})


class TestDataProcessor(unittest.TestCase):
    
    def setUp(self):
        """Przygotowanie danych testowych"""
        self.sample_data = [
            {'name': 'Jan', 'age': 25, 'score': 85.5},
            {'name': 'Anna', 'age': 30, 'score': 92.0},
            {'name': 'Piotr', 'age': 25, 'score': 78.5}
        ]
        self.processor = DataProcessor(self.sample_data)
    
    def test_init_with_data(self):
        """Test inicjalizacji z danymi"""
        self.assertEqual(len(self.processor.data), 3)
    
    def test_init_without_data(self):
        """Test inicjalizacji bez danych"""
        processor = DataProcessor()
        self.assertEqual(len(processor.data), 0)
    
    def test_filter_chaining(self):
        """Test chainingu metod filtrowania"""
        result = self.processor.filter({'age': 25})
        self.assertIsInstance(result, DataProcessor)
        self.assertEqual(len(self.processor.data), 2)
    
    def test_get_column_values(self):
        """Test pobierania wartości kolumny"""
        ages = self.processor.get_column_values('age')
        self.assertEqual(sorted(ages), [25, 25, 30])
    
    def test_get_column_values_nonexistent(self):
        """Test pobierania wartości nieistniejącej kolumny"""
        with self.assertRaises(KeyError):
            self.processor.get_column_values('nonexistent')
    
    def test_get_unique_values(self):
        """Test pobierania unikalnych wartości"""
        unique_ages = self.processor.get_unique_values('age')
        self.assertEqual(sorted(unique_ages), [25, 30])
    
    def test_count_rows(self):
        """Test liczenia wierszy"""
        self.assertEqual(self.processor.count_rows(), 3)
        
        # Po filtrowaniu
        self.processor.filter({'age': 25})
        self.assertEqual(self.processor.count_rows(), 2)


if __name__ == '__main__':
    unittest.main()