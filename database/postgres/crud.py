from sqlalchemy.orm import Session
from models import User, Transaction, StoreAddon

# دالة لإنشاء مستخدم جديد بمحفظة مالية
def create_user(db: Session, username: str):
    new_user = User(username=username, wallet_balance=0.0)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# دالة لتسجيل عمليات الشراء في المتجر وتحديث الرصيد
def process_store_purchase(db: Session, user_id: int, amount: float):
    user = db.query(User).filter(User.id == user_id).first()
    
    if user and user.wallet_balance >= amount:
        # خصم الرصيد
        user.wallet_balance -= amount
        # تسجيل العملية في الأرشيف المالي
        tx = Transaction(user_id=user_id, amount=-amount, tx_type="store_purchase")
        db.add(tx)
        
        db.commit()
        return True
    return False
