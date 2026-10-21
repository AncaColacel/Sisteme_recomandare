# Sisteme de Recomandare — Proiecte și Laboratoare

Acest repository conține rezolvările și temele practice realizate în cadrul cursului **Sisteme de Recomandare** (Master, Facultatea de Automatică și Calculatoare, Universitatea Națională de Știință și Tehnologie POLITEHNICA București).

---

## 📂 Cuprins Laboratoare

### 🔹 [Laboratorul 01: Colectarea Datelor Implicite](lab01/)
- **Descriere:** Colectarea evenimentelor și contextului utilizatorului (HTTP Headers, User-Agent, rezoluție ecran, geolocație/ip etc.) prin intermediul unei aplicații Flask.
- **Fișiere:** Script de tracking (`track.py`), pagină web de colectare (`index.html`) și log-ul de evenimente generat (`track_Colacel_Anca-Maria.json`).

### 🔹 [Laboratorul 02: Recombee — Definire Proprietăți Catalog](lab02/)
- **Descriere:** Integrarea platformei Recombee și crearea schemei de date pentru un catalog de cărți.
- **Dataset:** `books.csv` (6.810 cărți cu atribute precum autor, rating, descriere, categorii, pagini).
- **Fișiere:** Script API (`recombee_properties.py`), configurare variabile de mediu (`.env` / `.env.example`) și documentația aferentă (`README.md`).

---

## 🛠️ Instalare și Rulare

1. **Creare mediu virtual Python:**
   ```bash
   python -m venv .venv
   ```

2. **Activare mediu virtual:**
   - **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS:**
     ```bash
     source .venv/bin/activate
     ```

3. **Instalarea pachetelor necesare:**
   ```bash
   pip install -r requirements.txt
   ```

---

**Autor:** Anca-Maria Colăcel
