import json

class DualCurrencyWallet:
    def __init__(self, wallet_file="backend/finance/wallet_data.json"):
        self.wallet_file = wallet_file
        self.load_wallet()

    def load_wallet(self):
        try:
            with open(self.wallet_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"fiat_credits": 1000.0, "wolf_tokens": 500.0}
            self.save_wallet()

    def save_wallet(self):
        with open(self.wallet_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def get_balances(self):
        return f"💳 رصيد المحفظة الديجيتال: {self.data['fiat_credits']} كاش | {self.data['wolf_tokens']} عملة وولف التفاعلية"

    def process_transaction(self, amount, currency_type="wolf_tokens"):
        if currency_type in self.data and self.data[currency_type] >= amount:
            self.data[currency_type] -= amount
            self.save_wallet()
            return True, f"✅ تمت العملية بنجاح. خصم {amount} من {currency_type}"
        return False, "❌ رصيد غير كافٍ لإتمام العملية البرمجية."
