import psycopg2


def add_users():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            user="myuser",
            password="mypassword",
            database="mydb"
        )
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Charlie", 40))
            cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("David", 35))
            conn.commit()
            print("Charlie et David ont été ajoutés.")
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    add_users()