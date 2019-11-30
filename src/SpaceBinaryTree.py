#!/usr/bin/env python
# -*- coding: utf-8
from src.TreeNode import TreeNode
from sortedcontainers import SortedDict

class SpaceBinaryTree:
    '''
    Atrributes
    '''

    head = None
    sorted_dict = None


    '''
    Methods
    '''

    # Constructor
    def __init__(self, size, free_pages):
        # define the attributes
        free_pages = [x for x in range(free_pages)]
        self.head = TreeNode(node_left=None, node_right=None, size=size, free_pages=free_pages)
        self.sorted_dict = SortedDict({size: TreeNode(node_left=None,
                                                      node_right=None,
                                                      size=size,
                                                      free_pages=[[free_pages]])})

    def set_empty_space(self, num_of_slots, free_pages):
        if self.sorted_dict.get(num_of_slots):
            self.sorted_dict.get(num_of_slots).set_free_pages(free_pages)
        # If the key does not exist, then we create a new node and add
        # the list to a new node
        else:
            self.sorted_dict[num_of_slots] = TreeNode(node_left=None,
                                                       node_right=None,
                                                       size=num_of_slots,
                                                       free_pages=[[free_pages]])

    # else:
    # print("Index Error, the node has no list remaining")



    def get_available_space(self, number_of_chunks):
        #number of spaces is available in sorted dict
        if self.sorted_dict.get(number_of_chunks):
            temp_list = self.sorted_dict.get(number_of_chunks).free_pages.pop(0)
        else:
            '''
            Either the chunck is largest or smallest than the chunks available.
            '''
            # Get the largest space available from sorted dict
            largest_chuck = self.sorted_dict.keys()[-1]
            # Find if the number of chunks needed is lower than the largest available
            if number_of_chunks < largest_chuck:
                # if it is, we need to take one of those chunks and break it down
                #first we get the whole node out of the sorted dict
                temp_node = self.sorted_dict.pop(largest_chuck)
                #find if the node free pages list is not empty
                if not temp_node.is_node_empty:
                    # pop the first list of pages available in the free_pages list.
                    # remember that free pages is a list if list of pages
                    # The structure is to be able to keep list of pages that are the same size under
                    # a single dictionary with key number of free pages
                    temp_list = temp_node.free_pages.pop(0)
                    # Once we have the new list, we need to split it into the pages
                    # needed nad the remaining ones.
                    ret_list = temp_list[:number_of_chunks]
                    # Then we store the remaining list in an existing key
                    rem_list = temp_list[number_of_chunks:]
                    self.set_empty_space(len(rem_list), rem_list)
            else:
                #number of chunks is larger than largest spot available.
                enough_pages = False
                page_list = []
                free_pages_left = number_of_chunks
                # We are going to start looking at the smallest set of page lists
                # and we are going to add as many pages needed for the chunks to fit in
                while not enough_pages:
                    avail_pages_list = self.sorted_dict.keys()
                    if avail_pages_list[0] < free_pages_left:
                        for lp in self.sorted_dict.get(avail_pages_list[0]).get_all_free_pages():
                                if free_pages_left > len(lp):
                                    page_list = page_list + lp
                                    free_pages_left = free_pages_left - len(page_list)
                                else:
                                    page_list = page_list + lp[:free_pages_left]
                                    free_pages_left = free_pages_left - len(page_list)
                                    self.set_empty_space(len(free_pages_left), free_pages_left)

                        if free_pages_left > 0:
                            self.sorted_dict.pop(avail_pages_list[0])
                            continue







