from app.engines.observation.storage import InMemoryObservationStore


class ObservationEngine:
    def __init__(self, store: InMemoryObservationStore):
        self.store = store

    def record(self, content: str):
        clean_content = content.strip()

        if not clean_content:
            raise ValueError("Observation content cannot be empty.")

        return self.store.add(clean_content)

    def list_observations(self):
        return self.store.list_all()