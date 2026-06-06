class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, name: str, handler):
        self.commands[name] = handler

    def execute(self, name: str) -> bool:
        command = name.strip().lower()

        if command == "":
            return True

        handler = self.commands.get(command)

        if handler is None:
            print(f"Unknown command: {command}")
            return True

        return handler()

    def list_commands(self):
        return sorted(self.commands.keys())