import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>الذيب - al-theeb1</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma; background: #1a1a2e; color: #fff; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #e94560; }
            .btn { background: #e94560; color: white; padding: 15px 30px; border: none; 
                   border-radius: 8px; cursor: pointer; margin: 10px; font-size: 16px; }
            .btn:hover { background: #c13651; }
            #output { background: #16213e; padding: 20px; border-radius: 10px; 
                      margin-top: 20px; min-height: 100px; white-space: pre-wrap; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐺 الذيب - نظام الإنتاج التفاعلي</h1>
            <button class="btn" onclick="runAction('create_scene')">🎬 إنشاء مشهد</button>
            <button class="btn" onclick="runAction('wallet')">💰 المحفظة</button>
            <button class="btn" onclick="runAction('prompt')">✨ توليد موجه</button>
            <div id="output">اضغط على أي زر للبدء...</div>
        </div>
        <script>
            async function runAction(action) {
                document.getElementById('output').innerText = 'جاري التنفيذ...';
                const res = await fetch('/api/' + action);
                const data = await res.json();
                document.getElementById('output').innerText = data.result || data.error;
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/api/create_scene')
def api_create_scene():
    return jsonify({"result": "✅ تم إنشاء المشهد التفاعلي بنجاح!"})

@app.route('/api/wallet')
def api_wallet():
    return jsonify({"result": "💰 رصيد المحفظة: $1,000"})

@app.route('/api/prompt')
def api_prompt():
    return jsonify({"result": "✅ تم توليد الموجه بنجاح!"})

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
