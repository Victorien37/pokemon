"""
    File name :                 animation.py
    Author :                    Victorien Rodrigues
    Creation date :             16/09/2022
    Last modification date :    16/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Animation of entities
"""
#Importing libraries
import pygame

class AnimateSprite(pygame.sprite.Sprite):
    """AnimateSprite class, manages entity animations"""
    def __init__(self, name):
        super().__init__()
        #Loading the player's sprite based on (f) its name when it is instantiated
        self.sprite_sheet = pygame.image.load(f'../sprites/{name}.png')
        #Index for sprite animation
        self.animation_index = 0
        #Clamping the refresh of sprite animations
        self.clock = 0
        #Dictionary that takes into account a part of an image for the sprite
        self.images = {
            'DOWN': self.get_images(0),
            'LEFT': self.get_images(32),
            'RIGHT': self.get_images(64),
            'UP': self.get_images(96)
        }
        #player movement speed
        self.speed = 3

    def get_images(self, y):
        """Handles sprite image changes"""
        images = []
        for i in range(0, 3):
            #32 because a sprite image is 32px * 32px
            x = i * 32
            image = self.get_image(x, y)
            images.append(image)
        return images

    def get_image(self, x, y):
        """Allows us to display the sprite of our character by giving its size in px and giving it starting coordinates"""
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    def change_animation(self, name):
        """Change the sprite of the player according to his direction (keys pressed) and we add a transparent background"""
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey([0, 0, 0])
        self.clock += self.speed * 8

        #Animation clamping
        if self.clock >= 100:
            #Go to the next image
            self.animation_index += 1
            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.clock = 0