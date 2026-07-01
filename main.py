from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>تم التشغيل بنجاح! التطبيق يعمل الآن عبر Gunicorn.</h1>"

if __name__ == '__main__':
    app.run()
