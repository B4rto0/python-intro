# Analiza wielokryterialnego podejmowania decyzji (MCDM)

Projekt implementuje analizę wielokryterialną z użyciem biblioteki pymcdm w ramach laboratorium z Programowania Zaawansowanego.

## Problem badawczy

Wybór najlepszego samochodu spośród 5 opcji na podstawie 5 kryteriów:
- **Cena** (min)
- **Spalanie** (min) 
- **Bezpieczeństwo** (max)
- **Komfort** (max)
- **Niezawodność** (max)

## Implementowane metody

- **TOPSIS** - Technique for Order of Preference by Similarity to Ideal Solution
- **SPOTIS** - Stable Preference Ordering Towards Ideal Solution  
- **VIKOR** - VIšekriterijumsko KOmpromisno Rangiranje

## Funkcjonalności

✅ Analiza trzech metod MCDM  
✅ Porównanie wag eksperckich z entropijnymi  
✅ Testowanie różnych metod normalizacji  
✅ Wizualizacja wyników (6 wykresów)  
✅ Automatyczne generowanie raportów  
✅ Analiza zgodności między metodami  

## Instalacja

```bash
# Klonowanie repozytorium
git clone https://github.com/[twoja-nazwa]/mcdm-analysis.git
cd mcdm-analysis

# Instalacja zależności
pip install -r requirements.txt
```

## Uruchomienie

```bash
# Główna analiza
python mcdm.py

# Przeglądanie raportów
python view_report.py
```

## Wyniki

Program generuje:
- **Wykresy analizy** w formacie PNG
- **Szczegółowe raporty** w formacie Markdown
- **Porównania metod** z analizą zgodności

Wszystkie pliki są zapisywane w folderze `wykresy_raporty/` z timestampem.

## Struktura projektu

```
├── mcdm.py              # Główny kod analizy
├── view_report.py       # Przeglądarka raportów
├── requirements.txt     # Zależności
├── README.md           # Dokumentacja
└── wykresy_raporty/    # Wygenerowane wyniki
```

## Wymagania

- Python 3.7+
- pymcdm ≥ 1.1.3
- numpy ≥ 1.21.0
- pandas ≥ 1.3.0
- matplotlib ≥ 3.4.0
- scipy ≥ 1.0.0

## Przykładowe wyniki

### Ranking alternatyw:
- **TOPSIS**: Audi A4
- **SPOTIS**: Audi A4
- **VIKOR**: Toyota Corolla

### Zgodność metod: 
Audi A4 (2/3 metod)

## Autor

[Twoje Imię]  
Programowanie Zaawansowane - Lab 4  
[Data]

## Licencja

MIT License