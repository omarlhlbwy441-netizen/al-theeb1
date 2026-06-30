import sqlite3
import json
import os
from datetime import datetime

class DualCurrencyWallet:
    """نظام إدارة المحفظة المزدوجة المربوط علائقياً بدفتر الأستاذ المالي الموحد"""
    
    def __init__(self, db_path="database/wolf_archive.db", config_path="backend/finance/wallet_config.json"):
        self.db_path = db_path
        self.config_path = config_path
        self.data = {"wolf_tokens": 870.0, "fiat_credits": 1000.0}
        self.load_wallet()

    def load_wallet(self):
        """تحميل الأرصدة المستقرة من ملف التكوين المحمي"""
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.save_wallet()

    def save_wallet(self):
        """حفظ نسخة الحقيقة السريعة للأرصدة"""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def process_transaction(self, amount: float, currency_type: str = "wolf_tokens") -> tuple:
        """معالجة وخصم المعاملات المالية فورياً وتوثيقها بداخل قاعدة البيانات العلائقية"""
        if self.data[currency_type] < amount:
            return False, "❌ خطأ مالي: الرصيد المتوفر غير كافٍ لإتمام هذه العملية."
        
        # تنفيذ الخصم البرمجي
        self.data[currency_type] -= amount
        self.save_wallet()
        
        # التوثيق الفوري في SQLite كـ Audit Log للمستثمرين
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            cursor.execute('''
                INSERT INTO financial_ledger (transaction_type, amount, currency_type, status, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (f"System_Deduction", -amount, currency_type.upper(), "SUCCESS", timestamp))
            
            conn.commit()
            conn.close()
            return True, f"✅ تمت العملية بنجاح. خصم {amount} من {currency_type}"
        except Exception as e:
            return True, f"⚠️ تم الخصم برمجياً وفشل التوثيق العلائقي: {str(e)}"


def process_purchase(user_id, product_id, wallet):
    # 1. جلب بيانات المنتج
    with open("backend/store/store_db.json", "r") as f:
        store_data = json.load(f)
    
    product = next((p for p in store_data['products'] if p['id'] == product_id), None)
    
    if not product:
        return {"status": "error", "message": "المنتج غير موجود."}
    
    # 2. التحقق من الرصيد والخصم
    price = float(product['price'].split(' ')[0])
    if wallet.balance >= price:
        wallet.balance -= price
        return {
            "status": "success", 
            "message": f"تم شراء {product['name']} بنجاح!",
            "product_access_link": f"/archive/downloads/{product_id}"
        }
    else:
        return {"status": "error", "message": "رصيد غير كافٍ."}
