from indexer.abstract_index import AbstractIndex
from typing import Any, List, Generator


class HashMapIndex(AbstractIndex):
    def __init__(self):
        super().__init__()
        self.hash_map = {}

    def insert(self, term, document_id):
        if term not in self.hash_map:
            self.hash_map[term] = set()  
        self.hash_map[term].add(document_id)

    def search(self, term):
        return list(self.hash_map.get(term, []))  # Return a list of document IDs

    def remove(self, term):
        if term in self.hash_map:
            del self.hash_map[term]

    def __iter__(self) -> Generator[Any, None, None]:
        yield from self.hash_map




