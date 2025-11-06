from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from . import Base
from .user import user_projects


class ProjectStatus(str, PyEnum):
    PLANNED = "planned"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(Enum(ProjectStatus), nullable=False, default=ProjectStatus.PLANNED)
    
    # Erweiterte Felder für Bau-Controlling
    application_id = Column(String(50), nullable=True)  # Bauantrags-Nr
    permit_id = Column(String(50), nullable=True)      # Genehmigungsnummer
    funding_id = Column(String(50), nullable=True)     # Förderkennzeichen
    
    # Relationships
    contracts = relationship("Contract", back_populates="project", cascade="all, delete-orphan")
    budget_lines = relationship("BudgetLine", back_populates="project", cascade="all, delete-orphan")
    owner = relationship("User", back_populates="owned_projects")
    team = relationship("User", secondary=user_projects, back_populates="projects")
    funding_cases = relationship("FundingCase", back_populates="project", cascade="all, delete-orphan")
