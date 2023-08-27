from db.base_class import Base
from sqlalchemy import Column, Boolean, String
import uuid
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID


class User(Base):
    id = Column(GUID, primary_key=True)
    email = Column(String,nullable=False, unique=True,index=True)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    blogs = relationship("Blog", back_populates="authors")