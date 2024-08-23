from tortoise import fields, models
from pydantic import BaseModel


class TextSummary(models.Model):
    url = fields.CharField(max_length=200, unique=True)
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class SummaryPayloadSchema(BaseModel):
    url: str

    class Config:
        schema_extra = {
            "example": {
                "url": "https://example.com"
            }
        }
