
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

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == '159159':
            session['user'] = 'admin'
            return redirect(url_for('dashboard'))
        return "<h1>بيانات الدخول خاطئة</h1><a href='/'>رجوع</a>"
    return "<h1>دخول المسؤول</h1><form method='post'><input name='username' placeholder='Username'><input name='password' type='password' placeholder='Password'><button>دخول</button></form>"

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('login'))
    conn = get_db()
    balance = conn.execute('SELECT balance FROM users WHERE username = ?', ('admin',)).fetchone()['balance']
    conn.close()
    return render_template_string('''
    <div style="text-align:center; padding:50px; background:#0f3460; color:white; font-family: sans-serif;">
        <h1>لوحة تحكم الذئب الملكي</h1>
        <h3>💰 الرصيد المتبقي: ${{ balance }}</h3>
        <a href="/log-action/إنشاء مشهد" style="background:#e94560; padding:15px; margin:10px; color:white; text-decoration:none; border-radius:10px;">إنشاء مشهد</a>
        <a href="/log-action/توليد موجه" style="background:#e94560; padding:15px; margin:10px; color:white; text-decoration:none; border-radius:10px;">توليد موجه</a>
        <br><br><a href="/view-logs" style="color:#00d2ff;">عرض سجل العمليات</a> | <a href="/logout" style="color:white;">خروج</a>
    </div>
    ''', balance=balance)

@app.route('/view-logs')
def view_logs():
    if 'user' not in session: return redirect(url_for('login'))
    conn = get_db()
    logs = conn.execute('SELECT * FROM logs ORDER BY timestamp DESC').fetchall()
    conn.close()
    items = "".join([f"<li>{l['timestamp']} - {l['action']}</li>" for l in logs])
    return render_template_string(f"<h1>سجل العمليات</h1><ul>{items}</ul><br><a href='/dashboard'>العودة للوحة</a>")

@app.route('/log-action/<action>')
def log_action(action):
    if 'user' not in session: return redirect(url_for('login'))
    conn = get_db()
    conn.execute('INSERT INTO logs (action) VALUES (?)', (action,))
    conn.execute('UPDATE users SET balance = balance - 10 WHERE username = ?', ('admin',))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
