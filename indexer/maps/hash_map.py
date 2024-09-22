from indexer.abstract_index import AbstractIndex

import json
import os


class HashMapIndex(AbstractIndex):
    def __init__(self):
        super().__init__()
        self.hash_map = {}

    # def add(self, term, document_id):
    #     if term in self.hash_map:
    #         if document_id not in self.hash_map[term]:
    #             self.hash_map[term].append(document_id) 
    #     else:
    #         self.hash_map[term] = [document_id]
    def insert(self, term, document_id):
        if term in self.hash_map:
            if document_id not in self.hash_map[term]:
                self.hash_map[term].append(document_id) 
        else:
            self.hash_map[term] = [document_id]

    def search(self, term):
        return self.hash_map.get(term, [])

    def remove(self, term):
        if term in self.hash_map:
            del self.hash_map[term]


    def __iter__(self) -> Generator[BSTNode, None, None]:
            """
            Returns an iterator over the terms (keys) in the hash map.
            Yields each term (key) in the hash_map.
            """
            yield self.hash_map.keys()
    
# def insert(self, key: Any, value: Any) -> None:
#         """
#         Inserts a key-value pair into the binary search tree.

#         Parameters:
#             key (Any): The key to be inserted.
#             value (Any): The value associated with the key.

#         Returns:
#             None
#         """
#         self.root = self._insert_recursive(self.root, key, value)


# folder_path = ["USFinancialNewsArticles-preprocessed/April2018", "USFinancialNewsArticles-preprocessed/February2018",
#                "USFinancialNewsArticles-preprocessed/January2018", "USFinancialNewsArticles-preprocessed/March2018",
#                "USFinancialNewsArticles-preprocessed/May2018"]

# # initialize the HashMapIndex class
# hash = HashMapIndex()

# for folder in folder_path:
#     # Loop through all files in the folder
#     for filename in os.listdir(folder):
#         file_path = os.path.join(folder, filename)  # Get full path of the file
#         if os.path.isfile(file_path):  # Ensure it's a file and not a subdirectory
#             with open(file_path, 'r') as file:  # Open the file
#                 data = json.load(file)  
#                 preprocessed_text = data.get("preprocessed_text")
#                 if preprocessed_text:
#                     # Add each word in the preprocessed text to the hash map with the filename
#                     for word in preprocessed_text:
#                         hash.add(word, filename) 
