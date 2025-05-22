#3. Consumo de API con interfaz y autenticación (Nivel Intermedio/Avanzado) 
#Enunciado: Crea una aplicación en Python que: 
#• Use algun módulo gráfico para mostrar una ventana de login. 
#• Utilice una base de datos SQLite para validar si el usuario está registrado. 
#• Si el usuario no existe, puede mostrar un mensaje de error (no se requiere registrar 
#usuarios). 
#• Al hacer login correctamente, se muestre información proveniente de una API 
#pública, por ejemplo: (Api del clima, Api de Rick and Morty o a su eleccion) 
#Requisitos técnicos: 
#• Base de datos SQLite con una tabla usuarios (username TEXT, password TEXT). 
#• Validación del usuario con consulta SQL. 
#• Si el login es exitoso, se muestra la lista de usuarios obtenidos desde la API. 
#• Interfaz simple con campo usuario, contraseña, botón login.

import tkinter as tk
from tkinter import messagebox
import sqlite3
import requests
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        
        # Variables para los campos de entrada
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        
        # Crear widgets
        self.create_widgets()
        
        # Inicializar base de datos
        self.init_database()
        
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Etiquetas y campos de entrada
        tk.Label(main_frame, text="Usuario:").grid(row=0, column=0, sticky=tk.W, pady=10)
        tk.Label(main_frame, text="Contraseña:").grid(row=1, column=0, sticky=tk.W, pady=10)
        
        tk.Entry(main_frame, textvariable=self.username_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(main_frame, textvariable=self.password_var, show="*").grid(row=1, column=1, padx=10, pady=10)
        
        # Botón de login
        login_button = tk.Button(main_frame, text="Iniciar Sesión", command=self.validate_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)
        
    def init_database(self):
        # Verificar si existe la base de datos, si no, crearla con usuarios de prueba
        if not os.path.exists("users.db"):
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            
            # Crear tabla de usuarios
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
            ''')
            
            # Insertar usuarios de prueba
            usuarios_prueba = [
                ("admin", "admin"),
                ("usuario", "password"),
                ("test", "test123")
            ]
            
            cursor.executemany("INSERT OR IGNORE INTO usuarios VALUES (?, ?)", usuarios_prueba)
            conn.commit()
            conn.close()
            
    def validate_login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor, complete todos los campos")
            return
        
        # Validar en la base de datos
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        conn.close()
        
        if user:
            self.root.withdraw()  # Ocultar ventana de login
            self.open_api_window()  # Abrir ventana de API
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    def open_api_window(self):
        # Crear nueva ventana para mostrar datos de API
        api_window = tk.Toplevel(self.root)
        api_window.title("Datos de Rick and Morty API")
        api_window.geometry("600x400")
        
        # Cuando se cierre esta ventana, mostrar nuevamente la de login
        api_window.protocol("WM_DELETE_WINDOW", lambda: self.on_api_window_close(api_window))
        
        # Frame con scroll para mostrar resultados
        main_frame = tk.Frame(api_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear canvas con scrollbar
        canvas = tk.Canvas(main_frame)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Obtener datos de la API
        try:
            response = requests.get("https://rickandmortyapi.com/api/character")
            if response.status_code == 200:
                data = response.json()
                characters = data.get("results", [])
                
                # Título
                tk.Label(scrollable_frame, text="Personajes de Rick and Morty", font=("Arial", 14, "bold")).pack(pady=10)
                
                # Mostrar personajes
                for i, character in enumerate(characters):
                    frame = tk.Frame(scrollable_frame, relief=tk.RIDGE, bd=2)
                    frame.pack(fill=tk.X, padx=5, pady=5)
                    
                    tk.Label(frame, text=f"Nombre: {character['name']}", anchor="w").pack(fill=tk.X)
                    tk.Label(frame, text=f"Estado: {character['status']}", anchor="w").pack(fill=tk.X)
                    tk.Label(frame, text=f"Especie: {character['species']}", anchor="w").pack(fill=tk.X)
                    tk.Label(frame, text=f"Origen: {character['origin']['name']}", anchor="w").pack(fill=tk.X)
                    
            else:
                tk.Label(scrollable_frame, text=f"Error al obtener datos: {response.status_code}").pack()
        except Exception as e:
            tk.Label(scrollable_frame, text=f"Error: {str(e)}").pack()
    
    def on_api_window_close(self, window):
        window.destroy()
        self.root.deiconify()  # Mostrar ventana de login nuevamente


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

