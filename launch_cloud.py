
import os
import subprocess

def launch_system():
    print("🚀 جاري إطلاق المنظومة في بيئة الإنتاج السحابي...")
    # أمر التشغيل المعتمد على كونفج السحابة
    subprocess.run(["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"])

if __name__ == "__main__":
    launch_system()
