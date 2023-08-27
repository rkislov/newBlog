from datetime import datetime
from sqlalchemy import Column, Text, String,Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from fastapi_utils.guid_type import GUID

from db.base_class import Base


class Blog(Base):
    id = Column(GUID, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String,nullable=False)
    content = Column(Text, nullable=True)
    author_id = Column(GUID, ForeignKey("user.id"))
    author = relationship("User", back_populates="blogs")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime,)
    is_active = Column(Boolean, default=False)