from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"  # مفتاح الجلسة

# قاعدة بيانات SQLite
def init_db():
    conn = sqlite3.connect("store.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL)""")
    conn.commit()
    conn.close()

init_db()

# الصفحة الرئيسية
@app.route('/')
def home():
    conn = sqlite3.connect("store.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("home.html", products=products)

# تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect("store.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",) (username, password)
