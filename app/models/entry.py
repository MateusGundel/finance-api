from sqlalchemy import Boolean, Column, Integer, String, DateTime,Numeric

from app.db.base_class import Base

class Entry(Base):
    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(DateTime)
    user = Column(Integer, nullable=False)
    title = Column(String)
    description = Column(String)
    value = Column(Numeric(10, 2))
    operation_date = Column(DateTime)
    operation_type = Column(Integer)
    planned_entry = Column(Integer)