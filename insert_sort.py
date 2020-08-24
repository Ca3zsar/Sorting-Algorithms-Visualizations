import pygame
import sys
import random

import settings
import aux_functions

# To avoid Windows 10 scaling.
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Global Variables
isSorted = False
numberOfOperations = 0

# Initialize pygame and the window.
windowSurface, clock, font = aux_functions.initialize("Insertion Sort")


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


def insertion_sort(listOfNums):
    global numberOfOperations
    for i in range(1, len(listOfNums)):
        index = i-1
        value = listOfNums[i]
        while index >= 0 and listOfNums[index]>value:
            
            numberOfOperations += 1
            aux_functions.display(listOfNums, index + 1, numberOfOperations,
                              windowSurface, font, clock)
            check_input()
            
            listOfNums[index + 1] = listOfNums[index]
            index -= 1
        listOfNums[index + 1] = value
            

def run_program():
    global isSorted, numberOfOperations
    numberOfOperations = 0
    newList = aux_functions.get_new_list()
    while True:
        if not isSorted:
            insertion_sort(newList)
            isSorted = True
            
        check_input()
        aux_functions.display(newList, 0, numberOfOperations,
                              windowSurface, font, clock)    
    
run_program()