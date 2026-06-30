from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Wolf AI Core")

class ChatRequest(BaseModel):
    user_id: int
    message: str

@app.post("/api/ai/chat")
async def chat_with_ai(req: ChatRequest):
    # هنا يتم الربط الفعلي بمكتبة OpenAI أو Claude
    response_text = f"مرحباً يا ملك الذئاب.. لقد استلمت رسالتك: '{req.message}'. جاري التنفيذ!"
    
    return {
        "role": "assistant",
        "content": response_text,
        "status": "success"
    }
