from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from . import Base


class ContractStatus(str, PyEnum):
    DRAFT = "draft"
    SENT = "sent"
    SIGNED = "signed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ContractType(str, PyEnum):
    MAIN = "main"           # Hauptauftrag
    AMENDMENT = "amendment" # Nachtrag
    SERVICE = "service"     # Dienstleistung
    SUPPLY = "supply"       # Lieferung


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    parent_id = Column(Integer, ForeignKey("contracts.id"), nullable=True)  # Für Nachträge
    contractor = Column(String(255), nullable=True)
    contract_number = Column(String(50), nullable=True)
    contract_date = Column(Date, nullable=True)
    type = Column(Enum(ContractType), nullable=False, default=ContractType.MAIN)
    status = Column(Enum(ContractStatus), nullable=False, default=ContractStatus.DRAFT)
    description = Column(Text, nullable=True)
    value = Column(Numeric(14, 2), nullable=False, default=0)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    # Relationships
    project = relationship("Project", back_populates="contracts")
    parent = relationship("Contract", remote_side=[id], backref="amendments")
    invoices = relationship("Invoice", back_populates="contract", cascade="all, delete-orphan")
    cost_assignments = relationship("ContractCostAssignment", back_populates="contract")
