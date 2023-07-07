#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class defines the console.
    """
    classes = ["Amenity", "BaseModel", "City", "Place", "Review", "State",
               "User"]
    prompt = '(hbnb) '

    def emptyline(self):
        """
        Called when an empty line is entered in the command interpreter.
        """
        pass

    def do_quit(self, arg):
        """
        Quit the command interpreter.
        """
        quit()

    def do_EOF(self, arg):
        """
        Quit the command interpreter.
        """
        quit()

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, save it in a JSON file and print
        its ID
        """
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                all_objects = storage.all()
                print(all_objects[args[0] + '.' + args[1]])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                key = storage.all()
                del (key[args[0] + '.' + args[1]])
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """
        all_objects = storage.all()
        my_list = []
        if arg == "":
            for obj_id in all_objects.keys():
                obj = all_objects[obj_id]
                print(obj)
        else:
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for obj_id, obj in all_objects.items():
                    if obj.__class__.__name__ == arg:
                        my_list.append(str(obj))
                        print(my_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute.
        """
        args = arg.split()
        all_objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            obj = args[0] + "." + args[1]
            all_objects[obj].__dict__[args[2]] = eval(args[3])
            storage.save()
        except Exception:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
