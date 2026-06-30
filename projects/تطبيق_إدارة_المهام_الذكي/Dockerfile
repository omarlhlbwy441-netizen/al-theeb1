# استخدام بيئة Node.js خفيفة وسريعة
FROM node:18-alpine

# تحديد مسار العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات الاعتماديات وتثبيتها
COPY package.json ./
RUN npm install || echo "No dependencies to install yet"

# نسخ باقي ملفات المشروع
COPY . .

# فتح المنفذ 3000 للواجهة
EXPOSE 3000

# أمر التشغيل الافتراضي
CMD ["node", "api_gateway.js"]
