# backend/app/db/test_db_connection.py
import sys
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from .base import engine, SessionLocal

def test_connection():
    print("🔍 데이터베이스 연결을 테스트합니다...")
    
    # 1. 엔진을 통한 연결 테스트
    try:
        with engine.connect() as conn:
            # SQLAlchemy 2.0+에서는 text()로 감싸야 합니다.
            result = conn.execute(text("SELECT 1"))
            print("✅ 데이터베이스 연결 성공!")
            print(f"   - 데이터베이스 버전: {conn.dialect.server_version_info}")
    except Exception as e:
        print(f"❌ 데이터베이스 연결 실패: {e}")
        return False

    # 2. 세션을 통한 연결 테스트
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("✅ 데이터베이스 세션 생성 성공!")
        db.close()
        return True
    except Exception as e:
        print(f"❌ 데이터베이스 세션 생성 실패: {e}")
        return False

if __name__ == "__main__":
    if test_connection():
        print("\n✅ 모든 테스트가 성공적으로 완료되었습니다!")
        sys.exit(0)
    else:
        print("\n❌ 테스트 중 오류가 발생했습니다.")
        sys.exit(1)