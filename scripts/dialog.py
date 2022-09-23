"""
    File name :                 dialog.py
    Author :                    Victorien Rodrigues
    Creation date :             23/09/2022
    Last modification date :    23/09/2022
    Python version :            3.10.7
    Pygame version :            2.1.2
    Lang :                      FR
    Description :               Dialog box and font management
"""

#Importing librairies
import pygame

class DialogBox:
    """ DialogBox class, Instanciate a DialogBox object """
    X_POSITION = 650
    Y_POSITION = 800
    
    def __init__(self):
        """ DialogBox constructor """
        # Load an image, a font and dialog box
        self.box = pygame.image.load('../assets/dialogs/dialog.png')
        self.box = pygame.transform.scale(self.box, (600, 100))
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font('../assets/dialogs/dialog_font.ttf', 18)
        self.reading = False
        
    def execute(self, dialog=[]):
        """ Open a dialog box and display dialogs"""
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog
            
    def render(self, screen):
        """ Display dialog box and dialogs with a writing effect """
        if self.reading:
            self.letter_index += 1
            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 30 , self.Y_POSITION + 10))
            
    def next_text(self):
        """ If there are many dialogs, we read else there are no dialog boxes """
        self.text_index += 1
        self.letter_index = 0
        if self.text_index >= len(self.texts):
            # Close the dialog box
            self.reading = False