from typing import Callable


class Bot:
    def __init__(self, prefix):
        self.prefix = prefix
        self.commands = {}

    def run(self):
        while True:
            command = input("> ")
            if command.startswith(self.prefix):
                command = command[len(self.prefix):]
                self.process_cmd(command)

    def process_cmd(self, command: str):
        args = command.split(" ")
        command_name = args[0]
        if command_name in self.commands:
            del args[0]
            self.commands[command_name].__call__(self.commands[command_name], args)

    def register(self, name, function):
        if isinstance(function, Callable):
            self.commands[name] = function
        else:
            raise ValueError(f"Function for command {name} wasn't callable!")


bot = Bot("!")
