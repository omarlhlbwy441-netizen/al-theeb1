import sqlite3
from datetime import datetime

class WolfEngine:
    """محرك الأرشفة المعرفية (Lore) وصياغة المشاهد السينمائية لـ WOLF AI"""
    
    def __init__(self, db_path="database/wolf_archive.db"):
        self.db_path = db_path

    def add_lore(self, category: str, title: str, description: str) -> str:
        """أرشفة البيانات الروائية والعمق التاريخي للمنظومة داخل قاعدة البيانات"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            cursor.execute('''
                INSERT OR REPLACE INTO lore_archive (category, title, description, archived_at)
                VALUES (?, ?, ?, ?)
            ''', (category, title, description, timestamp))
            
            conn.commit()
            conn.close()
            return f"✅ تم حفظ وتوثيق الـ Lore المعرفي الكياني [{title}] بنجاح في تصنيف {category}."
        except Exception as e:
            return f"❌ فشل أرشفة الـ Lore علائقياً: {str(e)}"

    def create_scene(self, scene_id: str, title: str, content: str) -> str:
        """توثيق وحفظ المشاهد السينمائية والسيناريوهات الناتجة من مخرجات الذكاء الاصطناعي"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            cursor.execute('''
                INSERT OR REPLACE INTO generated_scenes (scene_id, title, content, tokens_spent, produced_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (scene_id, title, content, 10.0, timestamp))
            
            conn.commit()
            conn.close()
            return f"🎬 [Engine] تم صياغة المشهد الرقمي [{title}] وتوثيقه تحت المعرف الإلزامي: {scene_id}."
        except Exception as e:
            return f"❌ خطأ داخلي في نواة المحرك السينمائي: {str(e)}"
