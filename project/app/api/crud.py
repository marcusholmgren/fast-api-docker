import logging
from typing import Union

from fastapi import HTTPException
from tortoise.exceptions import IntegrityError

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

log = logging.getLogger(__name__)


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy dummy")
    try:
        await summary.save()
    except IntegrityError as e:
        log.error(f"IntegrityError: {e}")
        raise HTTPException(
            status_code=409, detail=f"URL '{payload.url}' already exists"
        )
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


def get_all():
    return TextSummary.all().values()
