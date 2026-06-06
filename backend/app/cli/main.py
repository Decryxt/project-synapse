from rich.console import Console

console = Console()


def banner():
    console.print("=" * 50)
    console.print("           PROJECT SYNAPSE")
    console.print("      Judgment Engine Version 0.1")
    console.print("=" * 50)
    console.print("")
    console.print("Type 'help' for commands.")
    console.print("")


def main():
    banner()

    while True:
        command = input("SYNAPSE://> ").strip().lower()

        if command == "help":
            console.print("")
            console.print("Available Commands")
            console.print("------------------")
            console.print("help")
            console.print("status")
            console.print("exit")
            console.print("")

        elif command == "status":
            console.print("")
            console.print("SYSTEM STATUS")
            console.print("------------------")
            console.print("Version: 0.1")
            console.print("Status: ONLINE")
            console.print("")

        elif command == "exit":
            console.print("")
            console.print("Shutting down Synapse...")
            break

        elif command == "":
            continue

        else:
            console.print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()