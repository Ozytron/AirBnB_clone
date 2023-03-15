#!/usr/bin/python3
"""HBNBCommand Module"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def do_quit(self, argv):
        """When executed, exits the console."""
        return True

    def do_EOF(self, argv):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
