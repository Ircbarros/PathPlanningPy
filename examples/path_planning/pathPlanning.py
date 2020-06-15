#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Italo Barros
Email: ircbarros@pm.me
License: MIT

The Path Planning algorithms for the World Grid Module!

Comments:

If you are using VS Code, please install the Better Comments Extension:

    # Indicates the Method
    #* Indicates some Important Information
    #! Indicates a deprecated or Warning Information
    #? Indicates possible future changes and questions
    #TODO: Indicates the future changes and optimizations

Need to change the code? Refactor? Help the next developer! Use a 
Style Guide to help others understand of your code. For more informations
about the Google Style Guide used here go to:

https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

'''

import os
import sys
import time
import pygame
#? Using the collections module since is the most efficient
#? to implement and manipulate a queue list
from collections import deque


# GLOBAL VARIABLES
#* Load the PyGame Vector2 lib
vec = pygame.math.Vector2
#* The position X in the grid
pos_x = 0
#* The position Y in the grid
pos_y = 0

def find_free_space(graph, position=(pos_x, pos_y)):
    """
    Reads free nodes in World Grid using the find_neighbors(node) function,
    and returns a list of free nodes that can be explored starting from the
    position inputed.

    Atrributes:

    (graph) (Class)
    (position) (tuple)
    
    Args:

        (graph): A World Grid Class
        (pos_x, pos_y): Is the start position in the World Grid that
                        we want to find the free space as a tuple
    
    Vars:

        pos_x = The node position in the X axys (column)
        pos_y = The node position in the Y axys (row)
    
    Returns:

        A list with the free nodes available in the World Grid

    [Example]

        USER DEFINED VALUES:



    """
    # SET THE POSITION USING LIST COMPREHENSION
    position_x, position_y = position[0], position[1]
    # TRANSFORM THE POSITION TO THE PYGAME VECTOR
    position = vec(position_x, position_y)
    # IMPORT THE DEQUE TO PUT THE NODES
    frontier = deque()
    # APPEND THE FRONTIER WITH THE POSITION
    frontier.append(position)
    print(f'Frontier: {frontier}')
    # THE LIST OF VISITED NODES
    visited = []
    print(f'Visited: {visited}')
    # THE POSITION WILL BE PUT AT THE VISITED QUEUE (IS WHERE WE ARE)
    visited.append(position)
    # START OUR LOOP
    #* As long there's nodes on the frontier do
    while len(frontier) > 0:
        # THE CURRENT NODE WE WANT TO LOOK IS THE NEXT NODE
        #* Pop's the next on the queue list
        current = frontier.popleft()
        print(f'Current: {current}')
        print(graph.find_neighbors(vec(current)))
        # THE NEIGHBOORS OF THE CURRENT TILE
        for next in  graph.find_neighbors(current):
            print("OK! Entered in the For LOOP")
            # IF THE NEXT NODE IS NOT VISITED
            if next not in visited:
                # ADD THE NODE TO THE FRONTIER LIST
                frontier.append(next)
                # PUT ON THE VISITED NODES
                visited.append(next)
    # PRINT ALL THE VISITED NODES
    print(f'The Visited Nodes are:\n{visited}')