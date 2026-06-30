import json
import os

class WolfEngine:
    def __init__(self, db_file="lore_database.json"):
        self.db_file = db_file
        self.load_db()
        os.makedirs("prompts", exist_ok=True)
        os.makedirs("scenes", exist_ok=True)

    def load_db(self):
        try:
            with open(self.db_file, "r", encoding="utf-8") as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            self.save_db()

    def save_db(self):
        with open(self.db_file, "w", encoding="utf-8") as f:
            json.dump(self.db, f, ensure_ascii=False, indent=4)

    def add_lore(self, category, title, description):
        if category not in self.db:
            self.db[category] = []
        self.db[category].append({"title": title, "description": description})
        self.save_db()
        return f"📚 تم أرشفة المرجعية [{title}] في تصنيف [{category}] بنجاح."

    def create_scene(self, scene_id, title, content):
        filename = f"scenes/scene_{scene_id}_{title.replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"🎬 عنوان المشهد: {title}\n\n{content}")
        return f"🎬 تم توليد وحفظ ملف المشهد السينمائي في: {filename}"

    def generate_prompt(self, title, description):
        filename = f"prompts/prompt_{title.replace(' ', '_')}.txt"
        ai_prompt = f"Objective: Generate high-end AI Video/Image context for {title}. Style: Cinematic Neo-Tokyo, hyper-realistic, detailed lighting. Core Concept: {description}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(ai_prompt)
        return f"🎯 تم إنتاج وتجهيز موجه الذكاء الاصطناعي للفيديو في: {filename}"
