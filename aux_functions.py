import random
import pygame
import settings

### Function to initialize pygame, font and surfaces.

def initialize(name):
    pygame.init()
    windowSurface = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption(name)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    
    return windowSurface, clock, font


### Functions for gettings a list and scaling numbers ###

def get_new_list():
    listOfNumbers = []
    for i in range(settings.numberOfNumbers):
        newNum = random.randint(settings.minimum, settings.maximum)
        listOfNumbers.append(newNum)
    
    return listOfNumbers


def scaleNumber(num):
    """ 
    Get a number between 0 and the number of pixels allocated for the drawing 
    of the column.
    """
    newNum = ((settings.height-settings.yOffset)*
              (num-settings.minimum)/(settings.maximum-settings.minimum))
    return newNum


### Functions to display columns or text.

def display_operations(number, windowSurface, font):
    textToDisplay = f"Number of comparisons : {number}"
    numberImage = font.render(textToDisplay, True,
                             settings.columnColor, settings.backgroundColor)
    numberRect = numberImage.get_rect()
    numberRect.top = windowSurface.get_rect().top + 20
    numberRect.left = windowSurface.get_rect().left + 20
    windowSurface.blit(numberImage, numberRect)


def draw_column(num, pos, color, windowSurface):
    """ Draw the rect that represents the current number. """
    
    colWidth = round((settings.width-2*settings.xOffset)/
                     (settings.numberOfNumbers))
    colHeight = round(scaleNumber(num))
    
    # Draw the rect for the column
    colRect = pygame.Rect(0,0,colWidth-1,colHeight)    
    colRect.left = settings.xOffset + pos*colWidth + 1
    colRect.bottom = windowSurface.get_rect().bottom
    
    # Draw a border of the columm
    borderRect = pygame.Rect(0,0,colWidth+1,colHeight+1)
    borderRect.left = settings.xOffset + pos*colWidth
    borderRect.bottom = windowSurface.get_rect().bottom
    
    pygame.draw.rect(windowSurface, settings.backgroundColor, borderRect)
    pygame.draw.rect(windowSurface, color, colRect) 


def display(listOfNums, index, minim, numberOfOperations, 
            windowSurface, font, clock):
    """ Update the screen. """
    windowSurface.fill(settings.backgroundColor)
    
    for i in range(settings.numberOfNumbers):
        # If the current number is the last compared one, change its color.
        if i == index:
            color = settings.highlightColor
        elif i == minim:
            color = settings.minColor
        else:
            color = settings.columnColor
        
        draw_column(listOfNums[i], i, color, windowSurface)
        display_operations(numberOfOperations, windowSurface, font)
        
    pygame.display.flip()
    clock.tick(settings.FPS)