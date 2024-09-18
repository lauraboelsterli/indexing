from typing import Any, List

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
                    hashmap[file] = preprocessed_text


class UnsortedList(AbstractIndex):
    def __init__(self):
        super.__init__()
        self.unsorted_list = []

    def add(self, term, document_id):
        for i in range(len(self.unsorted_list)):
            if self.unsorted_list[i][0] == term:
                if document_id not in self.unsorted_list[1][1]:
                    self.unsorted_list[1][1].append(document_id)
                return

        self.unsorted_list.append((term, [document_id]))

    def search(self, term):
        for key, value in self.unsorted_list:
            if key == term:
                return value
        return []

    def remove(self, term):
        self.unsorted_list = [(key, value) for key,value in self.unsorted_list if key != term]