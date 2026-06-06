from dataclasses import dataclass
from datetime import datetime


@dataclass
class Observation:
    id: int
    content: str
    created_at: datetime