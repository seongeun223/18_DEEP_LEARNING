from fastapi import FastAPI
from services.translation import perform_translation
from models.translation import TranslationRequest

app = FastAPI()

@app.post("/translate")
async def translate(request: TranslationRequest):
    
    result = perform_translation(request.text, request.lang)
    
    return {"translated_text" : result}
