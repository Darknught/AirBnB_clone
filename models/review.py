#!/usr/bin/python3
"""Module that defines class Review"""


from base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialization method for Review"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        """String representation for the Review object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
