import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

dashboard_html = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0f3460; color: white; margin: 0; padding: 20px; }
        .dashboard { max-width: 800px; margin: auto; background: rgba(255,255,255,0.05); padding: 30px; border-radius: 20px; backdrop-filter: blur(10px); text-align: center; }
        .card { background: #1a1a2e; padding: 20px; border-radius: 15px; margin: 10px 0; border: 1px solid #e94560; }
        .btn { display: inline-block; padding: 10px 20px; margin: 5px; background: #e94560; border-radius: 8px; text-decoration: none; color: white; font-weight: bold; }
    </style>
</head>
<body>
    <div class="dashboard">
        <h1>لوحة تحكم الذئب الملكي</h1>
        <div class="card">
            <h3>💰 رصيد المحفظة: $1,000</h3>
        </div>
        <div class="card">
            <h3>العمليات المتاحة:</h3>
            <a href="/api/create_scene" class="btn">إنشاء مشهد تفاعلي</a>
            <a href="/api/prompt" class="btn">توليد موجه (Prompt)</a>
        </div>
    </div>
</body>
</html>
'''

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
        <h1>تسجيل دخول الذئب</h1>
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
    if request.form.get('username') == 'admin' and request.form.get('password') == '159159':
        return render_template_string(dashboard_html)
    return "<h1>بيانات الدخول خاطئة!</h1>"

@app.route('/api/create_scene')
def create_scene():
    return "<h1>✅ تم إنشاء المشهد بنجاح</h1><br><a href='/login'>العودة</a>"

@app.route('/api/prompt')
def generate_prompt():
    return "<h1>✅ تم توليد الموجه بنجاح</h1><br><a href='/login'>العودة</a>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
