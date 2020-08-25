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
windowSurface, clock, font = aux_functions.initialize("Selection Sort")


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
                

def selection_sort(listOfNums):
    global numberOfOperations
    for i in range(len(listOfNums)):
        minimum = listOfNums[i]
        index = i
        for j in range(i+1,len(listOfNums)):
            check_input()
            numberOfOperations += 1
            if listOfNums[j] < minimum:
                minimum = listOfNums[j]
                index = j
            
            aux_functions.display(listOfNums, j, index, numberOfOperations,
                            windowSurface, font, clock)
            
        listOfNums[i], listOfNums[index] = listOfNums[index], listOfNums[i]   
        aux_functions.display(listOfNums, i, index, numberOfOperations,
                              windowSurface, font, clock)             
        

def run_program():
    global isSorted, numberOfOperations
    numberOfOperations = 0
    
    newList = aux_functions.get_new_list()
    while True:
        if not isSorted:
            selection_sort(newList)
            isSorted = True
        check_input()
        aux_functions.display(newList, len(newList), 0, numberOfOperations,
                              windowSurface, font, clock) 
    

run_program()