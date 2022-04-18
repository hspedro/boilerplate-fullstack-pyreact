from .base import CRUDBase
from api.models.account import Account
from api.schemas.account import AccountCreate, AccountUpdate

account = CRUDBase[Account, AccountCreate, AccountUpdate](Account)
