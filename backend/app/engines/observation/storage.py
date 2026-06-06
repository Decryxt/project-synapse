from app.engines.observation.models import Observation


class InMemoryObservationStore:
    def __init__(self):
        self._observations: list[Observation] = []
        self._next_id = 1

    def add(self, content: str) -> Observation:
        observation = Observation(
            id=self._next_id,
            content=content,
            created_at=__import__("datetime").datetime.now(),
        )

        self._observations.append(observation)
        self._next_id += 1

        return observation

    def list_all(self) -> list[Observation]:
        return self._observations.copy()