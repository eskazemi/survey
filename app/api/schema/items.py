from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List, ForwardRef

ListItemSchema = ForwardRef("List[ItemSchema]")


class TypeEnum(str, Enum):
    stepper = "stepper"
    group = "group"
    checkbox = "checkbox"
    switch = "switch"
    text = "text"
    rate = "rate"
    mobile = "mobile"


class ItemSchema(BaseModel):
    type: TypeEnum
    title: str
    body: str
    position: int
    required: Optional[bool]
    score: int = Field(ge=0, le=5)
    children: Optional[ListItemSchema]


ItemSchema.update_forward_refs()
