from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from . import Base


class FundingCase(Base):
    """Fördermittel-Fall (z.B. KfW, BAFA etc.)"""
    __tablename__ = "funding_cases"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    provider = Column(String(100), nullable=False)  # z.B. "KfW"
    program = Column(String(100), nullable=False)   # z.B. "433 - Effizenzhaus"
    reference = Column(String(100), nullable=True)  # Aktenzeichen
    total_amount = Column(Numeric(14, 2), nullable=False)
    notes = Column(Text, nullable=True)

    project = relationship("Project", back_populates="funding_cases")
    disbursements = relationship("Disbursement", back_populates="funding_case")


class Disbursement(Base):
    """Auszahlungen von Fördermitteln"""
    __tablename__ = "disbursements"

    id = Column(Integer, primary_key=True)
    funding_case_id = Column(Integer, ForeignKey("funding_cases.id"), nullable=False)
    amount = Column(Numeric(14, 2), nullable=False)
    reference = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)

    funding_case = relationship("FundingCase", back_populates="disbursements")