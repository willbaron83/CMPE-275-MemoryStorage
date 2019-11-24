#!/usr/bin/env python
# -*- coding: utf-8
from storage import MemoryManager
from pprint import pprint as pp
import pika



class TreeNode:
    is_leaf = ""
    num_keys = 0
    keys = []

    def __init__(self, level):
        self.is_leaf = True
        self.num_keys = level


