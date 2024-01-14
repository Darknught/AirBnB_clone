#!/usr/bin/python3
"""Module that defines FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
        "BaseModel": BaseModel, "User": User,
        "Place": Place, "State": State,
        "City": City, "Amenity": Amenity,
        "Review": Review
        }


class FileStorage:
    """class that uses private class attributes below"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        seria_objs = {
                key: value.to_dict() for key, value in self.__objects.items()
                }
        with open(self.__file_path, 'w') as f:
            json.dump(seria_objs, f)

    def reload_helper(self, data, key):
        """ reload helper """
        return classes[data[key]["__class__"]](**data[key])

    def reload(self):
        """Deserializes the JSON file to __objects if exists otherwise no"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    data = json.load(f)

                    for key in data:
                        self.__objects[key] = self.reload_helper(data, key)
            except Exception:
                return

    def get_object_by_id(self, class_name, instance_id):
        """
        Retrieve an object by class name and instance ID from the storage.
        Args:
            class_name (str): The name of the class.
            instance_id (str): The instance ID.
        Returns:
            object or None: The object if found, or None if not found.
        """
        all_objects = self.all()
        key = "{}.{}".format(class_name, instance_id)
        return all_objects.get(key)

    def delete(self, obj=None):
        """deletes object if present"""
        if obj is not None:
            del self.__objects[obj.__class__.__name__ + '.' + obj.id]
            self.save()
