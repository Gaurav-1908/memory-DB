def show_help():
    print("""
Commands:
  put <key> <value>    - Insert or update key
  get <key>            - Retrieve value for key
  delete <key>         - Delete key
  exists <key>         - Check if key exists
  reset                - Clear the entire store
  all                  - Show all key-value pairs
  help                 - Show this help message
  exit                 - Exit CLI
""")
