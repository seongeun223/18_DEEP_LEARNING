from fastapi import FastAPI
from routers import qa_router

app = FastAPI()

# 라우터 등록
app.include_router(qa_router.router)
