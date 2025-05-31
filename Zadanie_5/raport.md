# Raport - Biblioteki do przetwarzania obrazów w Python

## Wybrana dziedzina
Przetwarzanie obrazów - biblioteki umożliwiające manipulację, edycję i analizę obrazów cyfrowych.

## Przebadane biblioteki

### 1. Pillow (PIL)

**Nazwa:** Pillow (Python Imaging Library)  
**Przeznaczenie:** Podstawowe operacje na obrazach - otwieranie, zapisywanie, zmiana rozmiaru, filtry, konwersje formatów.

**Główne funkcje:**
- Obsługa wielu formatów obrazów (JPEG, PNG, GIF, BMP)
- Zmiana rozmiaru i obracanie obrazów
- Stosowanie filtrów (rozmycie, wyostrzenie)
- Regulacja jasności, kontrastu i nasycenia
- Operacje na pikselach

**Zalety:**
- Prosta instalacja i użytkowanie
- Bogata dokumentacja
- Lekka biblioteka
- Dobra dla podstawowych operacji
- Aktywnie rozwijana

**Ograniczenia:**
- Ograniczone możliwości zaawansowanej analizy
- Brak funkcji sztucznej inteligencji
- Mniej wydajna przy dużych obrazach

**Dokumentacja:** https://pillow.readthedocs.io/  
**Repozytorium:** https://github.com/python-pillow/Pillow

### 2. OpenCV

**Nazwa:** OpenCV (Open Source Computer Vision Library)  
**Przeznaczenie:** Zaawansowane przetwarzanie obrazów, wizja komputerowa, uczenie maszynowe.

**Główne funkcje:**
- Detekcja obiektów i twarzy
- Wykrywanie krawędzi i konturów
- Transformacje geometryczne
- Filtrowanie i morfologia
- Analiza ruchu i śledzenie
- Funkcje uczenia maszynowego

**Zalety:**
- Bardzo szerokie możliwości
- Wysoka wydajność
- Obsługa video i obrazów w czasie rzeczywistym
- Duża społeczność użytkowników
- Profesjonalne zastosowania

**Ograniczenia:**
- Większa złożożność niż Pillow
- Większy rozmiar instalacji
- Wymaga więcej zasobów systemowych
- Krzywa uczenia się jest stromiejsza

**Dokumentacja:** https://docs.opencv.org/  
**Repozytorium:** https://github.com/opencv/opencv

## Porównanie

| Aspekt | Pillow | OpenCV |
|--------|--------|---------|
| Łatwość użycia | Bardzo łatwe | Średnie |
| Funkcjonalność | Podstawowa | Zaawansowana |
| Wydajność | Dobra | Bardzo dobra |
| Rozmiar | Mały | Duży |
| Zastosowanie | Proste edycje | Wizja komputerowa |

## Instalacja i uruchamianie

### Instalacja bibliotek
```bash
pip install -r requirements.txt
```

### Uruchamianie przykładów

**Sposób 1 - Wszystkie przykłady jedną komendą (zalecane):**
```bash
python zadanie_5.py
```

**Sposób 2 - Osobne skrypty:**
```bash
python examples/pillow_example.py
python examples/opencv_example.py
```

Główny skrypt `zadanie_5.py` automatycznie wykrywa dostępność OpenCV i uruchamia odpowiednie przykłady.

## Wnioski

Obie biblioteki mają swoje miejsce w przetwarzaniu obrazów. Pillow doskonale nadaje się do prostych operacji, podczas gdy OpenCV oferuje profesjonalne narzędzia do zaawansowanej analizy obrazów i wizji komputerowej.