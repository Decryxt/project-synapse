from rich.console import Console

console = Console()


def exit_command():
    console.print("")
    console.print("Shutting down Synapse...")
    return False