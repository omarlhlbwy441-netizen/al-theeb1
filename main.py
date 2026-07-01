import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

login_html = '''
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head><meta charset="UTF-8"><title>تسجيل الدخول - الذيب</title></head>
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
    return jsonify({"message": "تمت محاولة تسجيل الدخول بنجاح!"})

if __name__ == '__main__':
    # تم إيقاف التشغيل المحلي لمنع رسائل السيرفر
    print("تم إعداد التطبيق للعمل على Railway.")
