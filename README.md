# ITTL Backend

ITTL 프로젝트의 백엔드 API 서버입니다.

## 🚀 실행 방법

### 1. 환경 설정

1. Python 가상환경 생성 및 활성화:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

2. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

3. 환경 변수 설정:
`.env` 파일을 프로젝트 루트에 생성하고 다음 내용을 추가:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ittlc_db
DB_USER=your_username
DB_PASSWORD=your_password
```

### 2. 서버 실행

#### 방법 1: Python 스크립트 실행
```bash
python run.py
```

#### 방법 2: Windows 배치 파일 실행
```bash
run.bat
```

#### 방법 3: uvicorn 직접 실행
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 📝 API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **헬스 체크**: http://localhost:8000/health

## 🏗️ 프로젝트 구조

```
ittlc_be/
├── app/
│   ├── api/          # API 라우터
│   ├── core/         # 설정 및 핵심 기능
│   ├── crud/         # 데이터베이스 CRUD 작업
│   ├── db/           # 데이터베이스 설정
│   ├── models/       # SQLAlchemy 모델
│   ├── schemas/      # Pydantic 스키마
│   ├── services/     # 비즈니스 로직
│   └── main.py       # FastAPI 앱
├── requirements.txt  # Python 패키지 의존성
├── run.py           # 서버 실행 스크립트
├── run.bat          # Windows 실행 배치 파일
└── load_env.py      # 환경 변수 로드 테스트
```

## 🔧 기술 스택

- **FastAPI**: 웹 프레임워크
- **SQLAlchemy**: ORM
- **Pydantic**: 데이터 검증
- **Uvicorn**: ASGI 서버
- **MySQL**: 데이터베이스
