"""
    File name :                 map.py
    Author :                    Victorien Rodrigues
    Creation date :             16/09/2022
    Last modification date :    16/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Map display management
"""
#Importing libraries
from dataclasses import dataclass
import pygame
import pytmx
import pyscroll
from npc import NPC

@dataclass
class Portal:
    """Portal data class"""
    # Portal("current world name", "portal name", "target world name", "spawn name")
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str

@dataclass
class Map:
    """Map data class, load map data"""
    name: str
    walls: list#[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list#[Portal]
    npcs: list#[NPC]
    
class MapManager:
    """MapManager class, Instantiates an object of type MapManager, Sets the point of entering the world"""
    def __init__(self, screen, player):
        """MapManager class constructor"""
        self.maps = dict() # "house" -> Map("house", walls, group)
        self.screen = screen
        self.player  = player
        self.current_map = "bonaugure" #current_map will be dynamic later when save is enable
        
        ### REGISTER MAP DOIT ETRE OBLIGATOIREMENT ETRE DECLARER DANS LA CLASSE MAP MANAGER ET NON DANS UN AUTRE FICHIER ###
        self.register_map("bonaugure", portals=[
            # Portal(from_world="bonaugure", origin_point="enter_my_home", target_world="my_home", teleport_point="spawn_player"),
            # Portal(from_world="bonaugure", origin_point="enter_rival_home", target_world="rival_home", teleport_point="spawn"),
            # Portal("bonaugure", "enter_route-201", "route-201", "spawn_route-201")
        ], npcs=[
            NPC("electro", nb_points=2, dialogs=["Tout le monde part à l'aventure","et devient peu à peu adulte..."])
        ])
        
        self.teleport_player("player")
        self.teleport_npcs()
    
    def check_npc_collisions(self, dialog_box):
        """Permanent check if an NPC has a collision with the player"""
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC:
                dialog_box.execute(sprite.dialogs)

    def check_collision(self):
        """Check permanently if we arrive on a Portal object, if so, we change world; As well as collisions"""
        # Portals
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)
                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)

        # Collisions
        for sprite in self.get_group().sprites():
            if type(sprite) is NPC:
                if sprite.feet.colliderect(self.player.rect):
                    sprite.speed = 0
                else:
                    sprite.speed = 0.5
            if sprite.feet.collidelist(self.get_walls()) > -1:
                collision = pygame.mixer.Sound('../assets/sounds/achivments/collision.wav')
                collision.play(1)
                sprite.move_back()

    def teleport_player(self, name):
        """Change map player with spawn point"""
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[], npcs=[]):
        """Changing the new map"""
        #Loading the map using the tmx module
        tmx_data = pytmx.util_pygame.load_pygame(f"../assets/maps/{name}.tmx") #f allows to make the link between text and variables
        map_data = pyscroll.data.TiledMapData(tmx_data)
        #The map takes the size of the screen
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        #Zoom on the map (and therefore also the player)
        map_layer.zoom = 2


        #Collision management
        walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        #draw the layer group and the player
        group = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=4)  # default_layer = layer level on tmx file
        group.add(self.player)

        #Collect the npcs to add them to the group
        for npc in npcs:
            group.add(npc)

        #Create a map object and add to my list
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs)

    def get_map(self):
        """Return the current map"""
        return self.maps[self.current_map]

    def get_group(self):
        """Return the map group"""
        return self.get_map().group
    
    def get_walls(self):
        """Return the walls for collisions on my map"""
        return self.get_map().walls

    def get_object(self, name):
        """Return the object names of the map"""
        return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        """Addition of NPCs on their respective location"""
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def draw(self):
        """Map display"""
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        """Constantly check the events"""
        self.get_group().update()
        self.check_collision()

        for npc in self.get_map().npcs:
            npc.move()