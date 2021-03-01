from pipebot.lib.bot import bot


class Command:
    def __init__(self, pipe_in = 0, pipe_out = 0):
        self.pipe_in = pipe_in
        self.pipe_out = pipe_out

    def func(args):
        return NotImplemented

    def __call__(self, *args):
        self.func(*args)


class AddCommand(Command):
    def __init__(self):
        self.pipe_in = 2
        self.pipe_out = 1

    def func(args):
        sumnum = int(args[0]) + int(args[1])
        print(sumnum)
        return (sumnum)


class ReverseCommand(Command):
    def __init__(self):
        self.pipe_in = 1
        self.pipe_out = 1

    def func(args):
        full = " ".join(args)
        rev = str(full)[::-1]
        print(rev)
        return (rev)


def register():
    bot.register("add", AddCommand)
    bot.register("reverse", ReverseCommand)
