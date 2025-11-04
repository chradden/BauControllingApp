from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from . import Base


class ApprovalType(str, PyEnum):
    TECHNICAL = "technical"     # Sachliche Prüfung (Bauleitung)
    FINANCIAL = "financial"     # Rechnerische Prüfung (Controlling)
    MANAGEMENT = "management"   # Geschäftsführung


class ApprovalStatus(str, PyEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class InvoiceApproval(Base):
    """Freigabe-Workflow für Rechnungen (4-Augen-Prinzip)"""
    __tablename__ = "invoice_approvals"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(Enum(ApprovalType), nullable=False)
    status = Column(Enum(ApprovalStatus), nullable=False, default=ApprovalStatus.PENDING)
    comment = Column(Text, nullable=True)
    approved_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    invoice = relationship("Invoice", back_populates="approvals")
    user = relationship("User")