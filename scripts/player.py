"""
    File name :                 player.py
    Author :                    Victorien Rodrigues
    Creation date :             16/09/2022
    Last modification date :    16/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Manage the player
"""
#Importing libraries
from entity import Entity

class Player(Entity):
    """Player class, inherits from Entity"""
    def __init__(self):
        """Constructor of the Player class, inherits from the Entity class"""
        super().__init__("player", 0, 0)