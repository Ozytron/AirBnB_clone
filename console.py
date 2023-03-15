#!/usr/bin/python3
"""HBNBCommand Module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def do_quit(self, argv):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, argv):
        """EOF command to exit the program\n"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
