
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Wolf AI & Voice Core")

class QueryRequest(BaseModel):
    user_input: str

@app.post("/generate_code")
async def generate_code(req: QueryRequest):
    # مسار مربوط بـ OpenAI/Claude
    return {"status": "success", "data": "Code generated via AI"}

@app.post("/speech_to_text")
async def process_voice(audio_data: bytes):
    # مسار مربوط بـ Whisper API
    return {"status": "success", "text": "تم تحويل الصوت إلى نص"}
