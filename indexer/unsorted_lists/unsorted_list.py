# from typing import Any, List
from typing import Any, List, Generator 

from indexer.abstract_index import AbstractIndex

import json
import os


class UnsortedList(AbstractIndex):
    def __init__(self):
        super().__init__()
        self.unsorted_list = []

    # def add(self, term, document_id):
    #     for i in range(len(self.unsorted_list)):
    #         if self.unsorted_list[i][0] == term:
    #             # indexing should be [i][1] instead, right? -- note by laura 
    #             if document_id not in self.unsorted_list[i][1]:
    #                 # self.unsorted_list[1][1].append(document_id)
    #                 self.unsorted_list[i][1].append(document_id)
    #             return 
    def insert(self, term, document_id):
        for i in range(len(self.unsorted_list)):
            if self.unsorted_list[i][0] == term:
                # indexing should be [i][1] instead, right? -- note by laura 
                if document_id not in self.unsorted_list[i][1]:
                    # self.unsorted_list[1][1].append(document_id)
                    self.unsorted_list[i][1].append(document_id)
                return 
            
        self.unsorted_list.append((term, [document_id]))

    def search(self, term):
        for key, value in self.unsorted_list:
            if key == term:
                return value 
        return []

    def remove(self, term):
        # create new list without term 
        self.unsorted_list = [(key, value) for key,value in self.unsorted_list if key != term]

    def __iter__(self) -> Generator[Any, None, None]:
        """
        Returns an iterator over the terms (keys) in the hash map.
        Yields each term (key) in the hash_map.
        # """
        # yield self.hash_map.keys()
        for item in self.unsorted_list:
            yield item 

        




