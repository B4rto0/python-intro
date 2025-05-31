# Biblioteki do przetwarzania obrazów - Lab 5

Projekt zawiera przykłady użycia dwóch bibliotek Python do przetwarzania obrazów:
- **Pillow** - podstawowe operacje na obrazach
- **OpenCV** - zaawansowane przetwarzanie obrazów

## Struktura projektu

```
/
├── examples/
│   ├── pillow_example.py    # Osobny skrypt Pillow
│   └── opencv_example.py    # Osobny skrypt OpenCV
├── main.py                  # Główny skrypt - uruchamia obie biblioteki
├── requirements.txt
├── raport.md
├── INSTALACJA.md
└── README.md
```

## Instalacja

```bash
pip install -r requirements.txt
```

## Uruchamianie

### Sposób 1 - Wszystkie przykłady jedną komendą (zalecane)
```bash
python main.py
```

### Sposób 2 - Osobne skrypty
```bash
python examples/pillow_example.py
python examples/opencv_example.py
```

## Opis bibliotek

### Pillow
Biblioteka do podstawowych operacji na obrazach:
- Zmiana rozmiaru obrazów
- Stosowanie filtrów (rozmycie, wyostrzenie)
- Regulacja jasności i kontrastu

### OpenCV  
Zaawansowana biblioteka do wizji komputerowej:
- Detekcja krawędzi algorytmem Canny
- Transformacje geometryczne (rotacja)
- Przetwarzanie obrazów w czasie rzeczywistym

## Wyniki

Po uruchomieniu powstają foldery z wynikami:
- `pillow_results/` - obrazy wygenerowane przez Pillow
- `opencv_results/` - obrazy wygenerowane przez OpenCV

Szczegółowy opis znajduaje w pliku `raport.md`.