"""
    File name :                 npc.py
    Author :                    Victorien Rodrigues
    Creation date :             16/09/2022
    Last modification date :    16/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Manage NPCs
"""
#Importing libraries
import pygame
from entity import Entity

class NPC(Entity):
    """NPC class, inherits from Entity"""
    def __init__(self, name, nb_points, dialogs):
        """Constructor of the NPC class, inherits from the Entity class"""
        super().__init__(name, 0, 0)
        self.nb_points = nb_points
        self.dialogs = dialogs
        self.points = []
        self.name = name
        self.speed = 0.5
        self.current_point = 0

    def move(self):
        """Management of automatic movement of NPCs"""
        current_point = self.current_point
        target_point = self.current_point + 1

        #If there is no more predefined path, we start again at the first path
        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        #3 is the margin of error in px for displacement
        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 1.01:
            self.move_down()
        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 1.01:
            self.move_up()
        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 1.01:
            self.move_left()
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 1.01:
            self.move_right()

        #If the NPC has a collision with the player, the NPC's path is temporarily stopped
        if self.rect.colliderect(target_rect):
            self.current_point = target_point

    def teleport_spawn(self):
        """Place the nNPC at the location indicated on the map"""
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        """Moves an NPC along a predefined path : {NPCname}_path{X}"""
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)