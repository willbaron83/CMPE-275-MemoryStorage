#!/usr/bin/env python
# -*- coding: utf-8
import math

from src.Page import Page

class MemoryManager:
    '''
    Atrributes
    '''

    page_list = []
    memory_tracker = {}  # key: memory_hash_id, value: list_of_pages_ids>
    total_memory_size = 0
    page_size = 0
    number_of_pages = 0
    list_of_pages_used = []
    fragmentation_threshold = 0

    '''
    Methods
    '''
    #Constructor
    def __init__(self, total_memory_size, page_size):
        #define the attributes
        self.total_memory_size = total_memory_size
        self.page_size = page_size

        self.number_of_pages = math.floor(self.total_memory_size / self.page_size)
        self.page_list = [Page(self.page_size)] * self.number_of_pages
        print("Number of pages in memory", len(self.page_list))


    def put_data(self, memory_id, data_chunks, num_of_chunks):
        '''
        :param memory_id:
        :param data_chunks:
        :param num_of_chunks:
        :return:
        '''

        if memory_id in self.memory_tracker:
            print("The following memory id exist and it will be overwritten: ", memory_id)
        else:
            print("Writing new memory_id: ", memory_id)

        # find available blocks of pages to save the data
        target_list_indexes = self.find_n_available_pages(num_of_chunks)

        # save the data in pages
        index_counter = 0
        for c in data_chunks:
            self.page_list[target_list_indexes[index_counter]].put_data(c)
            index_counter = index_counter + 1

        # update the list with used pages
        self.list_of_pages_used.extend(target_list_indexes)
        # update memory dic
        self.memory_tracker[memory_id] = target_list_indexes

        print(self.page_list[1].data)
        print("Successfully saved the data.")
        print("Free pages left: ", self.get_number_of_pages_available())

    def get_number_of_pages_available(self):
        return self.number_of_pages - len(self.list_of_pages_used)

    def get_memory_available_gb(self):
        return (self.number_of_pages - len(self.list_of_pages_used)) * self.page_size

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

    # this function is very slow, we need to improve it
    def find_n_available_pages(self, n):
        list_indexes_to_use = []

        for i in range(0, len(self.page_list)):
            if i not in self.list_of_pages_used:
                list_indexes_to_use.append(i)
                if len(list_indexes_to_use) == n:
                    break
        print("Found the following number of pages to save the data: ", len(list_indexes_to_use))
        return list_indexes_to_use

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