#!/usr/bin/env python
# -*- coding: utf-8
from storage import MemoryManager
from pprint import pprint as pp
import pika



class TreeNode:
    node_left = None
    node_right= None
    size = 0
    free_pages = []

    def __init__(self, node_left, node_right, size, free_pages):
        self.node_left = node_left
        self.node_right = node_right
        self.size - size
        self.free_pages = free_pages

    def insert_left_node(self, node):
        self.node_left = node

    def insert_right_node(self, node):
        self.node_right = node

    def set_size(self, size):
        self.size = size

    def set_free_pages(self, pages):
        self.free_pages.append(pages)

    def get_left_node(self):
        return self.node_left

    def get_right_node(self):
        return self.node_right

    def get_size(self):
        return self.size;

    def get_free_pages(self):
        return self.free_pages

