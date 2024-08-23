from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    url: str

    class Config:
        json_schema_extra = {"example": {"url": "https://example.com"}}


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int

    class Config:
        json_schema_extra = {"example": {"id": 1, "url": "https://example.com"}}
