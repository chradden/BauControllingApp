from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from . import Base


class ContractCostAssignment(Base):
    """Zuordnung von Vertragsanteilen zu DIN276-Kostengruppen"""
    __tablename__ = "contract_cost_assignments"

    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)
    cost_group_id = Column(Integer, ForeignKey("din276_cost_groups.id"), nullable=False)
    amount = Column(Numeric(14, 2), nullable=False, default=0)

    contract = relationship("Contract", back_populates="cost_assignments")
    cost_group = relationship("DIN276CostGroup")