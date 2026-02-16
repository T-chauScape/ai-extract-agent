from pydantic import BaseModel
from typing import Any

class ExtractRequest(BaseModel):
    texto_completo: str

class ExtractResponse(BaseModel):
    message: str
    result: Any