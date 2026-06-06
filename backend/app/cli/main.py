from rich.console import Console

from app.cli.commands.exit import exit_command
from app.cli.commands.help import help_command
from app.cli.commands.observe import observe_command
from app.cli.commands.observations import observations_command
from app.cli.commands.status import status_command
from app.cli.registry import CommandRegistry
from app.engines.observation.engine import ObservationEngine
from app.engines.observation.json_storage import JsonObservationStore

console = Console()


def banner():
    console.print("=" * 50)
    console.print("           PROJECT SYNAPSE")
    console.print("      Judgment Engine Version 0.1")
    console.print("=" * 50)
    console.print("")
    console.print("Type 'help' for commands.")
    console.print("")


def build_registry():
    registry = CommandRegistry()

    observation_store = JsonObservationStore()
    observation_engine = ObservationEngine(observation_store)

    registry.register("help", help_command(registry))
    registry.register("status", status_command)
    registry.register("observe", observe_command(observation_engine))
    registry.register("observations", observations_command(observation_engine))
    registry.register("exit", exit_command)

    return registry


def main():
    banner()
    registry = build_registry()

    running = True

    while running:
        command = input("SYNAPSE://> ")
        running = registry.execute(command)


if __name__ == "__main__":
    main()