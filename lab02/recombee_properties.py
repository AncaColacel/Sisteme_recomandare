import os
import pandas as pd
from dotenv import load_dotenv
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import AddItemProperty, ListItemProperties
from recombee_api_client.exceptions import APIException

# Incarcarea variabilelor de mediu din fisierul .env
load_dotenv()

# TODO 1: Configurare credentiale Recombee
# Credentialele sunt citite din fisierul .env (vezi .env.example pentru format)
DB_NAME = os.getenv('RECOMBEE_DB_NAME', 'upb-univ-dev')
PRIVATE_TOKEN = os.getenv('RECOMBEE_PRIVATE_TOKEN', '')
REGION = Region.EU_WEST  # Regiuni disponibile: Region.EU_WEST, Region.US_WEST, Region.CA_EAST, Region.AP_SE

# Initializarea clientului Recombee
client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=REGION)

# TODO 2: Configurare dataset propriu
# Dataset-ul ales: Books dataset de pe Kaggle (6810 carti)
# isbn13 va fi folosit ca itemId in Recombee (nu se inregistreaza ca proprietate)
PATH_DATASET = 'books.csv'

# TODO 3: Definirea schemei de date (11 proprietati mapate din dataset-ul de carti)
# Coloane din dataset: isbn13, isbn10, title, subtitle, authors, categories,
#                      thumbnail, description, published_year, average_rating,
#                      num_pages, ratings_count
# isbn13 = itemId (gestionat nativ de Recombee, NU se adauga ca proprietate)
PROPRIETATI_CATALOG = [
    {"name": "isbn10",          "type": "string"},
    {"name": "title",           "type": "string"},
    {"name": "subtitle",        "type": "string"},
    {"name": "authors",         "type": "string"},
    {"name": "categories",      "type": "string"},
    {"name": "thumbnail",       "type": "string"},
    {"name": "description",     "type": "string"},
    {"name": "published_year",  "type": "int"},
    {"name": "average_rating",  "type": "double"},
    {"name": "num_pages",       "type": "int"},
    {"name": "ratings_count",   "type": "int"},
]

def load_dataset():
    """Functie helper care citeste si verifica dataset-ul"""
    try:
        df = pd.read_csv(PATH_DATASET)
        total_randuri = len(df)
        print(f"Dataset incarcat cu succes! Total randuri: {total_randuri}")

        # Verificare numar de randuri (100 - 10K)
        if total_randuri < 100:
            print("ATENTIE: Dataset-ul are sub 100 de produse!")
        elif total_randuri > 10 * 1000:
            print("ATENTIE: Dataset-ul este prea mare! Limitati-l la primele 10K randuri.")

        print("\nPreview primele 3 randuri:")
        print(df.head(3))
        print("-" * 50)
        return df
    except FileNotFoundError:
        print(f"Eroare: Fisierul '{PATH_DATASET}' nu a fost gasit!")
        return None

def set_properties():
    """Functie care trimite structura coloanelor catre Recombee"""
    print(f"\nIncepe definirea proprietatilor pentru baza de date: '{DB_NAME}'...")

    for prop in PROPRIETATI_CATALOG:
        # Validare nume proprietati valide
        if "nume_proprietate" in prop["name"]:
            print("Eroare: Trebuie sa schimbati 'nume_proprietate_x' cu denumirile reale din coloanele fisierul vostru!")
            continue

        try:
            # Request API Recombee pentru adaugarea proprietatii (echivalentul adaugarii unei coloane intr-un tabel)
            client.send(AddItemProperty(prop["name"], prop["type"]))
            print(f"Proprietatea '{prop['name']}' ({prop['type']}) a fost adaugata cu succes.")
        except APIException as e:
            # Recombee returnează eroare daca proprietatea a fost deja definita la o rulare anterioara
            if "already exists" in str(e).lower():
                print(f"Proprietatea '{prop['name']}' exista deja in Recombee.")
            else:
                print(f"Eroare API la proprietatea '{prop['name']}': {e}")

def verify():
    """Interogheaza API-ul pentru a lista toate proprietatile active din cont"""
    print("Se verifica structura finala din Recombee Admin UI...")
    try:
        atribute_active = client.send(ListItemProperties())
        print("Proprietatile configurate in acest moment in baza ta de date:")
        for atribute in atribute_active:
            print(f"- {atribute['name']} => tip de date: {atribute['type']}")
    except APIException as e:
        print(f"Nu s-a putut efectua verificarea. Detalii eroare: {e}")

if __name__ == "__main__":
    # Verificam daca fisierul CSV local se citeste corect
    dataset_ok = load_dataset()

    if dataset_ok is not None:
        # Trimitem proprietatile catre Recombee prin API
        set_properties()

        # Listam ce s-a salvat in baza de date pentru confirmare
        verify()
