from rich.console import Console

console = Console()


def observations_command(observation_engine):
    def handler():
        observations = observation_engine.list_observations()

        console.print("")

        if not observations:
            console.print("No observations recorded.")
            console.print("")
            return True

        console.print("OBSERVATIONS")
        console.print("------------------")

        for observation in observations:
            console.print(f"#{observation.id}")
            console.print(f"Content: {observation.content}")
            console.print(f"Source: {observation.source}")
            console.print(f"Category: {observation.category}")
            console.print(f"Importance: {observation.importance}")
            console.print(f"Created: {observation.created_at}")
            console.print("------------------")

        console.print("")
        return True

    return handler