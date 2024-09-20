from indexer.abstract_index import AbstractIndex

import json
import os

class HashMapIndex(AbstractIndex):
    def __init__(self):
        super().__init__()
        self.hash_map = {}

    def add(self, term, document_id):
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

folder_path = ["USFinancialNewsArticles-preprocessed/April2018", "USFinancialNewsArticles-preprocessed/February2018",
               "USFinancialNewsArticles-preprocessed/January2018", "USFinancialNewsArticles-preprocessed/March2018",
               "USFinancialNewsArticles-preprocessed/May2018"]

# hashmap = {}

# initialize the HashMapIndex class
hash = HashMapIndex()

for folder in folder_path:
    # Loop through all files in the folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)  # Get full path of the file
        if os.path.isfile(file_path):  # Ensure it's a file and not a subdirectory
            with open(file_path, 'r') as file:  # Open the file
                data = json.load(file)  
                preprocessed_text = data.get("preprocessed_text")
                if preprocessed_text:
                    # Add each word in the preprocessed text to the hash map with the filename
                    for word in preprocessed_text:
                        hash.add(word, filename) 


# first_five_keys = list(hashmap.keys())[:5]

# # Print the first 5 keys
# for key in first_five_keys:
#     print(key)
