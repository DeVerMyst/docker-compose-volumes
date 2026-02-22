# read_db.py
import psycopg2

# Connexion à la base de données
conn = psycopg2.connect(
    host="localhost",  # Hôte pour le conteneur Docker
    port=5432,         # Port pour le conteneur Docker
    user="myuser",
    password="mypassword",
    database="mydb"
)

# Création d'un curseur
cur = conn.cursor()

# Récupération des données
cur.execute("SELECT name, age FROM users")
rows = cur.fetchall()

# Affichage des données
for row in rows:
    print(f"Nom: {row[0]}, Âge: {row[1]}")

# Fermeture du curseur et de la connexion
cur.close()
conn.close()