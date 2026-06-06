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
            console.print(f"#{observation.id} {observation.content}")

        console.print("")
        return True

    return handler