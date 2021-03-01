
import re
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
        if "||" in command:
            self.process_piped_cmds(command)
        args = command.split(" ")
        command_name = args[0]
        if command_name in self.commands:
            del args[0]
            self.commands[command_name].__call__(self.commands[command_name], args)

    def process_piped_cmds(self, command_string: str):
        cmds = re.split(r"\s*\|\|\s*")
        for command in cmds:
            if self.commands.get(command.split(" ")[0], None) is None:
                raise ValueError("That's not a command!")
        last_cmd = None
        for n, command in enumerate(cmds):
            cmd = self.commands.get(command.split(" ")[0])
            if last_cmd is not None and last_cmd.pipe_out != cmd.pipe_in:
                return ValueError("Mismatched pipe count!")

        last_args = None
        for command in cmds:
            cmd = self.commands.get(command.split(" ")[0])
            if last_args is None:
                cmd.__call__(cmd)
            last_args = cmd.__call__(cmd, last_args)

    def register(self, name, function):
        if isinstance(function, Callable):
            self.commands[name] = function
        else:
            raise ValueError(f"Function for command {name} wasn't callable!")


bot = Bot("!")
