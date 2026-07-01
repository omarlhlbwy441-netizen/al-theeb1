import os
import sqlite3
from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = 'al-theeb-secret-key-2026'
# المسار المعتمد في السحابة
DB_PATH = '/tmp/database.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, balance REAL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, action TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
    cursor.execute('INSERT OR IGNORE INTO users VALUES (?, ?)', ('admin', 1000.0))
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == '159159':
            session['user'] = 'admin'
            return redirect('/dashboard')
        return "خطأ في الدخول"
    return render_template_string('<body style="display:flex; justify-content:center; align-items:center; height:100vh; background:#0f3460; margin:0;"><form method="post" style="background:#fff; padding:20px; border-radius:10px;"><input name="username" placeholder="User" required><br><br><input name="password" type="password" placeholder="Pass" required><br><br><button>دخول</button></form></body>')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect('/')
    conn = sqlite3.connect(DB_PATH)
    user = conn.execute('SELECT balance FROM users WHERE username = ?', ('admin',)).fetchone()
    conn.close()
    return render_template_string('''
    <div style="text-align:center; padding:20px; background:#0f3460; color:white; height:100vh; font-family:sans-serif;">
        <h1>الذئب الملكي</h1>
        <h2>الرصيد: ${{ balance }}</h2>
        <a href="/action/10" style="display:block; padding:15px; background:#e94560; margin:10px; color:white; text-decoration:none; border-radius:10px; font-weight:bold;">إنشاء مشهد</a>
    </div>
    ''', balance=user[0])

@app.route('/action/<amount>')
def action(amount):
    conn = sqlite3.connect(DB_PATH)
    conn.execute('UPDATE users SET balance = balance - ? WHERE username = ?', (amount, 'admin'))
    conn.commit()
    conn.close()
    return redirect('/dashboard')
