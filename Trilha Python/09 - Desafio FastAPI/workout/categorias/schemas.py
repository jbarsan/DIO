from typing import Annotated
from pydantic import Field

from workout.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", examples="Scale", max_length=50)]
