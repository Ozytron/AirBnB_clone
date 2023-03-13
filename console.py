#!/usr/bin/python3
"""HBNBCommand Module"""

import cmd
import re
from shlex import split

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""Global variable-list for the class names used."""
Classes = [
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review"
]


def parse(arg):
    """This analyzes the line feed into the command interpreter by dividing
    them into words
    Argument:
        args (type:str)- The string to be processed.
    Return:
        return a list of processed words/terms
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    square_bracket = re.search(r"\[(.*?)\]", arg)

    if curly_braces is None:
        if square_bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:square_bracket.span()[0]])
            ret = [i.strip(",") for i in lexer]
            ret.append(square_bracket.group())
            return ret
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        ret = [i.strip(",") for i in lexer]
        ret.append(curly_braces.group())
        return ret


def verify_args(args):
    """This checks if the args is valid
    Argument:
        args (type:str): the string containing the
                       arguments passed to a command.
        Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse(args)
    if len(arg_list) == 0:
        print("**class name missing**")
    if arg_list[0] not in Classes:
        print("**class doesn't exist**")
    else:
        return (arg_list)


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb)"

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def do_EOF(self, argv):
        """EOF signal to exit the program"""
        print("")
        return True

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, argv):
        """When executed, exits the console."""
        return True

    def do_create(self, argv):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        args = verify_args(argv)
        if args:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, argv):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = verify_args(argv)
        if len(args) != 2:
            print("**instance id missing**")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("**no instance found**")
            else:
                print(storage.all()[key])

    def do_destroy(self, argv):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = verify_args(argv)
        if len(args) == 1:
            print("**instance id missing**")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("**no instance found**")
            else:
                del (storage.all()[key])
                storage.save()

    def do_all(self, argv):
        """Prints all string representation of all instances based
        or not on the class name.
        """
        arg_list = split(argv)
        objects = storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in Classes:
                print("**class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_update(self, argv):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        args = verify_args(argv)
        if len(args) == 1:
            print("**instance id missing**")
        if len(args) == 2:
            print("**attribute name missing**")
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("**value missing**")
        if len(args) == 4 and type(eval(args[2])) != dict:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("**no instance found**")
            else:
                obj = storage.all()[key]
                attr, value = args[2], args[3]
                if attr in type(obj).__dict__:
                    value_type = type(obj.__class__.__dict__[attr])
                    setattr(obj, attr, value_type(value))
                else:
                    setattr(obj, attr, value)
        elif type(eval(args[2])) == dict:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[key]
            for attr, value in eval(args[2]).items():
                class_dict = obj.__class__.__dict__
                if (attr in class_dict.keys() and
                        type(class_dict[attr]) in {str, int, float}):
                    value_type = type(class_dict[attr])
                    obj.__dict__[attr] = value_type(value)
                else:
                    obj.__dict__[attr] = value
        storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        arg1 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg1[0] == type(obj).__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
