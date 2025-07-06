from src.config import config
from src.APIClient import APIClient
import src.commands as commands
from src.utils import show_help

def cli():
    url, timeout, password = config()
    client = APIClient(url, timeout)
    print("🔑 Welcome to GDB CLI!")
    print(f"📡 Connected to: {url} (timeout: {timeout}s)")
    show_help()

    while True:
        try:
            user_input = input(">>> ").strip().split()
            if not user_input:
                continue

            cmd = user_input[0].lower()
            args = user_input[1:]

            if cmd == "put" and len(args) >= 2:
                key = args[0]
                value = ' '.join(args[1:])
                commands.put(client, key, value, password)
            elif cmd == "get" and len(args) == 1:
                commands.get(client, *args, password)
            elif cmd == "delete" and len(args) == 1:
                commands.delete(client, *args, password)
            elif cmd == "exists" and len(args) == 1:
                commands.exists(client, *args, password)
            elif cmd == "reset":
                commands.reset(client, password)
            elif cmd == "all":
                commands.get_all(client, password)
            elif cmd == "backup":
                commands.backup(client, password)
            elif cmd == "help":
                show_help()
            elif cmd == "exit":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid command. Type 'help' for instructions.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == '__main__':
    cli()
