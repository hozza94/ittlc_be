# backend/app/models/member.py
from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey, Enum
from sqlalchemy.sql import func
from ..db.base import Base
import enum

class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"

class Member(Base):
    __tablename__ = "members"

    member_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=True)
    sex = Column(Enum(Gender), nullable=True)
    birthday = Column(Date, nullable=True)
    contact = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    job = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    baptism = Column(Boolean, default=False)
    marriage = Column(Boolean, default=False)
    prev_church = Column(String(100), nullable=True)
    registration_date = Column(Date, nullable=True)
    memo = Column(Text, nullable=True)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())