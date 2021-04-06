import numpy as np
from utils import file_len
from gauss_jordan_method import jordan

if __name__ == "__main__":
    i = 1

    print("\n\n\n-------------------------------------------\n")
    print("\nAutorzy: Oskar Kurczewski i Jakub Czarnecki\n")
    print("Metody numeryczne - zadanie 2\n")
    print("Wariant: metoda eliminacji Jordana\n\n")
    print("-------------------------------------------\n")
    print("\n\n")

    # Aby dodać własny układ równań, należy połączyć macierz współczynników z macierzą znajdującą się po znaku równości, dodając ją jako ostatnią kolumnę. Separator dziesiętny to kropka.
    # Kolejne linijki to kolejne wiersze, a kolumny powinny być oddzielone spacją. Nazwa pliku wg wzoru: "data" + wielka litera inna niż A-J + ".txt".

    while i != 0:
        print("Wybierz podpunkt (a-j) z zadania: ")
        choice = "data" + input().capitalize() + ".txt"

        file = open(choice, "r")
        number_of_rows = file_len(choice)
        spl = file.read().splitlines()

        matrix = []
        for i in range(number_of_rows):
            helper = spl[i].split()
            matrix.append(helper)
        mat = np.asarray(matrix, dtype = np.double)

        print("\n\nWybrana macierz:\n\n" + str(mat))
        print("\nRozwiązanie:")
        print(jordan(mat))

        print("\nKontynuować? 0 - nie, inne - tak")
        i = input()