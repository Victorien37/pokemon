"""
    File name :                 main.py
    Author :                    Victorien Rodrigues
    Creation date :             16/09/2022
    Last modification date :    16/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               This file start the game
"""
#Importing libraries
import pygame
from game import Game

#Game generation
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_icon(pygame.image.load("../assets/images/icon.png"))
    game = Game()
    game.run()