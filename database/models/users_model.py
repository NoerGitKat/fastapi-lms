import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from database.main import Base
from .mixins import TimestampMixin


class Role(enum.Enum):
    teacher = 1
    student = 2


# Models
class User(TimestampMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))

    # Establish 1-1 relationship
    profile = relationship("Profile", back_populates="owner", uselist=False)


class Profile(TimestampMixin, Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)

    # Establish 1-1 relationship
    user_id = Column(Integer, ForeignKey("users.id"))
    student = relationship("User", back_populates="profile")
