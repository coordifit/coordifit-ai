"""User model definition."""

from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base


class User(Base):
    """Example user model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
