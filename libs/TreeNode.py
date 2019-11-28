#!/usr/bin/env python
# -*- coding: utf-8


class TreeNode:
    is_leaf = ""
    num_keys = 0
    keys = []

    def __init__(self, level):
        self.is_leaf = True
        self.num_keys = level


