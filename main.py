import os
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# تصميم الواجهة مع رسائل خطأ
login_html = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #1a1a2e, #16213e); height: 100vh; display: flex; align-items: center; justify-content: center; margin: 0; color: white; }
        .login-card { background: rgba(255, 255, 255, 0.1); padding: 40px; border-radius: 20px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37); backdrop-filter: blur(8px); width: 300px; text-align: center; }
        input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 10px; border: none; background: rgba(255, 255, 255, 0.2); color: white; box-sizing: border-box; }
        button { width: 100%; padding: 12px; margin-top: 20px; border-radius: 10px; border: none; background: #e94560; color: white; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-card">
        <h1>الذئب الملكي</h1>
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="اسم المستخدم" required>
            <input type="password" name="password" placeholder="كلمة المرور" required>
            <button type="submit">دخول</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(login_html)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'admin' and password == '159159':
        return "<h1>مرحباً بك أيها الملك في لوحة تحكم الذئب الأبيض</h1>"
    else:
        return "<h1>بيانات الدخول خاطئة! <a href='/'>حاول مجدداً</a></h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
