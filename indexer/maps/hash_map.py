from indexer.abstract_index import AbstractIndex
from typing import Any, List, Generator 
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


    def __iter__(self) -> Generator[Any, None, None]:
            """
            Returns an iterator over the terms (keys) in the hash map.
            Yields each term (key) in the hash_map.
            # """
            # yield self.hash_map.keys()
            for key in self.hash_map:
                yield key 
    
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



