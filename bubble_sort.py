import random
import pygame
import sys
import time

import settings

# To avoid Windows 10 scaling.
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Global Variables
numberOfNumbers = 100
numberOfOperations = 0
minimum = 1
maximum = 10000
isSorted = False
FPS = 120

# Initialize pygame and the window.
pygame.init()
windowSurface = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption("Bubble sort")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)


def get_new_list():
    listOfNumbers = []
    for i in range(numberOfNumbers):
        newNum = random.randint(1,10000)
        listOfNumbers.append(newNum)
    
    return listOfNumbers


def bubble_sort(listOfNums):
    global isSorted
    global numberOfOperations
    
    lastIndex = numberOfNumbers - 1
    numberOfOperations = 0
    
    while not isSorted:
        isSorted = True
        lastIndexCopy = lastIndex
        for i in range(lastIndexCopy):
            if listOfNums[i] > listOfNums[i+1]:
                isSorted = False
                numberOfOperations += 1
                
                listOfNums[i], listOfNums[i+1] = listOfNums[i+1], listOfNums[i]
                lastIndex = i
                yield i
        

def scaleNumber(num):
    newNum = ((settings.height-settings.yOffset)*
              (num-minimum)/(maximum-minimum))
    return newNum


def draw_column(num, pos, color):
    """ Draw the rect that represents the current number. """
    
    colWidth = round((settings.width-2*settings.xOffset)/(numberOfNumbers))
    colHeight = round(scaleNumber(num))
    
    colRect = pygame.Rect(0,0,colWidth,colHeight)    
    colRect.left = settings.xOffset + pos*colWidth
    colRect.bottom = windowSurface.get_rect().bottom
    
    pygame.draw.rect(windowSurface, color, colRect) 


def display_operations(number):
    """ Display the number above the column. """
    numberImage = font.render(str(number), True,
                             settings.columnColor, settings.backgroundColor)
    numberRect = numberImage.get_rect()
    numberRect.top = windowSurface.get_rect().top + 20
    numberRect.left = windowSurface.get_rect().left + 20
    windowSurface.blit(numberImage, numberRect)


def display(listOfNums, index):
    """ Update the screen. """
    windowSurface.fill(settings.backgroundColor)
    
    for i in range(numberOfNumbers):
        # If the current number is the last compared one, change its color.
        if i == index:
            color = (128, 128, 128)
        else:
            color = settings.columnColor
        
        draw_column(listOfNums[i], i, color)
        display_operations(numberOfOperations)
        
    pygame.display.flip()
    clock.tick(FPS)


def check_input():
    global isSorted
    """ Check if any key or button was pressed. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if isSorted:
                    isSorted = False
                    run_program()
                    

def run_program():
    """ Keeps running the program in a while loop. """
    listOfNums = get_new_list()
    while True:
        if not isSorted:
            for step in bubble_sort(listOfNums):
                display(listOfNums, step)
                check_input()
                
        check_input()
        display(listOfNums, 0)
            

if __name__ == "__main__":
    run_program()