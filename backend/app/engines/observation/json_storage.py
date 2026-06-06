import json
from datetime import datetime
from pathlib import Path

from app.engines.observation.models import Observation


class JsonObservationStore:
    def __init__(self, file_path: str = "data/observations.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def add(
        self,
        content: str,
        source: str,
        category: str,
        importance: int,
    ) -> Observation:
        observations = self.list_all()
        next_id = self._next_id(observations)

        observation = Observation(
            id=next_id,
            content=content,
            source=source,
            category=category,
            importance=importance,
            created_at=datetime.now(),
        )

        observations.append(observation)
        self._save(observations)

        return observation

    def list_all(self) -> list[Observation]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            Observation(
                id=item["id"],
                content=item["content"],
                source=item.get("source", "unknown"),
                category=item.get("category", "uncategorized"),
                importance=item.get("importance", 50),
                created_at=datetime.fromisoformat(item["created_at"]),
            )
            for item in data
        ]

    def _save(self, observations: list[Observation]) -> None:
        data = [
            {
                "id": observation.id,
                "content": observation.content,
                "source": observation.source,
                "category": observation.category,
                "importance": observation.importance,
                "created_at": observation.created_at.isoformat(),
            }
            for observation in observations
        ]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def _next_id(self, observations: list[Observation]) -> int:
        if not observations:
            return 1

        return max(observation.id for observation in observations) + 1