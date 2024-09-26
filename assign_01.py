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
                with open(file_path, 'r', encoding='utf-8') as file:  # Open the file
                    data = json.load(file)
                    words = data["preprocessed_text"]

                    for word in words:
                        index.insert(word, filename)


# @timer
# def loopy_loop():
#     total = sum((x for x in range(0, 1000000)))

@timer
def search_time(structure, search_terms):
    for term in search_terms:
        structure.search(term)


def main():
    path = ["USFinancialNewsArticles-preprocessed/April2018", "USFinancialNewsArticles-preprocessed/February2018",
        "USFinancialNewsArticles-preprocessed/January2018", "USFinancialNewsArticles-preprocessed/March2018",
        "USFinancialNewsArticles-preprocessed/May2018"]
    # path = ["USFinancialNewsArticles-preprocessed/April2018"]
    # # path = ["test_data/folder1"]
    # #
    # # for the unsorted list (currently using time to measure how long did it take)
    # unsorted = UnsortedList()
    # index_files(path, unsorted)  # get a data structure with every word
    # all_terms = [term for term, _ in unsorted.unsorted_list]  # create a list of 100,000 random search terms
    # search_terms = random.choices(all_terms, k=10000)
    # search_time(unsorted, search_terms)

    # for the hashmap
    # hashmap = HashMapIndex()
    # index_files(path, hashmap)
    # all_terms = [term for term in hashmap.hash_map.keys()]
    # search_terms = random.choices(all_terms, k=500000)
    # search_time(hashmap, search_terms)

    # for the avl tree
    avl_tree = AVLTreeIndex()
    # avl_tree.insert(3, "a")
    # avl_tree.insert(2, "b")
    # avl_tree.insert(1, "c")
    # print(avl_tree.tree_height())
    # print(avl_tree.get_keys_in_order())

    index_files(path, avl_tree)
    all_terms = avl_tree.get_keys()
    search_terms = random.choices(all_terms, k=500000)
    search_time(avl_tree, search_terms)

    # # # Here, we are creating a sample binary search tree index
    # # # and sending it to the index_files function
    # bst_index = BinarySearchTreeIndex()
    # index_files(path, bst_index)
    # all_terms = bst_index.get_keys_in_order()
    # search_terms = random.choices(all_terms, k=10)
    #
    # search_time(bst_index, search_terms)

    # As a gut check, we are printing the keys that were added to the 
    # index in order. 
    # print(bst_index.get_keys_in_order())


if __name__ == "__main__":
    main()
