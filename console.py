#!/usr/bin/python3

"""Import different modules and classes."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

"""The HBNBCommandc class."""


class HBNBCommand(cmd.Cmd):
    """The HBNBCommandc class."""

    prompt = "(hbnb) "

    def do_quit(self, args):
        r"""Quit command to exit the program.\n"""
        return (True)

    def do_EOF(self, args):
        r"""EOF command to exit the program.\n"""
        return (True)

    def do_create(self, args):
        """Create an instance of BaseModel, saves and prints the id.\n"""
        # daddy = {"BasemModel": BaseModel}
        if args:
            if args == "BaseModel":
                baseModelInstance = BaseModel()
                print(baseModelInstance.id)
                return ()
            # here = ["User", "State", "City", "Amenity", "Place", "Review"]
            elif args == "User":
                userInstance = User()
                print(userInstance.id)
            elif args == "State":
                stateInstance = State()
                print(stateInstance.id)
            elif args == "City":
                cityInstance = City()
                print(cityInstance.id)
            elif args == "Amenity":
                amenityInstance = Amenity()
                print(amenityInstance.id)
            elif args == "Place":
                placeInstance = Place()
                print(placeInstance.id)
            elif args == "Review":
                reviewInstance = User()
                print(reviewInstance.id)
            else:
                print("** class doesn't exit **")
                return ()
        else:
            print(" ** class name missing **")
            return ()

    def do_show(self, args):
        """
        Print the string representation of an instance based on the
        class name and id.\n
        """
        splitItUp = args.split(" ")
        here = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
            ]
        if not splitItUp:
            print("** class name missing **")
        elif splitItUp[0] not in here:
            print("** class doesn't exist **")
        elif len(splitItUp) < 2:
            print("** instance id missing **")
        else:
            everyInstance = storage.all()
            whatIneed = splitItUp[0] + "." + splitItUp[1]
            if whatIneed in everyInstance:
                print(everyInstance[whatIneed])
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Print the string representation of all instances based
        or not on the class name.\n
        """
        splitItUp = args.split(" ")
        here = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
            ]
        if splitItUp[0] is None:
            everyInstance = storage.all()
            for instance in everyInstance.values():
                print(instance)
        elif splitItUp[0] not in here:
            print("** class doesn't exist **")
        elif splitItUp[0] in here:
            instanceWeNeed = splitItUp[0]
            everyInstance = storage.all()
            classInstances = [
                instance for instance in everyInstance.values()
                if instance.__class__.__name__ == instanceWeNeed
            ]
            for instance in classInstances:
                print("[\"{}\"]".format(instance))
        else:
            everyInstance = storage.all()
            for instance in everyInstance.values():
                print(instance)

    def do_destroy(self, args):
        """Delete an instance based on the class name and id.\n"""
        splitItUp = args.split(" ")
        here = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
            ]
        if not splitItUp[0]:
            print("** class name missing **")
        elif splitItUp[0] not in here:
            print("** class doesn't exist **")
        elif len(splitItUp) < 2:
            print("** instance id missing **")
        else:
            everyInstance = storage.all()
            whatIneed = splitItUp[0] + "." + splitItUp[1]
            if whatIneed in everyInstance:
                del (everyInstance[whatIneed])
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, args):
        """
        Update an instance based on the class name and id by adding or
        updatung attribute.
        """
        split_args = args.split(" ")
        here = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
            ]

        if not split_args:
            print("** class name missing **")
            return
        elif split_args[0] not in here:
            print("** class doesn't exist **")
            return
        elif len(split_args) < 2:
            print("** instance id missing **")
            return

        className = split_args[0]
        instanceID = split_args[1]
        key = className + "." + instanceID

        everyInstance = storage.all()

        if key not in everyInstance:
            print("** no instance found **")
            return

        instance = everyInstance[key]

        if len(split_args) < 3:
            print("** attribute name missing **")
            return
        elif len(split_args) < 4:
            print("** value missing **")
            return

        attributeName = split_args[2]
        attributeValue = split_args[3].replace('"', '')

        if attributeName in ["id", "created_at", "updated_at"]:
            # These attributes can not be updated
            return

        setattr(instance, attributeName, attributeValue)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
