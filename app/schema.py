from pydantic import BaseModel
from typing import List


class CorepField(BaseModel):
    field_code: str
    value: str
    currency: str
    rule_reference: str
    explanation: str
    confidence: str


class CorepResponse(BaseModel):
    template: str
    fields: List[CorepField]
    missing_data: List[str]
    validation_errors: List[str] = []
