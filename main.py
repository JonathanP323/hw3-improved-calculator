import importlib
import os

def load_plugins():
    plugins = {}
    plugins_dir = "plugins"
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module = importlib.import_module(f"{plugins_dir}.{module_name}")
            plugins[module.operation_name()] = module
    return plugins

def repl():
    print("Welcome to the REPL Calculator!")
    print("Type 'menu' to see available commands or 'exit' to quit.")

    plugins = load_plugins()

    while True:
        user_input = input("Enter command (e.g., add 5 3): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if user_input.lower() == "menu":
            print("Available commands:")
            for command in plugins:
                print(command)
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Use format: <command> <a> <b>")
            continue

        command, a, b = parts
        if command not in plugins:
            print(f"Unknown operation: {command}")
            continue

        try:
            a = float(a)
            b = float(b)
            result = plugins[command].run(a, b)
            print(f"The result of {a} {command} {b} is: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

