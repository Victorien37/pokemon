"""
    File name :                 button.py
    Author :                    Victorien Rodrigues
    Creation date :             23/12/2022
    Last modification date :    23/12/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Create a button or a menu
"""
import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, rect, text, font, fgcolor, bgcolor, active_color, command):
        super().__init__()
        self.rect = rect
        self.text = text
        self.font = font
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.active_color = active_color
        self.command = command
        
        self.menu_open = False
        
    
    def draw(self, surface):
        # Détermine la couleur de fond en fonction de l'état du bouton
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            color = self.active_color
        else:
            color = self.bgcolor

        # Dessine le fond du bouton
        pygame.draw.rect(surface, color, self.rect)

        # Dessine le texte du bouton
        text_surface = self.font.render(self.text, True, self.fgcolor)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def on_click(self):
        if self.command is not None:
            self.command()
        