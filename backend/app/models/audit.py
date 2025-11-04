from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from . import Base


class AuditLog(Base):
    """Audit-Trail für alle relevanten Änderungen (wer/wann/was)"""
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    entity_type = Column(String(50), nullable=False)  # z.B. "project", "invoice"
    entity_id = Column(Integer, nullable=False)
    action = Column(String(50), nullable=False)  # z.B. "create", "update", "delete"
    changes = Column(JSON, nullable=True)  # {field: {old: x, new: y}}
    
    # Relationships
    user = relationship("User", lazy="joined")