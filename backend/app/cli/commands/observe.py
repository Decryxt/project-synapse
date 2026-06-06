from rich.console import Console

console = Console()


def observe_command(observation_engine):
    def handler():
        console.print("")
        content = input("Enter observation:\n> ")

        try:
            observation = observation_engine.record(content)
        except ValueError as error:
            console.print(f"Error: {error}")
            return True

        console.print(f"✓ Observation #{observation.id} stored.")
        console.print("")
        return True

    return handler