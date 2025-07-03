# backend/app/crud/member.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.member_id == member_id).first()

def get_member_by_email(db: Session, email: str):
    return db.query(models.Member).filter(models.Member.email == email).first()

def get_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Member).offset(skip).limit(limit).all()

def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def update_member(db: Session, db_member: models.Member, member: schemas.MemberUpdate):
    update_data = member.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_member, field, value)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def delete_member(db: Session, member_id: int):
    db_member = db.query(models.Member).filter(models.Member.member_id == member_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()
    return db_member