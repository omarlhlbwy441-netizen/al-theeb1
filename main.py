import os
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'al-theeb-secret-key-2026'

# الواجهات بتصميم فخم
login_html = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><style>
    body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #1a1a2e, #16213e); height: 100vh; display: flex; align-items: center; justify-content: center; margin: 0; color: white; }
    .login-card { background: rgba(255, 255, 255, 0.1); padding: 40px; border-radius: 20px; backdrop-filter: blur(8px); width: 300px; text-align: center; }
    input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 10px; border: none; background: rgba(255, 255, 255, 0.2); color: white; }
    button { width: 100%; padding: 12px; margin-top: 20px; border-radius: 10px; border: none; background: #e94560; color: white; font-weight: bold; cursor: pointer; }
</style></head>
<body>
    <div class="login-card">
        <h1>دخول الذئب</h1>
        <form action="/" method="post">
            <input type="text" name="username" placeholder="اسم المستخدم" required>
            <input type="password" name="password" placeholder="كلمة المرور" required>
            <button type="submit">دخول</button>
        </form>
    </div>
</body>
</html>
'''

dashboard_html = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><style>
    body { font-family: 'Segoe UI', sans-serif; background: #0f3460; color: white; text-align: center; padding: 50px; }
    .btn { display: inline-block; padding: 15px 30px; margin: 10px; background: #e94560; border-radius: 10px; text-decoration: none; color: white; font-weight: bold; }
</style></head>
<body>
    <h1>لوحة تحكم الذئب الملكي</h1>
    <h3>💰 رصيد المحفظة: $1,000</h3>
    <a href="/create-scene" class="btn">إنشاء مشهد تفاعلي</a>
    <a href="/generate-prompt" class="btn">توليد موجه (Prompt)</a>
    <br><a href="/logout">تسجيل خروج</a>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == '159159':
            session['user'] = 'admin'
            return redirect(url_for('dashboard'))
        return "<h1>بيانات الدخول خاطئة!</h1>"
    return render_template_string(login_html)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template_string(dashboard_html)

@app.route('/create-scene')
def create_scene():
    if 'user' not in session: return redirect(url_for('login'))
    return "<h1>✅ تم إنشاء المشهد بنجاح!</h1><a href='/dashboard'>العودة</a>"

@app.route('/generate-prompt')
def generate_prompt():
    if 'user' not in session: return redirect(url_for('login'))
    return "<h1>✨ تم توليد الموجه بنجاح!</h1><a href='/dashboard'>العودة</a>"

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
