""" 1.	Opis funkcji wbudowanej: zip()
	•	Funkcja zip() łączy elementy z dwóch lub więcej iterowalnych obiektów (np. list, krotek) w pary. Zwraca iterator, który tworzy krotki zawierające elementy z tych iterowalnych obiektów na odpowiadających sobie pozycjach.
	•	Przykład: zip([1, 2, 3], ['a', 'b', 'c']) zwróci iterator tworzący pary: (1, 'a'), (2, 'b'), (3, 'c').
	•	Dokumentacja: https://docs.python.org/3/library/functions.html#zip
	2.	Opis modułu: random
	•	Moduł random zapewnia funkcje do generowania liczb pseudolosowych oraz operacji na tych liczbach, takich jak losowanie elementów z listy, mieszanie listy, generowanie losowych liczb całkowitych lub zmiennoprzecinkowych w określonych zakresach.
	•	Przykład: random.randint(1, 10) zwróci losową liczbę całkowitą z przedziału 1–10.
	•	Dokumentacja: https://docs.python.org/3/library/random.html
	3.	Opis wyjątku: ValueError
	•	Wyjątek ValueError jest podnoszony, gdy funkcja otrzymuje argument o poprawnym typie, ale nieodpowiedniej wartości. Na przykład, gdy próbuje się przekonwertować tekst, który nie jest liczbą, na typ liczbowy.
	•	Przykład: int('abc') spowoduje rzutowanie błędu ValueError.
	•	Dokumentacja: https://docs.python.org/3/library/exceptions.html#ValueError """

# Importowanie modułu random do generowania losowych liczb
import random

# Tworzenie dwóch list
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# Łączenie list za pomocą funkcji zip()
zipped = list(zip(list1, list2))

# Wypisanie połączonych par
print("Połączone listy:", zipped)

# Użycie funkcji z modułu random
random_choice = random.choice(list1)  # Wybiera losowy element z listy

print("Losowy wybór z listy list1:", random_choice)

# Obsługa wyjątku try-except
try:
    num = int("abc")  
except ValueError as e:
    print("Błąd konwersji:", e)  
