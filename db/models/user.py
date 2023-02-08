from sqlalchemy import Column, Enum, String, Boolean, ForeignKey, Text, Integer
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import Timestamp
import enum

class Role(enum.Enum):
    teacher = 1
    student = 2


class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)
    
    profile = relationship("Profile", back_populates="owner", uselist=False)

class Profile(Timestamp, Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")