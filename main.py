import os
import sqlite3
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'al-theeb-secret-key-2026'

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, balance REAL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, action TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
    cursor.execute('INSERT OR IGNORE INTO users VALUES (?, ?)', ('admin', 1000.0))
    conn.commit()
    conn.close()

init_db()

dashboard_html = '''
<div style="text-align:center; padding:50px; background:#0f3460; color:white; font-family: sans-serif;">
    <h1>لوحة تحكم الذئب الملكي</h1>
    <h3>💰 الرصيد المتبقي: ${{ balance }}</h3>
    <a href="/log-action/إنشاء مشهد" style="background:#e94560; padding:15px; margin:10px; color:white; text-decoration:none; border-radius:10px;">إنشاء مشهد</a>
    <a href="/log-action/توليد موجه" style="background:#e94560; padding:15px; margin:10px; color:white; text-decoration:none; border-radius:10px;">توليد موجه</a>
    <br><br><a href="/logout" style="color:white;">تسجيل خروج</a>
</div>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == '159159':
            session['user'] = 'admin'
            return redirect(url_for('dashboard'))
        return "خطأ في الدخول"
    return "<h1>دخول المسؤول</h1><form method='post'><input name='username' placeholder='Username'><input name='password' type='password' placeholder='Password'><button>دخول</button></form>"

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('login'))
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE username = ?', ('admin',))
    balance = cursor.fetchone()[0]
    conn.close()
    return render_template_string(dashboard_html, balance=balance)

@app.route('/log-action/<action>')
def log_action(action):
    if 'user' not in session: return redirect(url_for('login'))
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO logs (action) VALUES (?)', (action,))
    cursor.execute('UPDATE users SET balance = balance - 10 WHERE username = ?', ('admin',))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# تم إيقاف التشغيل المحلي لمنع تضارب المنافذ في كولاب
