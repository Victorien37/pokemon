"""
    File name :                 entity.py
    Author :                    Victorien Rodrigues
    Creation date :             16/09/2022
    Last modification date :    16/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Entity movement management
"""
#Importing libraries
import pygame

from animation import AnimateSprite

class Entity(AnimateSprite):
    """Instance un objet de type Entity"""
    def __init__(self, name, x, y):
        """Entity Constructor of the class"""
        #Inheritance from the Game class which allows to include the Player object in the Game object (because the player is part of the game)
        super().__init__(name)
        #Selection of a part of the image to make the sprite
        self.image = self.get_image(0, 0)
        #We raise the background color
        self.image.set_colorkey([0, 0, 0])
        #Use of the get_image function (create if below) which allows to give the size in px of my character
        self.rect = self.image.get_rect()
        #Player's position on the map when spawned
        self.position = [x, y]
        #Management of collisions at the feet of the character
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.odl_position = self.position.copy()

    def save_location(self):
        """Saving player foot coordinates"""
        self.odl_position = self.position.copy()

    

    ###METHODS THAT WILL ALLOW TO CHANGE THE PLAYER'S POSITION DEPENDING ON THE KEYS PRESSED ON THE KEYBOARD###
    def move_right(self):
        """Right arrow key"""
        self.change_animation("RIGHT")
        self.position[0] += self.speed

    def move_left(self):
        """Left arrow key"""
        self.change_animation("LEFT")
        self.position[0] -= self.speed

    def move_up(self):
        """Up arrow key"""
        self.change_animation("UP")
        self.position[1] -= self.speed

    def move_down(self):
        """Down arrow key"""
        self.change_animation("DOWN")
        self.position[1] += self.speed

    def update(self):
        """Update function that takes the position of our character from the constructor"""
        self.rect.topleft = self.position
        #Position of the feet on the player for collision management
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        """Changed coordinates of the player at the old position if he is beyond the limit set by collision"""
        self.position = self.odl_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom