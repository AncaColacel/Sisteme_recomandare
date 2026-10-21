# Laborator 2: Sistem de recomandare cu Recombee — Înregistrare proprietăți

## Descrierea dataset-ului

**Domeniu:** Cărți (Books)

**Sursă:** [Books Dataset — Kaggle (Abdallah Wagih Ibrahim)](https://www.kaggle.com/code/abdallahwagih/books-recommendation-system/input)

**Volum:** 6810 de cărți

**Descriere generală:**
Dataset-ul conține metadate despre cărți, creat pentru dezvoltarea de sisteme de recomandare, chatboți și aplicații NLP. Fiecare intrare reprezintă o carte unică identificată prin codul ISBN-13 și include informații precum titlul, autorul/autorii, categoria, anul publicării, numărul de pagini, rating-ul mediu și numărul de recenzii. De asemenea, sunt disponibile descrierile cărților și link-uri către thumbnail-urile copertelor de pe Google Books.

## Proprietățile definite în Recombee

Coloana `isbn13` este utilizată ca **itemId** în Recombee (identificator unic nativ, nu se înregistrează ca proprietate separată).

| Nr. | Proprietate | Tip Recombee | Descriere |
|-----|-------------|--------------|-----------|
| 1 | `isbn10` | `string` | Codul ISBN-10 al cărții |
| 2 | `title` | `string` | Titlul cărții |
| 3 | `subtitle` | `string` | Subtitlul cărții (poate fi gol) |
| 4 | `authors` | `string` | Autorul/autorii, separați prin `;` |
| 5 | `categories` | `string` | Categoria/genul literar |
| 6 | `thumbnail` | `string` | URL către imaginea copertei (Google Books) |
| 7 | `description` | `string` | Descrierea/rezumatul cărții |
| 8 | `published_year` | `int` | Anul publicării |
| 9 | `average_rating` | `double` | Rating-ul mediu (ex: 4.15) |
| 10 | `num_pages` | `int` | Numărul de pagini |
| 11 | `ratings_count` | `int` | Numărul total de recenzii/rating-uri |

## Structura proiectului

```
lab02/
├── books.csv                 # Dataset-ul CSV cu 6810 cărți
├── recombee_properties.py    # Script Python pentru înregistrarea proprietăților în Recombee
├── README.md                 # Documentația proiectului (acest fișier)
└── ro/
    └── README.md             # Ghidul laboratorului (instrucțiuni)
```

## Rulare

### 1. Instalare dependențe

```bash
pip install recombee-api-client pandas
```

### 2. Executare script

```bash
cd lab02
python recombee_properties.py
```

Scriptul va:
1. Încărca și valida dataset-ul CSV
2. Trimite cele 11 proprietăți către Recombee prin API
3. Afișa o verificare finală cu proprietățile înregistrate

## Tehnologii utilizate

- **Python 3.12**
- **Recombee API Client** (`recombee-api-client`)
- **Pandas** — citirea și validarea fișierului CSV
