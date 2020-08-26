import pygame
import sys

import settings
import aux_functions

# To avoid Windows 10 scaling.
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Global Variables
numberOfOperations = 0
isSorted = False

# Initialize pygame and the window.
windowSurface, clock, font = aux_functions.initialize("Bubble Sort")

def bubble_sort(listOfNums):
    global isSorted
    global numberOfOperations
    
    lastIndex = settings.numberOfNumbers - 1
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
            if event.key == pygame.K_LEFT:
                settings.FPS -= 10
                print(settings.FPS)
            if event.key == pygame.K_RIGHT:
                settings.FPS += 10
                print(settings.FPS)
                    

def run_program():
    """ Keeps running the program in a while loop. """
    listOfNums = aux_functions.get_new_list()
    while True:
        if not isSorted:
            for step in bubble_sort(listOfNums):
                aux_functions.display(listOfNums, step, numberOfOperations,
                                     windowSurface, font, clock)
                check_input()
                
        check_input()
        aux_functions.display(listOfNums, 0, numberOfOperations, windowSurface,
                              font, clock)
            

if __name__ == "__main__":
    run_program()
