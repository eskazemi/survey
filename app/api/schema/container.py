from pydantic import BaseModel
from enum import IntEnum
from typing import Optional, List
from datetime import datetime
from .items import ItemSchema


class StatusEnum(IntEnum):
    test = 1
    two = 2


class TypeEnum(IntEnum):
    customer = 1
    staff = 2


class ContainerSchema(BaseModel):
    title: str
    body: str
    slug: str
    status: Optional[StatusEnum]
    is_active: bool = True
    container_type: TypeEnum
    items: List[ItemSchema]
    min_score: int
    time_slice_pattern: Optional[str]
    started_at: Optional[datetime]
    expired_at: Optional[datetime]


class DeActivePoll(BaseModel):
    is_active: bool





