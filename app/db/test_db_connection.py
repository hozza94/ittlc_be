# backend/app/db/test_db_connection.py
import os
import sys
from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# 프로젝트 루트 디렉토리를 시스템 경로에 추가
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

# 이제 app 모듈을 import 할 수 있습니다
from app.core.config import SQLALCHEMY_DATABASE_URL

# 로깅 설정
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_db_connection():
    db = None
    try:
        db = SessionLocal()
        # 간단한 쿼리 실행
        db.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}", file=sys.stderr)
        return False
    finally:
        if db is not None:
            db.close()

if __name__ == "__main__":
    if test_db_connection():
        print("테스트가 성공적으로 완료되었습니다.")
    else:
        print("테스트 중 오류가 발생했습니다.")