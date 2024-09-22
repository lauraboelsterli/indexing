from typing import Any, List

from indexer.abstract_index import AbstractIndex

import json
import os


class UnsortedList(AbstractIndex):
    def __init__(self):
        super().__init__()
        self.unsorted_list = []

    def add(self, term, document_id):
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
        

# folder_path = ["USFinancialNewsArticles-preprocessed/April2018", "USFinancialNewsArticles-preprocessed/February2018",
#                "USFinancialNewsArticles-preprocessed/January2018", "USFinancialNewsArticles-preprocessed/March2018",
#                "USFinancialNewsArticles-preprocessed/May2018"]


# # note: he said that we should not go through all documents with the unsorted list since it would take too long
# # so make the size of the search smaller --laura 

# # in-class clarification: tracking time to search documents not time to parse through documents -- note by laura 


# unsorted = UnsortedList()

# for folder in folder_path:
#     # Loop through all files in the folder
#     for filename in os.listdir(folder):
#         # get full path of the file
#         file_path = os.path.join(folder, filename)  
#         if os.path.isfile(file_path):  # Ensure it's a file and not a subdirectory
#             with open(file_path, 'r') as file: 
#                 data = json.load(file)  
#                 preprocessed_text = data.get("preprocessed_text")
#                 if preprocessed_text:
#                     for word in preprocessed_text:
#                         unsorted.add(word, filename) 


