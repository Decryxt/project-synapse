from app.engines.observation.json_storage import JsonObservationStore


class ObservationEngine:
    def __init__(self, store: JsonObservationStore):
        self.store = store

    def record(
        self,
        content: str,
        source: str,
        category: str,
        importance: int,
    ):
        clean_content = content.strip()
        clean_source = source.strip() or "unknown"
        clean_category = category.strip() or "uncategorized"

        if not clean_content:
            raise ValueError("Observation content cannot be empty.")

        if importance < 1 or importance > 100:
            raise ValueError("Importance must be between 1 and 100.")

        return self.store.add(
            content=clean_content,
            source=clean_source,
            category=clean_category,
            importance=importance,
        )

    def list_observations(self):
        return self.store.list_all()