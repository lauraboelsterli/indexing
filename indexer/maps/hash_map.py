from indexer.abstract_index import AbstractIndex

import json 
import os 

folder_path = ["USFinancialNewsArticles-preprocessed/April2018", "USFinancialNewsArticles-preprocessed/February2018", 
               "USFinancialNewsArticles-preprocessed/January2018", "USFinancialNewsArticles-preprocessed/March2018", 
               "USFinancialNewsArticles-preprocessed/May2018"]

hashmap = {}
for folder in folder_path:
    # Loop through all files in the folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)  # Get full path of the file
        if os.path.isfile(file_path):  # Ensure it's a file and not a subdirectory
            with open(file_path, 'r') as file:  # Open the file
                data = json.load(file)  # Load the JSON data
                preprocessed_text = data.get("preprocessed_text")
                if preprocessed_text:
                    # for word in preprocessed_text:
                    hashmap[file] = preprocessed_text

print(hashmap.keys())[:5]



class HashMapIndex(AbstractIndex):
    
    def __init__(self):
        super().__init__()
        self.hash_map = {}

    def add(self, term, document_id):
        pass

    def search(self, term):
        pass

    def remove(self, term):
        pass