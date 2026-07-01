import os
import sqlite3
from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = 'al-theeb-secure-2026'

# التأكد من المسار الصحيح
DB_PATH = 'database.db'

def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

# تهيئة القاعدة
conn = get_db()
conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, balance REAL)')
conn.execute('INSERT OR IGNORE INTO users VALUES (?, ?)', ('admin', 1000.0))
conn.commit()
conn.close()

@app.route('/')
def index():
    return '<form method="post" action="/login"><input name="username"><input name="password" type="password"><button>دخول</button></form>'

@app.route('/login', methods=['POST'])
def login():
    if request.form.get('username') == 'admin' and request.form.get('password') == '159159':
        session['user'] = 'admin'
        return redirect('/dashboard')
    return "خطأ"

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect('/')
    conn = get_db()
    balance = conn.execute('SELECT balance FROM users WHERE username = ?', ('admin',)).fetchone()[0]
    return f'<h1>الرصيد: {balance}</h1><a href="/act">خصم 10</a>'

@app.route('/act')
def act():
    conn = get_db()
    conn.execute('UPDATE users SET balance = balance - 10 WHERE username = ?', ('admin',))
    conn.commit()
    return redirect('/dashboard')
