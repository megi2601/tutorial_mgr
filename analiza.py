"""Wczytuje przykładowe dane CSV i zapisuje wykres używany w LaTeX-u."""

import csv
from pathlib import Path

import matplotlib.pyplot as plt


KATALOG_PROJEKTU = Path(__file__).resolve().parent
PLIK_DANYCH = KATALOG_PROJEKTU / "dane" / "wyniki.csv"
PLIK_WYKRESU = KATALOG_PROJEKTU / "obrazy" / "wykres.png"


def wczytaj_dane(sciezka: Path) -> tuple[list[str], list[int]]:
    """Zwraca nazwy miesięcy i odpowiadające im wartości z pliku CSV."""
    with sciezka.open(encoding="utf-8", newline="") as plik:
        rekordy = list(csv.DictReader(plik))

    miesiace = [rekord["miesiac"] for rekord in rekordy]
    wartosci = [int(rekord["liczba_uzytkownikow"]) for rekord in rekordy]
    return miesiace, wartosci


def zapisz_wykres(miesiace: list[str], wartosci: list[int], sciezka: Path) -> None:
    """Tworzy wykres liniowy i zapisuje go jako plik PNG."""
    sciezka.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 4.5))
    plt.plot(miesiace, wartosci, marker="o", linewidth=2, color="#1769aa")
    plt.title("Przykładowy wzrost liczby użytkowników")
    plt.xlabel("Miesiąc")
    plt.ylabel("Liczba użytkowników")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(sciezka, dpi=180)
    plt.close()


def main() -> None:
    miesiace, wartosci = wczytaj_dane(PLIK_DANYCH)
    zapisz_wykres(miesiace, wartosci, PLIK_WYKRESU)
    print(f"Zapisano wykres: {PLIK_WYKRESU}")


if __name__ == "__main__":
    main()
