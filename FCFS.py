#ALGORYTM FCFS(First Come, FirstServed)
#Oznacza to, że sortujemy procesy od początku do końca w takiej kolejności jakiej sie pojawiły
def fcfs(arrival_time: list[int], burst_time: list[int]) -> None:
    #Długość listy to liczba naszych zadań.
    n = len(arrival_time)
    #Tworzymy liste, która reprezentuje id każdego procesu zaczynając od 0.
    id = list(range(n))

#Sortujemy wedlug czasu przybycia(arrival_time).
    for i in id:
         for j in range(0, n - 1):
            if arrival_time[id[j]] > arrival_time[id[j + 1]]:
                temp=id[j]
                id[j] = id[j + 1]
                id[j + 1] = temp

    #Tworzymy listy złożone z zer, które będziemy później modyfikować.
    start_time = [0] * n
    finish_time = [0] * n
    waiting_time = [0] * n
    current_time = 0

    #Ustawiamy poszczególne wartości dla danego id(Już w odpowiedniej kolejności).
    for i in id:
        if current_time < arrival_time[i]:      #Jeśli aktualny czas jest mniejszy, niż czas przybycia to znaczy, że procesor jest bezczynny do momentu przybycia zadania
            current_time = arrival_time[i]      #W takim wypadku aktualizujemy current_time
        start_time[i] = current_time     #Ustawiamy czas rozpoczęcia
        finish_time[i] = current_time + burst_time[i]   #Ustawiamy czas zakończenia
        waiting_time[i] = start_time[i] - arrival_time[i]   #Ustawiamy czas oczekiwania
        current_time = finish_time[i]    #Aktualizujemy aktualny czas

    #Obliczamy średni czas oczekiwania
    total_waiting_time = sum(waiting_time)
    average_waiting_time = total_waiting_time / n


#Wypisujemy nasze wyniki w przejrzysty sposób
    print("Kolejność | ID Procesu | Czas przybycia | Czas wykonania | Czas rozpoczęcia | Czas zakończenia | Czas oczekiwania")
    x=0
    for i in id:
        x += 1
        print(f"{x:9} | {i:10} | {arrival_time[i]:14} | {burst_time[i]:14} | {start_time[i]:16} | {finish_time[i]:16} | {waiting_time[i]:15}")
    print("\nŚredni czas oczekiwania: ",round(average_waiting_time,2))
    print("Całkowity czas działania algorytmu: ",(finish_time[id[-1]]-start_time[id[0]]))     #Całkowity czas algorytmu to finish_time ostatniego w kolejności procesu odejmując początkowy czas rozpoczęcia po ewentualnej bezczynności..

# Definiujemy tablice arrival_time i burst_time.
arrival_time = [1, 2, 3, 4, 0]
burst_time = [2, 3, 4, 5, 6]

# Przeprowadzamy symulację.
fcfs(arrival_time, burst_time)