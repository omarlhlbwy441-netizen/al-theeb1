
import sys
import os
sys.path.append("/content/drive/MyDrive/wolf-super-app")

from fastapi import FastAPI, HTTPException
from app.services.auth import AuthManager
from app.services.wallet import WalletManager
from app.services.ai_bridge import AIBridge, ChatRequest

app = FastAPI(title="Wolf Super App")

# تهيئة الخدمات
wallet_service = WalletManager()
ai_service = AIBridge()

@app.get("/")
async def root():
    return {"message": "نظام الذئب يعمل بكامل طاقته!"}

@app.post("/wallet/charge")
async def charge_wallet(user_id: str, amount: float):
    await wallet_service.update_balance(user_id, amount)
    return {"status": "success", "user": user_id, "amount_added": amount}

@app.post("/ai/chat")
async def chat_with_ai(request: ChatRequest):
    # خصم تكلفة الخدمة
    if not await wallet_service.update_balance(request.user_id, -1.0):
        raise HTTPException(status_code=402, detail="رصيد غير كافٍ")
    
    response = await ai_service.get_response(request.user_id, request.message)
    return {"response": response, "cost": 1.0}
