# Laborator 3: Sistem de recomandare cu Recombee — Trimitere Items

Acest modul implementează popularea efectivă a catalogului de produse în platforma **Recombee** pe baza schemei de date definite în Laboratorul 2.

---

## Descriere Dataset & Mapare

- **Domeniu:** Cărți (*Books*)
- **Sursă:** [Books Dataset — Kaggle](https://www.kaggle.com/code/abdallahwagih/books-recommendation-system/input)
- **Volum încărcat:** 6.810 cărți
- **Identificator Unic (`itemId`):** Coloana `isbn13` din fișierul CSV, convertită în format string.
- **Proprietăți sincronizate:**
  - `isbn10` (`string`)
  - `title` (`string`)
  - `subtitle` (`string`)
  - `authors` (`string`)
  - `categories` (`string`)
  - `thumbnail` (`string`)
  - `description` (`string`)
  - `published_year` (`int`)
  - `average_rating` (`double`)
  - `num_pages` (`int`)
  - `ratings_count` (`int`)

---

## Optimizări & Tehnici de implementare

1. **Optimizare prin Cereri Batch:**
   - Pentru evitarea a 6.810 apeluri HTTP individuale, datele sunt grupate în loturi de câte **100 de cereri** (`Batch`).
   - Întreg setul de date de 6.810 item-uri a fost transferat în doar **69 de request-uri HTTP**.

2. **Creare automată (`cascade_create=True`):**
   - Utilizarea `SetItemValues(item_id, properties, cascade_create=True)` permite crearea automată a item-ului în Recombee dacă acesta nu există, setându-i simultan toate valorile atributelor într-o singură instrucțiune.

3. **Tratarea valorilor lipsă (`NaN` / `None`):**
   - Câmpurile opționale sau lipsă (precum `subtitle`, cărți fără an de publicare sau fără categorii) sunt filtrate înainte de serializare pentru a preveni erori de parsare sau incompatibilități de tip în API.

4. **Securitatea credențialelor:**
   - Variabilele de conectare (`RECOMBEE_DB_NAME`, `RECOMBEE_PRIVATE_TOKEN`) sunt încărcate în mod securizat din fișierul `.env`.

---

## 📂 Structura Modulului

```
lab03/
├── books.csv                 # Dataset-ul CSV cu 6.810 cărți
├── recombee_items.py         # Scriptul Python de trimitere în loturi
├── .env.example              # Model pentru variabilele de mediu
├── .env                      # Credențialele reale (ignorat în git)
└── README.md                 # Documentația laboratorului 
```

**Autor:** Anca-Maria Colăcel  
**Master:** Facultatea de Automatică și Calculatoare, UNSTPB  
