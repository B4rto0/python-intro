"""
Moduł data_utils - narzędzia do przetwarzania danych
===================================================

Ten moduł zawiera funkcje i klasy do:
- Ładowania danych z plików CSV
- Filtrowania i grupowania danych
- Podstawowej manipulacji struktur danych
"""

import csv
from typing import List, Dict, Any, Optional, Union
from collections import defaultdict


def load_csv_data(filepath: str, delimiter: str = ',', 
                  encoding: str = 'utf-8') -> List[Dict[str, Any]]:
    """
    Ładuje dane z pliku CSV i zwraca jako listę słowników.
    
    Args:
        filepath (str): Ścieżka do pliku CSV
        delimiter (str): Separator kolumn (domyślnie ',')
        encoding (str): Kodowanie pliku (domyślnie 'utf-8')
    
    Returns:
        List[Dict[str, Any]]: Lista słowników reprezentujących wiersze
    
    Raises:
        FileNotFoundError: Gdy plik nie istnieje
        ValueError: Gdy plik ma nieprawidłowy format
    """
    try:
        data = []
        with open(filepath, 'r', encoding=encoding, newline='') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            for row in reader:
                # Konwersja numerycznych wartości
                processed_row = {}
                for key, value in row.items():
                    if value.isdigit():
                        processed_row[key] = int(value)
                    else:
                        try:
                            processed_row[key] = float(value)
                        except ValueError:
                            processed_row[key] = value
                data.append(processed_row)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Plik {filepath} nie został znaleziony")
    except Exception as e:
        raise ValueError(f"Błąd podczas czytania pliku: {str(e)}")


def filter_data(data: List[Dict[str, Any]], 
                conditions: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Filtruje dane na podstawie podanych warunków.
    
    Args:
        data (List[Dict[str, Any]]): Dane do filtrowania
        conditions (Dict[str, Any]): Słownik warunków {kolumna: wartość}
    
    Returns:
        List[Dict[str, Any]]: Przefiltrowane dane
    
    Example:
        >>> data = [{'name': 'Jan', 'age': 25}, {'name': 'Anna', 'age': 30}]
        >>> filter_data(data, {'age': 25})
        [{'name': 'Jan', 'age': 25}]
    """
    if not data or not conditions:
        return data
    
    filtered = []
    for row in data:
        match = True
        for key, value in conditions.items():
            if key not in row or row[key] != value:
                match = False
                break
        if match:
            filtered.append(row)
    
    return filtered


def group_by_column(data: List[Dict[str, Any]], 
                   column: str) -> Dict[Any, List[Dict[str, Any]]]:
    """
    Grupuje dane według wartości w określonej kolumnie.
    
    Args:
        data (List[Dict[str, Any]]): Dane do grupowania
        column (str): Nazwa kolumny do grupowania
    
    Returns:
        Dict[Any, List[Dict[str, Any]]]: Słownik grup
    
    Raises:
        KeyError: Gdy kolumna nie istnieje w danych
    """
    if not data:
        return {}
    
    if column not in data[0]:
        raise KeyError(f"Kolumna '{column}' nie istnieje w danych")
    
    groups = defaultdict(list)
    for row in data:
        groups[row[column]].append(row)
    
    return dict(groups)


class DataProcessor:
    """
    Klasa do zaawansowanego przetwarzania danych.
    
    Attributes:
        data (List[Dict[str, Any]]): Przechowywane dane
    """
    
    def __init__(self, data: Optional[List[Dict[str, Any]]] = None):
        """
        Inicjalizuje procesor danych.
        
        Args:
            data (Optional[List[Dict[str, Any]]]): Opcjonalne dane początkowe
        """
        self.data = data or []
    
    def load_from_csv(self, filepath: str, **kwargs) -> 'DataProcessor':
        """
        Ładuje dane z pliku CSV.
        
        Args:
            filepath (str): Ścieżka do pliku
            **kwargs: Dodatkowe argumenty dla load_csv_data
        
        Returns:
            DataProcessor: Zwraca siebie dla chaining
        """
        self.data = load_csv_data(filepath, **kwargs)
        return self
    
    def filter(self, conditions: Dict[str, Any]) -> 'DataProcessor':
        """
        Filtruje dane według warunków.
        
        Args:
            conditions (Dict[str, Any]): Warunki filtrowania
        
        Returns:
            DataProcessor: Zwraca siebie dla chaining
        """
        self.data = filter_data(self.data, conditions)
        return self
    
    def get_column_values(self, column: str) -> List[Any]:
        """
        Zwraca wszystkie wartości z określonej kolumny.
        
        Args:
            column (str): Nazwa kolumny
        
        Returns:
            List[Any]: Lista wartości
        
        Raises:
            KeyError: Gdy kolumna nie istnieje
        """
        if not self.data:
            return []
        
        if column not in self.data[0]:
            raise KeyError(f"Kolumna '{column}' nie istnieje w danych")
        
        return [row[column] for row in self.data if column in row]
    
    def get_unique_values(self, column: str) -> List[Any]:
        """
        Zwraca unikalne wartości z kolumny.
        
        Args:
            column (str): Nazwa kolumny
        
        Returns:
            List[Any]: Lista unikalnych wartości
        """
        values = self.get_column_values(column)
        return list(set(values))
    
    def count_rows(self) -> int:
        """
        Zwraca liczbę wierszy w danych.
        
        Returns:
            int: Liczba wierszy
        """
        return len(self.data)