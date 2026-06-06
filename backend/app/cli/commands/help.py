from rich.console import Console

console = Console()


def help_command(registry):
    def handler():
        console.print("")
        console.print("Available Commands")
        console.print("------------------")

        for command in registry.list_commands():
            console.print(command)

        console.print("")
        return True

    return handler