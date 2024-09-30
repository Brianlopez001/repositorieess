from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

app.secret_key = 'Onefregon001'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    try:
        with sqlite3.connect('usuarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (username) VALUES (?)", (username,))
            conn.commit()
        return "Usuario registrado exitosamente!"
    except sqlite3.IntegrityError:
        return "Error: El nombre de usuario ya existe. Por favor, elige otro."
    except Exception as e:
        return f"Ocurrió un error al registrar el usuario: {e}"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    try:
        with sqlite3.connect('usuarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
            user = cursor.fetchone()
        
        if user:
            return f"Bienvenido de nuevo, {username}!"
        else:
            return "Usuario no encontrado. Por favor, verifica el nombre de usuario o regístrate."
    except Exception as e:
        return f"Ocurrió un error al iniciar sesión: {e}"


# Manejo de errores
@app.errorhandler(500)
def internal_error(error):
    return "Ocurrió un error interno, por favor intenta de nuevo más tarde.", 500

if __name__ == '__main__':
    app.run(debug=False)  # Cambia a False
    
    
