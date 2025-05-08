from fastapi import APIRouter, Body, status

from workout.contrib.dependencies import DatabaseDependency
from workout.atleta.schemas import AtletaIn

router = APIRouter()

@router.post("/", summary="Criar novo atleta",
             status_code=status.HTTP_201_CREATED)
async def post(db_session: DatabaseDependency,
               atleta_in: AtletaIn = Body(...)):
    pass
