
import json
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
from indexer.abstract_index import AbstractIndex

# importing all libraries he showed us in class --laura
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
            file_path = os.path.join(folder, filename)  # Get full path of the file
            if os.path.isfile(file_path):  # Ensure it's a file and not a subdirectory
                with open(file_path, 'r') as file:  # Open the file
                    # data = json.load(file)  
                    data = json.load(file)
                    words = data["preprocessed_text"]
                    
                    for word in words:
                        index.insert(word, filename)

        
@timer
def loopy_loop():
    total = sum((x for x in range(0, 1000000)))


def main():
    # You'll need to change this to be the absolute path to the root folder
    # of the dataset
    # data_directory = '/Users/lauraboelsterli/Downloads/DS4300/24f-a01-indexit-laurab/USFinancialNewsArticles-preprocessed'
    path = ["USFinancialNewsArticles-preprocessed/April2018", "USFinancialNewsArticles-preprocessed/February2018",
            "USFinancialNewsArticles-preprocessed/January2018", "USFinancialNewsArticles-preprocessed/March2018",
            "USFinancialNewsArticles-preprocessed/May2018"]   
    # Here, we are creating a sample binary search tree index 
    # and sending it to the index_files function
    bst_index = BinarySearchTreeIndex()    
    index_files(path, bst_index)
    # function that implements search function
    bst_index.search('voyaging')


    # As a gut check, we are printing the keys that were added to the 
    # index in order. 
    # print(bst_index.get_keys_in_order())
    
    # hashmap_idx = HashMapIndex()
    # index_files(path, hashmap_idx)

    
    # quick demo of how to use the timing decorator included
    # in indexer.util
    loopy_loop()


if __name__ == "__main__":
    main()
