from fastapi import APIRouter, HTTPException
from services.service import answer_question
from models.question_model import QuestionRequest

# APIRouter 객체 생성
router = APIRouter()

# 질문-답변 API 라우트 정의
@router.post("/ask_question")
async def ask_question(request: QuestionRequest):
    print("요청 들어옴!")
    try:
        result = await answer_question(request.question)  # 비동기 함수 호출 시 await 추가
        return result
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

