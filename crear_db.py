import sqlite3

# Crea la base de datos y la tabla si no existen
with sqlite3.connect('usuarios.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL
                    )''')
    conn.commit()

print("Base de datos y tabla 'usuarios' creadas correctamente.")
