from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.api.deps import get_current_active_user
from app.schemas import User

router = APIRouter()


@router.get('/')
async def alguma_coisa(db: Session = Depends(deps.get_db),
                       current_user: User = Depends(get_current_active_user)
                       ):
    users = crud.user.get_multi(db, skip=0, limit=100)
    return {"message": users, "text": "Lorem ipsun aquela coisa chata"}

class Teste:
    def teste1(self):
        pass

class Teste2(Teste):
    def teste1(self):
        super().teste1()