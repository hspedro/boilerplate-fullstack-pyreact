import uuid
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID

from api.db.base_class import Base


class Account(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    balance = Column(Integer, nullable=False, default=0)
