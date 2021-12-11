from pydantic import BaseModel
from typing import Optional, Any


class PollSchema(BaseModel):
    """
    The data structure determines the input from the user
    """
    container_id: str
    container_type: int
    mobile: str
    unit: Optional[str] = None
    data: Any
