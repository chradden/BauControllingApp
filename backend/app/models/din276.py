from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class DIN276CostGroup(Base):
    """DIN 276 Kostengruppenstruktur (z.B. 300 - Bauwerk - Baukonstruktionen)"""
    __tablename__ = "din276_cost_groups"

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    parent_id = Column(Integer, ForeignKey("din276_cost_groups.id"), nullable=True)
    level = Column(Integer, nullable=False)  # 1=100er, 2=110er, 3=111er
    
    # Self-referential relationship for hierarchical structure
    children = relationship("DIN276CostGroup", 
                          backref=relationship("DIN276CostGroup", remote_side=[id]),
                          lazy="joined")
    
    # Relationships to other models
    budget_lines = relationship("BudgetLine", back_populates="cost_group")