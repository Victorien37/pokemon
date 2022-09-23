"""
    File name :                 loadmap.py
    Author :                    Victorien Rodrigues
    Creation date :             16/09/2022
    Last modification date :    16/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Map route
"""
#Importing libraries
from map import *

map = MapManager

# Portal("nom mode actuel", "nom du portail", "nom du monde cible", "nom du spawn")
##########  ##########
map.register_map("bonaugure", portals=[
            Portal(from_world="bonaugure", origin_point="enter_my_home", target_world="my_home", teleport_point="spawn_player"),
            Portal(from_world="bonaugure", origin_point="enter_rival_home", target_world="rival_home", teleport_point="spawn"),
            Portal("bonaugure", "enter_route-201", "route-201", "spawn_route-201")
        ], npcs=[
            NPC("electro", nb_points=2, dialogs=["Tout le monde part à l'aventure","et devient peu à peu adulte..."])
        ])