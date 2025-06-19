# Funkcja symulująca algorytm LRU
def lru(pages, frames):
    memory = []  # Lista reprezentująca ramki stron w pamięci
    page_faults = 0  # Licznik błędów strony

    for page in pages:
        if page not in memory:
            page_faults += 1  # Jeśli strona nie jest w pamięci, zwiększamy licznik błędów strony
            if len(memory) >= frames:   #Jeśli pomięć jest pełna to :
                memory.pop(0)  # Usuwamy najmniej niedawno używaną stronę (pierwszą na liście)
            memory.append(page)  # Dodajemy nową stronę do pamięci
        else:
            memory.remove(page)  # Usuwamy stronę, aby później dodać ją na koniec
            memory.append(page)  # Przesuwamy stronę na koniec (aktualizujemy jej użycie)
        print("Stan Pamięci: ",memory,"  Zaladowana strona: ",page)  # Wyświetlamy stan pamięci po każdym kroku

    return page_faults

# Strony do załadowania
pages = [4, 5, 3, 1, 4, 5, 2, 4, 5, 3, 1, 2]
frames = 3  # Liczba ramek stron w pamięci

# Symulacja
page_faults = lru(pages, frames)
print("Błędy braku strony: ",page_faults)