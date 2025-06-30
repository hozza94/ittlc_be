# backend/app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# 라우터 임포트
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.base import Base, engine

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 구체적인 도메인으로 제한하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to ITTLC API"}
