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

        
@timer
def loopy_loop():
    total = sum((x for x in range(0, 1000000)))


def main():
    print("start")

    path = ["USFinancialNewsArticles-preprocessed/April2018", "USFinancialNewsArticles-preprocessed/February2018",
        "USFinancialNewsArticles-preprocessed/January2018", "USFinancialNewsArticles-preprocessed/March2018",
        "USFinancialNewsArticles-preprocessed/May2018"]
    # path = ["test_data/folder1"]

    # for the unsorted list (currently using time to measure how long did it take)
    # unsorted = UnsortedList()
    # index_files(path, unsorted) # get a data structure with every word
    # # Create a list of 100,000 random search terms
    # all_terms = [term for term, _ in unsorted.unsorted_list]
    # search_terms = random.choices(all_terms, k=100000)  # shuffle stuff?
    # # Measure the time taken for searching 100,000 words
    # start_time = time.time()
    # for term in search_terms:
    #     unsorted.search(term)
    # end_time = time.time()
    # print(f"Time taken to search 100,000 words for the unsorted list: {end_time - start_time:.2f} seconds")

    # for the hashmap
    # hashmap = HashMapIndex()
    # index_files(path, hashmap)
    # # Create a list of 100,000 random search terms
    # print("test")
    # all_terms = [term for term, _ in hashmap.hash_map.items()]
    # print("test finish")
    # # search_terms = random.choices(hashmap, k=10)
    # # search_terms = random.choices(hashmap.keys(), k=10)
    # search_terms = random.choices(all_terms, k=10)
    # # Measure the time taken for searching 100,000 words
    # start_time = time.time()
    # for term in search_terms:
    #     print("5")
    #     hashmap.search(term)
    # end_time = time.time()
    # print(f"Time taken to search 100,000 words for the hashmap: {end_time - start_time:.2f} seconds")

    # # for the avl tree
    avl_tree = AVLTreeIndex()
    avl_tree.insert(3, "a")
    avl_tree.insert(2, "b")
    avl_tree.insert(1, "c")
    print(avl_tree.tree_height())
    # print(avl_tree.height)
    print(avl_tree.get_keys_in_order())
    
    # index_files(path, avl_tree)
    # # Create a list of 100,000 random search terms
    # all_terms = [term for term, _ in avl_tree.root]
    # search_terms = random.choices(all_terms, k=100000)
    # # Measure the time taken for searching 100,000 words
    # start_time = time.time()
    # for term in search_terms:
    #     avl_tree.search(term)
    # end_time = time.time()
    # print(f"Time taken to search 100,000 words for the AVL tree: {end_time - start_time:.2f} seconds")


    # # Here, we are creating a sample binary search tree index 
    # # and sending it to the index_files function
    # bst_index = BinarySearchTreeIndex()    
    # index_files(path, bst_index)

    # As a gut check, we are printing the keys that were added to the 
    # index in order. 
    # print(bst_index.get_keys_in_order())
    # quick demo of how to use the timing decorator included
    # in indexer.util
    # loopy_loop()


if __name__ == "__main__":
    main()
