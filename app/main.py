from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
import uvicorn

# FastAPI 앱 생성
app = FastAPI(
    title="ITTL Backend API",
    description="ITTL 백엔드 API 서버",
    version="1.0.0"
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 특정 도메인만 허용하도록 설정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 헬스 체크 엔드포인트
@app.get("/")
async def root():
    return {"message": "ITTL Backend API 서버가 실행 중입니다."}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "서버가 정상적으로 실행 중입니다."}

# API 라우터들을 여기에 추가할 예정
# from app.api.v1 import router as api_v1
# app.include_router(api_v1, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
