# Środowisko do programistycznej pracy magisterskiej — Windows

## 1. Zainstaluj narzędzia

1. Zainstaluj **Git**: <https://git-scm.com/download/win>.
2. Zainstaluj **Python 3**: <https://www.python.org/downloads/windows/>. Podczas instalacji zaznacz `Add python.exe to PATH`.
3. Zainstaluj **Visual Studio Code**: <https://code.visualstudio.com/>.
4. W VS Code otwórz widok **Extensions** (`Ctrl+Shift+X`) i zainstaluj:
   - `Python` (Microsoft),
   - `Pylance` (Microsoft),
   - `Jupyter` (Microsoft),
   - `LaTeX Workshop` (James Yu).
5. Zainstaluj **MiKTeX**: <https://miktex.org/download>. W ustawieniach MiKTeX włącz automatyczną instalację brakujących pakietów.
6. Zainstaluj aplikację **Codex** i otwórz ten folder jako projekt. Dzięki temu Codex może czytać, tworzyć i sprawdzać pliki należące do pracy.
7. Załóż konto w **GitHub**: <https://github.com/>. 

## 2. Sprawdź instalację

Otwórz terminal PowerShell w VS Code z menu **Terminal → New Terminal** i wykonaj:

```powershell
python --version
git --version
pdflatex --version
```

Każde polecenie powinno wyświetlić numer wersji. Jeśli `python` nie działa, spróbuj `py --version`.

## 3. Uruchom analizę w Pythonie

W terminalu, w głównym folderze projektu, wykonaj:

```powershell
python -m pip install -r requirements.txt
python analiza.py
```

(zamiast python analiza.py można kliknąć przycisk w VS code - prawy górny róg ekranu)

Sprawdź, czy powstał plik `obrazy/wykres.png`. W VS Code wybierz interpreter: `Ctrl+Shift+P` → **Python: Select Interpreter**.

## 4. Skompiluj dokumenty LaTeX

Najpierw uruchom `python analiza.py`, ponieważ oba dokumenty korzystają z wygenerowanego wykresu. Następnie:

1. Otwórz `praca.tex` w VS Code.
2. Naciśnij `Ctrl+Alt+B` (polecenie LaTeX Workshop: **Build LaTeX project**).
3. Powtórz dla `prezentacja.tex`.
4. Otwórz podgląd PDF skrótem `Ctrl+Alt+V`.

Alternatywnie użyj terminala:

```powershell
pdflatex praca.tex
pdflatex prezentacja.tex
```

## 5. Włącz Git i opublikuj projekt

1. Ustaw swoją tożsamość (jednorazowo, po pobraniu gita):

   ```powershell
   git config --global user.name "Imię Nazwisko"
   git config --global user.email "adres@example.com"
   ```

2. Utwórz lokalne repozytorium i pierwszy zapis zmian:

W VS Code do pracy z git służy ikona z trzema kropkami (poniżej lupki) na panelu po lewej. Tam można się przeklikać przez:

- utworzenie repozytorium (initialize repo)
- zapisywanie kolejnych etapów pracy (stage changes, commit)
- wysyłanie tych zmian do repo na githubie (push)

Wszystkie te czynności można też robić przez teminal zamiast przez guziki w VS Code:

   ```powershell
   git init
   git add .
   git commit -m "Dodaj początkową strukturę pracy"
   ```

UWAGA: żeby połączyć się z repo internetowym trzeba będzie się logować przez przeglądarkę na swoje konto GitHub (VS Code wysyła odpowiednie komunikaty i linki).

3. Po każdym zamkniętym etapie pracy wykonuj:

   ```powershell
   git status
   git add .
   git commit -m "Krótki opis wykonanej zmiany"
   git push
   ```
Dzięki temu jesteśmy zabezpieczeni na wypadek np. całkowitej awarii komputera ;)

## 6. Dodatek: Ustawienia projektu w folderze `.vscode`

Plik `.vscode/settings.json` przechowuje ustawienia VS Code tylko dla tego projektu. Możesz dzięki temu dostosować pracę z Pythonem i LaTeX-em bez zmieniania konfiguracji innych projektów. Jeżeli dodasz folder `.vscode` do Git, te ustawienia będą dostępne również po sklonowaniu repozytorium na innym komputerze.

1. Utwórz folder `.vscode` w głównym folderze projektu.
2. Utwórz w nim plik `settings.json`.
3. Zacznij od minimalnej konfiguracji:

   ```json
   {
     "latex-workshop.latex.autoBuild.run": "onSave",
     "latex-workshop.latex.outDir": "%DIR%/build",
     "latex-workshop.view.pdf.viewer": "tab"
   }
   ```

Ten przykład automatycznie kompiluje LaTeX po zapisaniu pliku, umieszcza pliki wynikowe w folderze `build` i otwiera PDF w karcie VS Code. Później możesz tu dodać np. własne narzędzia kompilacji, receptury `latexmk`, automatyczne formatowanie albo sprawdzanie pisowni.

Ustawienia prywatne lub zależne od konkretnego komputera lepiej zachować globalnie w VS Code albo dodać `.vscode/` do `.gitignore`. Do repozytorium zapisuj tylko konfigurację przydatną wszystkim osobom pracującym nad projektem.

## 7. Codzienny schemat pracy

1. Otwórz folder projektu w Codex i VS Code.
2. Zmień kod, dane albo tekst.
3. Uruchom skrypt i sprawdź wykres.
4. Skompiluj dokumenty i obejrzyj PDF-y.
5. Wykonaj commit i `git push`.
