"""
DataFlow - Biblioteka do przetwarzania i analizy danych
========================================================

Biblioteka zawiera narzędzia do:
- Przetwarzania i manipulacji danych (data_utils)
- Operacji matematycznych i statystycznych (math_tools)
- Przetwarzania tekstu i analizy (text_processing)
"""

from .data_utils import (
    load_csv_data,
    filter_data,
    group_by_column,
    DataProcessor
)

from .math_tools import (
    calculate_statistics,
    normalize_data,
    MathCalculator
)

from .text_processing import (
    clean_text,
    extract_keywords,
    TextAnalyzer
)



__all__ = [
    'load_csv_data', 'filter_data', 'group_by_column', 'DataProcessor',
    'calculate_statistics', 'normalize_data', 'MathCalculator',
    'clean_text', 'extract_keywords', 'TextAnalyzer'
]