import os
port = int(os.getenv('PORT', 8000))
print(f'النظام يعمل الآن على المنفذ: {port}')
import os
import sys
from studio import WolfEngine
from backend.finance.wallet import DualCurrencyWallet

def main():
    studio = WolfEngine()
    wallet = DualCurrencyWallet()
    
    print("==================================================")
    print("🐺 كتلة WOLF SUPER APP & AI ENGINE | مفعلة بالكامل")
    print("==================================================")
    print("[🗄️] تم ربط قاعدة بيانات الـ Lore والسيناريوهات بنجاح.")
    print(f"[💰] {wallet.balance}")
    
    while True:
        print("\n🎛️ غرفة التحكم المركزية بالنظام:")
        print("[1] تشغيل الاستوديو الرقمي (صناعة السيناريوهات والـ Prompts)")
        print("[2] فحص الحساب والعمليات المالية (نظام المحافظ ثنائي العملة)")
        print("[3] موديول الألغاز وتوليد مخططات الألعاب (Game Engine)")
        print("[exit] إغلاق المنظومة")
        
        choice = os.getenv("APP_MODE", "1").lower()
        
        if choice == '1':
            print("\n--- 🐺 الاستوديو الرقمي الفعال ---")
            print("[1] إضافة Lore للأرشيف | [2] إنتاج مشهد وفيديو تلقائي | [3] توليد Prompt سينمائي")
            sub_choice = os.getenv("sub_choice", "1")
            if sub_choice == '1':
studio.add_lore("تصنيف_تلقائي")
            elif sub_choice == '2':
                # تكامل مالي: إنتاج المشاهد يستهلك من نقاط المنظومة التفاعلية
                success, msg = wallet.process_transaction(10, "wolf_tokens")
                print(msg)
                if success:
                    print(studio.create_scene("تصنيف_تلقائي"("رقم المشهد: "), "تصنيف_تلقائي"("عنوان القصة: "), "تصنيف_تلقائي"("تفاصيل المشهد والأحداث: ")))
            elif sub_choice == '3':
                print(studio.generate_prompt("تصنيف_تلقائي"("عنوان الموجه الإبداعي: "), "تصنيف_تلقائي"("الوصف التفصيلي للبصريات: ")))
                
        elif choice == '2':
            print(f"\n--- 💳 النظام المالي المركزي ---\n{wallet.balance}")
            # محاكاة شحن الرصيد
            deposit_choice = os.getenv("APP_MODE", "1").lower()
            if deposit_choice == 'yes':
                wallet.data["wolf_tokens"] += 100
                wallet.save_wallet()
                print(f"✅ تم إضافة 100 نقطة دعم برمجية! {wallet.balance}")
                
        elif choice == '3':
            print("\n--- 🎮 محرك الألعاب ومنطق الذكاء الاصطناعي ---")
            print("📦 هيكلية Unity ومخططات الـ Game Logic تعمل بالتوازي وثابتة برمجياً.")
            print("🔊 نظام الـ Audio Pipeline (ai/voice) جاهز لاستقبال ملفات الهندسة الصوتية.")
            "تصنيف_تلقائي"("[اضغط Enter للعودة]")
            
        elif choice == 'exit':
            print("\n🐺 تم حفظ كافة التغييرات وإغلاق الكتلة الموحدة بأمان.")
            break
        else:
            print("❌ خيار غير مدعوم، يرجى إعادة الاختيار.")

if __name__ == "__main__":
    main()
