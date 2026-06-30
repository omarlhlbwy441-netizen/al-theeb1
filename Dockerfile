
FROM python:3.10-slim

WORKDIR /app

# نسخ المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ كامل المشروع
COPY . .

# تشغيل التطبيق
CMD ["uvicorn", "wolf-app.main:app", "--host", "0.0.0.0", "--port", "8000"]
