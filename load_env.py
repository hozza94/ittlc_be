# backend/load_env.py
import os
import sys
from pathlib import Path

# 프로젝트 루트를 시스템 경로에 추가
project_root = str(Path(__file__).parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from dotenv import load_dotenv
from app.core.config import settings, SQLALCHEMY_DATABASE_URL

# .env 파일 로드
load_dotenv()

print(f"DB_HOST: {settings.DB_HOST}")
print(f"DB_USER: {settings.DB_USER}")
print(f"DB_NAME: {settings.DB_NAME}")
print(f"DB_PORT: {settings.DB_PORT}")
print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")  # 비밀번호는 출력하지 않음