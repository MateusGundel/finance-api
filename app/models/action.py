from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func

from app.db.base_class import Base


class Action(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_hash = Column(String)
    value = Column(String)
    type = Column(String)
    data = Column(DateTime, server_default=func.now())
