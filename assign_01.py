import json
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
from indexer.abstract_index import AbstractIndex
from indexer.maps.hash_map import HashMapIndex
from indexer.unsorted_lists.unsorted_list import UnsortedList

import os
import pstats
import string
import time 
import random 
import pickle
import cProfile


def index_files(path: str, index: AbstractIndex) -> None:
    

    for folder in path:
        print(f"Processing folder: {folder}")  # Debug statement

        # Loop through all files in the folder
        for filename in os.listdir(folder):
            # print("file test")
            # print(filename)
            file_path = os.path.join(folder, filename)  # Get full path of the file
            if os.path.isfile(file_path):  # Ensure it's a file and not a subdirectory
                with open(file_path, 'r') as file:  # Open the file
                    data = json.load(file)
                    words = data["preprocessed_text"]
                    
                    for word in words:
                        index.insert(word, filename)
        
<<<<<<< HEAD
@timer
def loopy_loop():
    total = sum((x for x in range(0, 1000000)))
=======
# @timer
# def loopy_loop():
#     total = sum((x for x in range(0, 1000000)))

@timer 
def searchtime(structure, search_terms):
    for term in search_terms:
        structure.search(term)

>>>>>>> 93af2c7f90 (fixed the search functions and the hashmap data structure and how we get keys for each structure in main)


def main():
    # print("start")

    # path = ["USFinancialNewsArticles-preprocessed/April2018", "USFinancialNewsArticles-preprocessed/February2018",
    #     "USFinancialNewsArticles-preprocessed/January2018", "USFinancialNewsArticles-preprocessed/March2018",
    #     "USFinancialNewsArticles-preprocessed/May2018"]
    # path = ["USFinancialNewsArticles-preprocessed/April2018"]
    path = ["test_data/folder1"]

    # for the unsorted list (currently using time to measure how long did it take)
    unsorted = UnsortedList()
    index_files(path, unsorted) # get a data structure with every word
    # Create a list of 100,000 random search terms
    all_terms = [term for term, _ in unsorted.unsorted_list]
    search_terms = random.choices(all_terms, k=10)  # shuffle stuff?
    # Measure the time taken for searching n words

    # for term in search_terms:
    #     unsorted.search(term)
    searchtime(unsorted, search_terms)


    # for the hashmap
    hashmap = HashMapIndex()
    # print("hi")
    index_files(path, hashmap)
    # print("test")
    all_terms = [term for term in hashmap.hash_map.keys()]
    search_terms = random.choices(all_terms, k=10)
    # Measure the time taken for searching n words

    # for term in search_terms:
    #     # print("5")
    #     hashmap.search(term)

    searchtime(hashmap, search_terms)

    # # for the avl tree
    avl_tree = AVLTreeIndex()
<<<<<<< HEAD
    avl_tree.insert(3, "a")
    avl_tree.insert(2, "b")
    avl_tree.insert(1, "c")
    print(avl_tree.tree_height())
    # print(avl_tree.height)
    print(avl_tree.get_keys_in_order())
=======
    # print(avl_tree)
>>>>>>> 93af2c7f90 (fixed the search functions and the hashmap data structure and how we get keys for each structure in main)
    
    index_files(path, avl_tree)
    # Create a list of 100,000 random search terms
    # all_terms = [term for term, _ in avl_tree.root]
    all_terms = avl_tree.get_keys()
    search_terms = random.choices(all_terms, k=10)
    # # Measure the time taken for searching n words
    # for term in search_terms:
    #     avl_tree.search(term)
    searchtime(avl_tree, search_terms)


    # # Here, we are creating a sample binary search tree index 
    # # and sending it to the index_files function
<<<<<<< HEAD
    # bst_index = BinarySearchTreeIndex()    
    # index_files(path, bst_index)
=======
    bst_index = BinarySearchTreeIndex()    
    index_files(path, bst_index)
    all_terms = bst_index.get_keys_in_order() 
    search_terms = random.choices(all_terms, k=10)

    searchtime(bst_index, search_terms)


>>>>>>> 93af2c7f90 (fixed the search functions and the hashmap data structure and how we get keys for each structure in main)

    # As a gut check, we are printing the keys that were added to the 
    # index in order. 
    # print(bst_index.get_keys_in_order())








if __name__ == "__main__":
    main()
