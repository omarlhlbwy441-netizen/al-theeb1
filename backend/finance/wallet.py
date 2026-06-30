
import json
import os

class DualCurrencyWallet:
    def __init__(self, balance=0):
        self.balance = balance

def process_purchase(user_id, product_id, wallet):
    # مسار قاعدة البيانات
    store_db_path = "/content/al-theeb1/backend/store/store_db.json"
    
    if not os.path.exists(store_db_path):
        return {"status": "error", "message": "قاعدة بيانات المتجر غير موجودة."}
        
    with open(store_db_path, "r", encoding="utf-8") as f:
        store_data = json.load(f)
    
    product = next((p for p in store_data['products'] if p['id'] == product_id), None)
    
    if not product:
        return {"status": "error", "message": "المنتج غير موجود."}
    
    # استخراج السعر
    try:
        price = float(product['price'].split(' ')[0])
    except:
        return {"status": "error", "message": "خطأ في تنسيق سعر المنتج."}
    
    if wallet.balance >= price:
        wallet.balance -= price
        return {
            "status": "success", 
            "message": f"تم شراء {product['name']} بنجاح!",
            "product_access_link": f"/archive/downloads/{product_id}"
        }
    else:
        return {"status": "error", "message": "رصيد غير كافٍ."}
