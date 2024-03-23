#!/usr/bin/env python3
"""Entry point to the program."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, line):
        """Create a new instance of a specified class."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = self.class_dict[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of instances."""
        args = line.split()
        if not args or args[0] not in self.class_dict:
            print([str(obj) for obj in storage.all().values()])
        else:
            print([str(obj) for obj in storage.all().values()
                   if type(obj).__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                obj = storage.all()[obj_key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")

    def do_count(self, line):
        """Retrieve the number of instances of a class."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        else:
            count = sum(1 for obj in storage.all().values() if type(obj).__name__ == args[0])
            print(count)

    def do_show_by_id(self, line):
        """Retrieve an instance based on its ID."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy_by_id(self, line):
        """Destroy an instance based on its ID."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update_by_id(self, line):
        """Update an instance based on its ID."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                obj = storage.all()[obj_key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")

    def do_update_by_dict(self, line):
        """Update an instance based on its ID with a dictionary."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** dictionary missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                obj = storage.all()[obj_key]
                if isinstance(args[2], dict):
                    for key, value in args[2].items():
                        setattr(obj, key, value)
                    obj.save()
                else:
                    print("** dictionary missing **")
            else:
                print("** no instance found **")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_EOF(self, line):
        """Exit the program."""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True


if __name__ == '__
