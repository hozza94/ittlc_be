#!/usr/bin/env python3
"""
ITTL Backend 서버 실행 스크립트
"""
import uvicorn
from app.main import app

if __name__ == "__main__":
    print("🚀 ITTL Backend 서버를 시작합니다...")
    print("📝 API 문서: http://localhost:8000/docs")
    print("🔍 ReDoc 문서: http://localhost:8000/redoc")
    print("💚 헬스 체크: http://localhost:8000/health")
    print("-" * 50)
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 