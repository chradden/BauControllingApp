from sqlalchemy import Column, Integer, String, Boolean, DateTime, Table, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from . import Base


class UserRole(str, PyEnum):
    ADMIN = "admin"               # System-Admin
    MANAGER = "manager"           # Geschäftsführung
    CONTROLLER = "controller"     # Controlling
    SUPERVISOR = "supervisor"     # Bauleitung
    CLERK = "clerk"              # Sachbearbeitung
    VIEWER = "viewer"            # Nur Lesezugriff


# Many-to-Many: User <-> Project (für Projekt-Teams)
user_projects = Table(
    "user_projects",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(200), nullable=True)
    hashed_password = Column(String(255), nullable=True)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.VIEWER)
    
    # Additional fields
    phone = Column(String(50), nullable=True)
    department = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    owned_projects = relationship("Project", back_populates="owner")  # Als Owner
    projects = relationship("Project", secondary=user_projects, back_populates="team")  # Als Teammitglied
