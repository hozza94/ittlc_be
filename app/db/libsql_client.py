"""
LibSQL 클라이언트 설정
"""
import os
from libsql_client import create_client
from typing import Optional

class LibSQLClient:
    def __init__(self):
        self.url = os.getenv("LIBSQL_URL", "libsql://ittlcdb-hozza.aws-ap-northeast-1.turso.io")
        self.auth_token = os.getenv("LIBSQL_AUTH_TOKEN")
        
        if self.auth_token:
            self.client = create_client(
                url=self.url,
                auth_token=self.auth_token
            )
        else:
            self.client = create_client(url=self.url)
    
    async def execute(self, sql: str, params: Optional[list] = None):
        """SQL 실행"""
        if params:
            return await self.client.execute(sql, params)
        return await self.client.execute(sql)
    
    async def batch(self, statements: list):
        """배치 실행"""
        return await self.client.batch(statements)
    
    async def close(self):
        """클라이언트 종료"""
        await self.client.close()

# 전역 클라이언트 인스턴스
libsql_client = LibSQLClient() 