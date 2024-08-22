from tortoise import fields, models


class TextSummary(models.Model):
    url = fields.CharField(max_length=200, unique=True)
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url
