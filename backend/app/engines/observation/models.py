from dataclasses import dataclass
from datetime import datetime


@dataclass
class Observation:
    id: int
    content: str
    source: str
    category: str
    importance: int
    created_at: datetime