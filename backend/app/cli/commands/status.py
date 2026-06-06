from rich.console import Console

console = Console()


def status_command():
    console.print("")
    console.print("SYSTEM STATUS")
    console.print("------------------")
    console.print("Version: 0.1")
    console.print("Status: ONLINE")
    console.print("")
    return True