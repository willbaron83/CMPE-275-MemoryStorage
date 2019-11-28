#!/usr/bin/env python
# -*- coding: utf-8
from src.TreeNode import TreeNode

class SpaceBinaryTree:
    '''
    Atrributes
    '''

    head = None



    '''
    Methods
    '''

    # Constructor
    def __init__(self):
        # define the attributes
        head = TreeNode(node_left=None, node_right=None, size=None, free_pages=[])

    def set_empty_space(self, size, slots):
        if self.head.size == None:
            self.head.set_size(size)
            self.head.set_free_pages(slots)

        elif size == self.head.size:
            self.head.set_free_pages(slots)

        else:
            pass


    def get_available_node(self, size):
        pass