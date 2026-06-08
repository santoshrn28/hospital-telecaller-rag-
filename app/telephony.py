from fastapi import APIRouter, Request
from main import generate_response

router = APIRouter()

@router.post("/voice")
async def voice(req: Request):
    data = await req.form()
    speech_text = data.get("SpeechResult")

    reply = generate_response(speech_text)

    return f"""
    <Response>
        <Say>{reply}</Say>
    </Response>
    """
