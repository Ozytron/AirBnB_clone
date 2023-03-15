#!/usr/bin/python3
"""HBNBCommand Module"""

import cmd
import re
from shlex import split

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "

    """Global variable-list for the class names used."""
    __Classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
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
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, argv):
        """EOF command to exit the program\n"""
        return True

    def do_create(self, argv):
        """Usage: create <class>
        Creates a new instance of class, prints the id
        and saves it (to the JSON file)
        """
        arg_list = parse(argv)
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        elif arg_list[0] not in HBNBCommand.__Classes:
            print("** class doesn't exist **")
            return False
        else:
            print(eval(arg_list[0])().id)
            models.storage.save()

    def do_show(self, argv):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg_list = parse(argv)
        objs_dict = models.storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        elif arg_list[0] not in HBNBCommand.__Classes:
            print("** class doesn't exist **")
            return False
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in objs_dict:
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, argv):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        (save the change into the JSON file)
        """
        arg_list = parse(argv)
        objs_dict = models.storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        elif arg_list[0] not in HBNBCommand.__Classes:
            print("** class doesn't exist **")
            return False
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in objs_dict.keys():
            print("** no instance found **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            del (objs_dict[key])
            models.storage.save()

    def do_all(self, argv):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        arg_list = split(argv)
        objects = models.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in HBNBCommand.__Classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_update(self, argv):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        (save the change into the JSON file)
        """
        arg_list = parse(argv)
        objs_dict = models.storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__Classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in objs_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_list) == 4:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            obj = objs_dict[key]
            attr, value = arg_list[2], arg_list[3]
            if attr in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[attr])
                obj.__dict__[attr] = value_type(value)
            else:
                obj.__dict__[attr] = value
        elif type(eval(arg_list[2])) == dict:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            obj = objs_dict[key]
            for attr, value in eval(arg_list[2]).items():
                class_dict = obj.__class__.__dict__
                if (attr in class_dict.keys() and
                        type(class_dict[attr]) in {str, int, float}):
                    value_type = type(class_dict[attr])
                    obj.__dict__[attr] = value_type(value)
                else:
                    obj.__dict__[attr] = value
        models.storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        arg1 = parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if arg1[0] == type(obj).__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
