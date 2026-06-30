
class WalletManager:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deduct_funds(self, amount: float) -> bool:
        """خصم الرصيد مع التحقق"""
        if amount <= 0:
            return False
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def add_funds(self, amount: float):
        """إضافة رصيد (شحن المحفظة)"""
        if amount > 0:
            self.balance += amount

    def get_balance(self):
        return self.balance
