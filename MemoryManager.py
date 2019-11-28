#!/usr/bin/env python
# -*- coding: utf-8
import PageClass
import SpaceBinaryTree
import TreeNode

class MemoryManager:
    '''
    Atrributes
    '''

    page_list = []
    memory_tracker = {} #<memory_id, binary data>
    memory_size = 0
    page_size = 0
    memory_available = 0
    memory_used = 0
    fragmentation_threshold = 0

    '''
    Methods
    '''
    #Constructor
    def __init__(self):
        #define the attributes
        #TODO
        pass

    def put_data(self, data):
        '''
        :param data:
        :return:
        '''
        #TODO
        pass

    def get_data(self, memory_id):
        '''
        :param memory_id:
        :return:
        '''
        #TODO
        pass

    def update_data(self, data, memory_id):
        '''
        :param data:
        :param memory_id:
        :return:
        '''
        #TODO
        pass

    def delete_data(self, memory_id):
        '''
        :param memory_id:
        :return:
        '''
        #TODO
        pass

    def defragment_data(self):
        '''
        :param data:
        :param list_of_pages:
        :return:
        '''
        #TODO
        pass

    def partition_data(self, data, list_of_pages):
        '''
        :param data:
        :param list_of_pages:
        :return:
        '''
        #TODO
        pass

    def update_binary_tree(self):
        '''
        :return:
        '''
        #TODO
        pass