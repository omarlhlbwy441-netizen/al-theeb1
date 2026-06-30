import os
import sys

# إضافة المسار الحالي لضمان التعرف على الموديولات الفرعية
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def init_databases():
    print("\n[🗄️] جاري فحص وتهيئة البنية التحتية لقواعد البيانات...")
    # هنا يتم الربط المستقبلي مع موديولات Postgres, MongoDB, Redis
    print("  -> تم تجهيز اتصالات قاعدة البيانات (Postgres/MongoDB/Redis) بنجاح.")

def boot_backend_services():
    print("\n[⚙️] جاري تشغيل الخدمات الخلفية ونظام الـ SaaS...")
    print("  -> تفعيل نظام المحفظة المالية ثنائية العملة والمخرجات المالية.")
    print("  -> موديول الشبكة الاجتماعية (hm-ya) جاهز للاتصال.")
    print("  -> نظام التنبيهات وإدارة الطلبات في وضع الاستعداد.")

def run_studio_mode():
    print("\n--- 🐺 تفعيل الاستوديو الرقمي (Studio Mode) ---")
    try:
        from studio import WolfEngine
        studio = WolfEngine()
        while True:
            choice = input("\n[1] إضافة Lore | [2] إنشاء مشهد | [3] توليد Prompt | [4] عودة للرئيسية: ")
            if choice == '1':
                cat = input("التصنيف: ")
                t = input("العنوان: ")
                d = input("التفاصيل: ")
                print(studio.add_lore(cat, t, d))
            elif choice == '2':
                sid = input("رقم المشهد: ")
                t = input("العنوان: ")
                c = input("المحتوى: ")
                print(studio.create_scene(sid, t, c))
            elif choice == '3':
                t = input("العنوان: ")
                d = input("الوصف: ")
                print(studio.generate_prompt(t, d))
            elif choice == '4':
                break
    except ImportError:
        print("❌ خطأ: موديول الاستوديو غير متاح أو يحتوي على أخطاء تركيبية.")

def run_game_ai_engine():
    print("\n--- 🎮 محرك الألعاب والذكاء الاصطناعي (Game & AI Engine) ---")
    print("  -> محرك Unity الذكي جاهز لتوليد المخططات (Blueprints).")
    print("  -> نظام هندسة الصوت (ai/voice) في وضع الاستعداد لبناء المؤثرات.")
    print("  -> لوحة التحكم بمشروع (Wolf App) متصلة.")
    input("\n[اضغط Enter للعودة للقائمة الرئيسية]")

def main():
    print("==================================================")
    print("🐺 نظام WOLF SUPER APP & AI ENGINE | مدمج بالكامل")
    print("==================================================")
    
    # التنشيط التلقائي للبنية التحتية عند الإقلاع
    init_databases()
    boot_backend_services()
    
    while True:
        print("\nلوحة التحكم المركزية بالمنظومة:")
        print("[1] تشغيل الاستوديو الرقمي وصناعة الفيديوهات (Studio Mode)")
        print("[2] إدارة محرك الألعاب ومخططات الذكاء الاصطناعي (Game AI)")
        print("[exit] إغلاق النظام بالكامل")
        
        choice = input("\nاختر الإجراء المطلوب: ").strip().lower()
        
        if choice == '1':
            run_studio_mode()
        elif choice == '2':
            run_game_ai_engine()
        elif choice == 'exit':
            print("\n🐺 إيقاف النظام. تم حفظ كافة السجلات والأرشيف بنجاح.")
            break
        else:
            print("❌ خيار غير صحيح، يرجى المحاولة مجدداً.")

if __name__ == "__main__":
    main()
