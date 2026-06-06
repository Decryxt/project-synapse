from rich.console import Console

from app.cli.registry import CommandRegistry
from app.cli.commands.exit import exit_command
from app.cli.commands.help import help_command
from app.cli.commands.status import status_command

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

    registry.register("help", help_command(registry))
    registry.register("status", status_command)
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