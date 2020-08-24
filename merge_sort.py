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
windowSurface, clock, font = aux_functions.initialize("Merge Sort")


def merge(listOfNums, start, mid, end):
    global numberOfOperations
    
    n1 = mid - start + 1
    n2 = end - mid

    A = [0]*n1
    B = [0]*n2

    for i in range(n1): 
        A[i] = listOfNums[start + i] 
  
    for j in range(0 , n2): 
        B[j] = listOfNums[mid + 1 + j] 

    i,j,k = 0, 0, start

    while i < n1 and j < n2 : 
        if A[i] <= B[j]: 
            listOfNums[k] = A[i] 
            i += 1
        else: 
            listOfNums[k] = B[j] 
            j += 1
        k += 1
        numberOfOperations += 1
        aux_functions.display(listOfNums, k, numberOfOperations, 
                              windowSurface, font, clock)
        check_input()
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        listOfNums[k] = A[i] 
        i += 1
        k += 1
        numberOfOperations += 1
        aux_functions.display(listOfNums, k, numberOfOperations, 
                              windowSurface, font, clock)
        check_input()
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        listOfNums[k] = B[j] 
        j += 1
        k += 1
        numberOfOperations += 1
        aux_functions.display(listOfNums, k, numberOfOperations, 
                              windowSurface, font, clock)
        check_input()


def merge_sort(listOfNums, start, end):
    if start<end:
        mid = start + (end-start)//2
        
        merge_sort(listOfNums, start, mid)
        merge_sort(listOfNums, mid+1, end)

        merge(listOfNums, start, mid, end)
        
        
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
            merge_sort(newList, 0, len(newList)-1)
            isSorted = True
        check_input()
        aux_functions.display(newList, 0, numberOfOperations, 
                              windowSurface, font, clock)
    

run_program()
