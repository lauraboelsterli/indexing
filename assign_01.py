
import json
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
from indexer.abstract_index import AbstractIndex

def index_files(path: str, index: AbstractIndex) -> None:
    # path should contain the location of the news articles you want to parse
    if path is not None:
        print(f'path = {path}')
    
    # a sample json news article.  assume this is in a file named sample.json
    sample_filename = "sample.json"
    sample_json = '''
        {
            "title": "Some article",
            "text": "here is the text of a sample news article",
            "preprocessed_text": ["here", "text", "sample", "news", "article"]
        }
    '''
    
    # extract the preprocessed_text words and add them to the index with
    # sample.json as the file name
    the_json = json.loads(sample_json)
    words = the_json["preprocessed_text"]
    
    for word in words:
        index.insert(word, sample_filename)
        
@timer
def loopy_loop():
    total = sum((x for x in range(0, 1000000)))


def main():
    # You'll need to change this to be the absolute path to the root folder
    # of the dataset
    data_directory = "/location/of/downloaded/dataset/of/newsarticles"
       
    # Here, we are creating a sample binary search tree index 
    # and sending it to the index_files function
    bst_index = BinarySearchTreeIndex()    
    index_files(data_directory, bst_index)
    
    # As a gut check, we are printing the keys that were added to the 
    # index in order. 
    print(bst_index.get_keys_in_order())
    
    
    # quick demo of how to use the timing decorator included
    # in indexer.util
    loopy_loop()


if __name__ == "__main__":
    main()
