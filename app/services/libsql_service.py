"""
LibSQL 직접 연결 서비스
"""
import os
from typing import Optional, List, Dict, Any
from libsql_client import create_client
from dotenv import load_dotenv
from pathlib import Path

# .env 파일 로드
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

class LibSQLService:
    def __init__(self):
        self.libsql_url = os.getenv("LIBSQL_URL")
        self.auth_token = os.getenv("LIBSQL_AUTH_TOKEN")
        
        if not self.libsql_url or not self.auth_token:
            raise ValueError("LIBSQL_URL과 LIBSQL_AUTH_TOKEN이 설정되지 않았습니다.")
        
        # HTTP URL로 변환
        self.http_url = self.libsql_url.replace("libsql://", "https://")
        self.client = None
    
    async def get_client(self):
        """LibSQL 클라이언트 반환"""
        if self.client is None:
            self.client = create_client(url=self.http_url, auth_token=self.auth_token)
        return self.client
    
    async def close(self):
        """클라이언트 종료"""
        if self.client:
            await self.client.close()
            self.client = None
    
    # User 관련 메서드
    async def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """사용자 생성"""
        client = await self.get_client()
        sql = """
        INSERT INTO users (email, password_hash, username, role, is_active, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """
        result = await client.execute(sql, [
            user_data['email'],
            user_data['password_hash'],
            user_data['username'],
            user_data.get('role', 'user'),
            user_data.get('is_active', True)
        ])
        return {"user_id": result.last_insert_id}
    
    async def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """이메일로 사용자 조회"""
        client = await self.get_client()
        sql = "SELECT * FROM users WHERE email = ?"
        result = await client.execute(sql, [email])
        if result.rows:
            return dict(zip([col.name for col in result.columns], result.rows[0]))
        return None
    
    async def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """ID로 사용자 조회"""
        client = await self.get_client()
        sql = "SELECT * FROM users WHERE user_id = ?"
        result = await client.execute(sql, [user_id])
        if result.rows:
            return dict(zip([col.name for col in result.columns], result.rows[0]))
        return None
    
    async def get_users(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """사용자 목록 조회"""
        client = await self.get_client()
        sql = "SELECT * FROM users LIMIT ? OFFSET ?"
        result = await client.execute(sql, [limit, skip])
        return [dict(zip([col.name for col in result.columns], row)) for row in result.rows]
    
    # Member 관련 메서드
    async def create_member(self, member_data: Dict[str, Any]) -> Dict[str, Any]:
        """멤버 생성"""
        client = await self.get_client()
        sql = """
        INSERT INTO members (name, age, sex, birthday, contact, address, job, email, 
                           baptism, marriage, prev_church, registration_date, memo, 
                           created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """
        result = await client.execute(sql, [
            member_data['name'],
            member_data.get('age'),
            member_data.get('sex'),
            member_data.get('birthday'),
            member_data.get('contact'),
            member_data.get('address'),
            member_data.get('job'),
            member_data.get('email'),
            member_data.get('baptism', False),
            member_data.get('marriage', False),
            member_data.get('prev_church'),
            member_data.get('registration_date'),
            member_data.get('memo')
        ])
        return {"member_id": result.last_insert_id}
    
    async def get_member_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """이메일로 멤버 조회"""
        client = await self.get_client()
        sql = "SELECT * FROM members WHERE email = ?"
        result = await client.execute(sql, [email])
        if result.rows:
            return dict(zip([col.name for col in result.columns], result.rows[0]))
        return None
    
    async def get_member_by_id(self, member_id: int) -> Optional[Dict[str, Any]]:
        """ID로 멤버 조회"""
        client = await self.get_client()
        sql = "SELECT * FROM members WHERE member_id = ?"
        result = await client.execute(sql, [member_id])
        if result.rows:
            return dict(zip([col.name for col in result.columns], result.rows[0]))
        return None
    
    async def get_members(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """멤버 목록 조회"""
        client = await self.get_client()
        sql = "SELECT * FROM members LIMIT ? OFFSET ?"
        result = await client.execute(sql, [limit, skip])
        return [dict(zip([col.name for col in result.columns], row)) for row in result.rows]
    
    async def update_member(self, member_id: int, member_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """멤버 업데이트"""
        client = await self.get_client()
        
        # 업데이트할 필드들
        update_fields = []
        values = []
        
        for key, value in member_data.items():
            if value is not None and key != 'member_id':
                update_fields.append(f"{key} = ?")
                values.append(value)
        
        if not update_fields:
            return None
        
        update_fields.append("updated_at = CURRENT_TIMESTAMP")
        values.append(member_id)
        
        sql = f"UPDATE members SET {', '.join(update_fields)} WHERE member_id = ?"
        await client.execute(sql, values)
        
        return await self.get_member_by_id(member_id)
    
    async def delete_member(self, member_id: int) -> bool:
        """멤버 삭제"""
        client = await self.get_client()
        sql = "DELETE FROM members WHERE member_id = ?"
        result = await client.execute(sql, [member_id])
        return result.rows_affected > 0

# 전역 LibSQL 서비스 인스턴스
libsql_service = LibSQLService() 