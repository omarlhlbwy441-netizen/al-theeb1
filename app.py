from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from studio import WolfEngine
from backend.finance.wallet import DualCurrencyWallet

app = FastAPI(
    title="Wolf Super App & AI Engine API",
    description="الواجهة البرمجية المركزية لإدارة أنظمة الذكاء الاصطناعي، المحافظ المالية، والاستوديو الرقمي للإنتاج",
    version="1.0.0"
)

# تفعيل الـ CORS للسماح لواجهات العرض والمتصفحات بالاتصال الآمن بالسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

studio = WolfEngine()
wallet = DualCurrencyWallet()

class LoreInput(BaseModel):
    category: str
    title: str
    description: str

class SceneInput(BaseModel):
    scene_id: str
    title: str
    content: str

class PromptInput(BaseModel):
    title: str
    description: str

class DepositInput(BaseModel):
    amount: float

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "🐺 خادم Wolf AI يعمل بكفاءة ككتلة ويب موحدة ومستقرة",
        "system_balances": wallet.get_balances()
    }

@app.get("/wallet/balance")
def get_balance():
    return {"balances": wallet.get_balances(), "raw_data": wallet.data}

@app.post("/wallet/deposit")
def deposit_tokens(payload: DepositInput):
    wallet.data["wolf_tokens"] += payload.amount
    wallet.save_wallet()
    return {"message": f"✅ تم شحن {payload.amount} عملة وولف بنجاح", "balances": wallet.get_balances()}

@app.post("/studio/lore")
def add_new_lore(payload: LoreInput):
    result = studio.add_lore(payload.category, payload.title, payload.description)
    return {"message": result}

@app.post("/studio/scene")
def create_new_scene(payload: SceneInput):
    success, msg = wallet.process_transaction(10, "wolf_tokens")
    if not success:
        raise HTTPException(status_code=402, detail=msg)
    result = studio.create_scene(payload.scene_id, payload.title, payload.content)
    return {"transaction_status": msg, "studio_result": result}

@app.post("/studio/prompt")
def generate_ai_prompt(payload: PromptInput):
    result = studio.generate_prompt(payload.title, payload.description)
    return {"message": result}
