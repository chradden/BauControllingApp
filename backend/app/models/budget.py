from decimal import Decimal
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from . import Base


class BudgetType(str, PyEnum):
    INITIAL = "initial"      # Erste Baseline
    FORECAST = "forecast"    # Prognose
    CURRENT = "current"      # Aktueller Stand
    COMMITTED = "committed"  # Beauftragt


class BudgetLine(Base):
    """Budget-Position je Kostengruppe mit Type (Initial/Forecast/Current)"""
    __tablename__ = "budget_lines"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    cost_group_id = Column(Integer, ForeignKey("din276_cost_groups.id"), nullable=False)
    type = Column(Enum(BudgetType), nullable=False, default=BudgetType.INITIAL)
    amount = Column(Numeric(14, 2), nullable=False, default=0)
    description = Column(String(500), nullable=True)
    version = Column(Integer, nullable=False, default=1)

    # Relationships
    project = relationship("Project", back_populates="budget_lines")
    cost_group = relationship("DIN276CostGroup", back_populates="budget_lines")
    
    def __str__(self):
        return f"{self.cost_group.code} - {self.type}: {self.amount}"