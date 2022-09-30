"""
    File name :                 game.py
    Author :                    Victorien Rodrigues
    Creation date :             16/09/2022
    Last modification date :    16/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Game engine
"""

#Importing librairies
from copy import copy
import this
import pygame
import pytmx
import pyscroll
from player import Player
from map import MapManager
from dialog import DialogBox

class Game:
    """ Instantiates a Game type object """
    def __init__(self):
        """ Game class constructor """
        #Create the game graphic
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Pokemon")
        
        #Generation of a Player type object (class player) by passing these generation on the map (we retrieve the coordinates from a layer of the tmx file)
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        self.liste = []
        # self.music_name = MapManager(self.screen, self.player).get_map().name
        # Liste des musiques
        self.towns = ["bonaugure", "littorella", "felicite", "charbourg", "floraville", "vestigion", "unionpolis", "bonville", "voilaroc", "verchamps", "joliberges", "celestia", "frimapic", "rivamar"]
        self.roads = ["route-201", "202", "203", "204", "205", "floraville-meadow", "fuego-forge", "wind-turbines"]
        self.lakes = ["lake-truth"]
        self.shores = ["shore-lake-truth"]
        self.areas = ["rest", "fight", "relaxation"]
        self.seas = ["220"]
        self.forests = ["vestigion-forest"]
        self.caves = ["entrance-charbourg", "charbourg-mine"]
        self.special = ["pokecenter", "old-castle", "vestigion-galaxy-building"]
        
    def handle_input(self):
        """ Animation of the sprite according to pressed keys """
        #Get keys that are pressed
        pressed = pygame.key.get_pressed()
        
        #If the player press key up
        if pressed[pygame.K_UP]:
            self.player.move_up()
            #Else if down
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            #Else if left
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            #Else if right
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            
    def update(self):
        """ Refresh the map constantly """
        self.map_manager.update()
        
    def new_map(self):
        """ Return the name of the new_map """
        this_map = self.map_manager.get_world_name()
        self.liste.append(this_map)
        
        # if len(self.liste) > 1:
        #     print(self.liste[0] + "--" + self.liste[1])
        if this_map != self.liste[0]:
            self.liste[1] = self.liste[0]
            self.liste[0] = this_map
            # print("this_map : " + this_map + " old_map : " + self.liste[1])
            # print(self.liste[0])
            return self.liste[0]
        
    def play_music(self):
        """ Music automation """
        # If the music name isn't in the good respository
        try:
            if self.liste[0] in self.towns:
                pygame.mixer.music.load(f'../assets/sounds/towns/{self.liste[0]}.mp3')
            elif self.liste[0] in self.roads:
                pygame.mixer.music.load(f'../assets/sounds/roads/{self.liste[0]}.mp3')
            elif self.liste[0] in self.lakes:
                pygame.mixer.music.load(f'../assets/sounds/lakes/{self.liste[0]}.mp3')
            elif self.liste[0] in self.shores:
                pygame.mixer.music.load(f'../assets/sounds/shores/{self.liste[0]}.mp3')
            elif self.liste[0] in self.areas:
                pygame.mixer.music.load(f'../assets/sounds/areas/{self.liste[0]}.mp3')
            elif self.liste[0] in self.seas:
                pygame.mixer.music.load(f'../assets/sounds/seas/{self.liste[0]}.mp3')
            elif self.liste[0] in self.forests:
                pygame.mixer.music.load(f'../assets/sounds/forests/{self.liste[0]}.mp3')
            elif self.liste[0] in self.caves:
                pygame.mixer.music.load(f'../assets/sounds/caves/{self.liste[0]}.mp3')
            elif self.liste[0] in self.special:
                pygame.mixer.music.load(f'../assets/sounds/special/{self.liste[0]}.mp3')
            pygame.mixer.music.play(-1, 0.0)
        except:
            print(self.liste[0])
            
        
    def run(self):
        """ Running the game """
        clock = pygame.time.Clock()
        
        #Game loop
        running = True
        pygame.mixer.music.load('../assets/sounds/towns/bonaugure.mp3') # self.current_map later
        pygame.mixer.music.play(-1, 0.0)
        #As long as we don't close the window, we refresh the page and redraw the slaps
        while running:
            if self.new_map() != None:
                self.play_music()
            #Save player coordinates to manage collisions with his feet
            self.player.save_location()
            #Before updating the elements, I take into account the keys that are pressed
            self.handle_input()
            self.update()
            #Centering the camera relative to the player's position on the map
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)
            clock.tick(60)
        pygame.quit()