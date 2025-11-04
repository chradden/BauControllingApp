from sqlalchemy import Column, Integer, String, Text, Numeric, Date, DateTime, ForeignKey, Enum, JSON, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from . import Base


class InvoiceStatus(str, PyEnum):
    DRAFT = "draft"           # Erfasst/OCR
    IN_REVIEW = "in_review"   # In Prüfung
    APPROVED = "approved"     # Geprüft & freigegeben
    REJECTED = "rejected"     # Abgelehnt
    PAID = "paid"            # Bezahlt


class TaxRate(str, PyEnum):
    ZERO = "zero"      # 0%
    REDUCED = "reduced"  # 7%
    FULL = "full"      # 19%
    REVERSE = "reverse" # Reverse Charge


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)
    invoice_number = Column(String(100), nullable=False)
    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=True)
    status = Column(Enum(InvoiceStatus), nullable=False, default=InvoiceStatus.DRAFT)
    
    # Beträge
    net_amount = Column(Numeric(14, 2), nullable=False, default=0)
    tax_rate = Column(Enum(TaxRate), nullable=False, default=TaxRate.FULL)
    tax_amount = Column(Numeric(14, 2), nullable=False, default=0)
    gross_amount = Column(Numeric(14, 2), nullable=False, default=0)
    
    # Metadaten
    issuer_name = Column(String(255), nullable=True)
    issuer_vat_id = Column(String(50), nullable=True)
    issuer_iban = Column(String(50), nullable=True)
    reference = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    is_partial = Column(Boolean, default=False)
    is_final = Column(Boolean, default=False)
    
    # OCR & Duplikaterkennung
    document_hash = Column(String(64), nullable=True)  # SHA256 des PDFs
    ocr_data = Column(JSON, nullable=True)            # Rohdaten aus OCR
    ocr_confidence = Column(Numeric(5, 2), nullable=True)  # 0-100%
    
    # Prüfung & Zahlung
    review_started_at = Column(DateTime, nullable=True)
    reviewed_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    approved_at = Column(DateTime, nullable=True)
    approved_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    paid_at = Column(DateTime, nullable=True)
    payment_reference = Column(String(100), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    contract = relationship("Contract", back_populates="invoices")
    invoice_lines = relationship("InvoiceLine", back_populates="invoice", cascade="all, delete-orphan")
    reviewed_by = relationship("User", foreign_keys=[reviewed_by_id])
    approved_by = relationship("User", foreign_keys=[approved_by_id])
    approvals = relationship("InvoiceApproval", back_populates="invoice", cascade="all, delete-orphan")
