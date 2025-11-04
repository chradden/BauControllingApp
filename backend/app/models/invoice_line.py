from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class InvoiceLine(Base):
    """Einzelposition einer Rechnung mit Zuordnung zur DIN276-Kostengruppe"""
    __tablename__ = "invoice_lines"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    cost_group_id = Column(Integer, ForeignKey("din276_cost_groups.id"), nullable=False)
    description = Column(Text, nullable=True)
    quantity = Column(Numeric(10, 3), nullable=False, default=1)
    unit = Column(String(20), nullable=True)  # z.B. "m²", "Stück"
    unit_price = Column(Numeric(14, 2), nullable=False)
    amount = Column(Numeric(14, 2), nullable=False)  # quantity * unit_price

    invoice = relationship("Invoice", back_populates="invoice_lines")
    cost_group = relationship("DIN276CostGroup")