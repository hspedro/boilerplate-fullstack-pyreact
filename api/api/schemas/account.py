from typing import Optional
from uuid import UUID
from pydantic import BaseModel


# Shared properties
class AccountBase(BaseModel):
    pass


# Properties to receive via API on creation
class AccountCreate(AccountBase):
    pass


# Properties to receive via API on update
class AccountUpdate(AccountBase):
    balance: int


class AccountInDBBase(AccountBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Account(AccountInDBBase):
    pass
