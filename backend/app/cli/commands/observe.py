from rich.console import Console

console = Console()


def observe_command(observation_engine):
    def handler():
        console.print("")

        content = input("Enter observation:\n> ")
        source = input("Source:\n> ")
        category = input("Category:\n> ")
        importance_raw = input("Importance (1-100):\n> ")

        try:
            importance = int(importance_raw)
            observation = observation_engine.record(
                content=content,
                source=source,
                category=category,
                importance=importance,
            )
        except ValueError as error:
            console.print(f"Error: {error}")
            console.print("")
            return True

        console.print(f"✓ Observation #{observation.id} stored.")
        console.print("")
        return True

    return handler