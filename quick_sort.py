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
windowSurface, clock, font = aux_functions.initialize("Quick Sort")

def partition(listOfNums, start, end):
    global numberOfOperations
    
    pivot = random.randint(start, end)
    listOfNums[pivot], listOfNums[end] = listOfNums[end], listOfNums[pivot]
    
    index = start
    for i in range(start, end):
        if listOfNums[i] < listOfNums[end]:
            listOfNums[i], listOfNums[index] = listOfNums[index], listOfNums[i]
            index += 1
            numberOfOperations += 1
            aux_functions.display(listOfNums, i, numberOfOperations,
                                  windowSurface, font, clock)
        check_input()
    
    listOfNums[index], listOfNums[end] = listOfNums[end], listOfNums[index]
    aux_functions.display(listOfNums, index, numberOfOperations,
                        windowSurface, font, clock)
    return index
    

def quick_sort(listOfNums, start, end):
    if start<end:
        pivot = partition(listOfNums, start, end)
        
        quick_sort(listOfNums, start, pivot - 1)
        quick_sort(listOfNums, pivot + 1, end)


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
    global isSorted, numberOfOperations
    numberOfOperations = 0
    newList = aux_functions.get_new_list()
    while True:
        if not isSorted:
            quick_sort(newList, 0, len(newList)-1)
            isSorted = True
        check_input()
        aux_functions.display(newList, 0, numberOfOperations,
                              windowSurface, font, clock)
    
run_program()