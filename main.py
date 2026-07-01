import os
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

login_html = '''
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head><meta charset="UTF-8"><title>الذيب - دخول</title></head>
<body>
    <h1>مرحباً بك في الذيب</h1>
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="اسم المستخدم" required><br>
        <input type="password" name="password" placeholder="كلمة المرور" required><br>
        <button type="submit">دخول</button>
    </form>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(login_html)

@app.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "تمت محاولة تسجيل الدخول!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
