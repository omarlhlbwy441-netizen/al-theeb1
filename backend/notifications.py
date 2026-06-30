
import datetime

def send_notification(event_type, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] 📢 [إشعار {event_type}]: {message}"
    
    # في الواقع، هنا يمكن ربط خدمة SMTP (إيميل) أو Telegram API
    print(formatted_msg)
    
    # تسجيل الإشعار في ملف (Log)
    with open("/content/al-theeb1/system_alerts.log", "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")

# تجربة الإشعار
send_notification("نظام", "تم تفعيل لوحة التحكم التنفيذية بنجاح.")
