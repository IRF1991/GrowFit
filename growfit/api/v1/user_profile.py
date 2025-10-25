from fastapi import APIRouter
from growfit.models.user_profile import UserProfile

router = APIRouter()

@router.post("/imc")
def calcular_imc(user: UserProfile):
    imc = user.peso / (user.altura ** 2)
    return {"imc": imc}
