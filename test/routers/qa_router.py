from fastapi import APIRouter, HTTPException
from services.service import answer_question
from models.question_model import QuestionRequest

# APIRouter 객체 생성
router = APIRouter()

# 질문-답변 API 라우트 정의
@router.post("/ask_question/")
async def ask_question(request: QuestionRequest):
    try:
        result = answer_question(request.question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
