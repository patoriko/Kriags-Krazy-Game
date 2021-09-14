import os
import pygame.image
from pygame.locals import *


def renderImage(file, transparent=True):
    filename = os.path.join('Images', file)
    image = pygame.image.load(filename)
    if transparent == True:
        image = image.convert()
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()
    return image
