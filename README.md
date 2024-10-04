[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d0clE_qN)
# DS4300 - Fall 2024 - Assignment #1 - Index It 

## Assignment Overview

Database systems use indexes to speed up retrieval operations.  In this assignment, you will implement several different in-memory indexing data structures, build indexes with them for a large corpus of documents, and analyze their relative performance with respect to searches. 

### DataSet

The input corpus is based on the [US Financial News Articles](https://www.kaggle.com/datasets/jeet2016/us-financial-news-articles) Kaggle Dataset. Each news article is in a separate JSON file containing metadata about the article as well as the full text.  The full text has been pre-processed to remove stop words, any tokens composed of only digits and decimal points, and lemmatized. 

## Steps in the Final Deliverable

1. Read in all the JSON files and extract the `preprocessed_text` element. It will contain a list of words/tokens to be indexed.  Insert each word from `preprocessed_text` into the current data structure as the key and using the filename as the value. 
1. Get a list of keys (tokens) from the index. Shuffle the resulting list. 
1. Using the list of randomized keys, perform a set of searches of increasing size, gathering execution time information for each data set. Start with ~100K and increase the size until the execution times of the set of searches against the 4 different data structures becomes significant.  

I have included a decorator in `indexer.util.timer` that tracks the execution time in nanoseconds and milliseconds.  You are free to track performance data in some other Pythonic way if you'd like.  

At the end of the experiments, you should have a table of data.  One dimension of the table will represent the 4 data structures, and the other dimension will represent the various dataset sizes for searches that you performed. 


## Implementation Details

You'll use the following data structures for this project:
- Binary Search Tree (already implemented for you)
- AVL Tree (started for you)
- Hash Table (main functions stubbed out for you)
- Unsorted List (not started)

Each data structure should conceptually manage an inverted index for the corpus. In this case, the inverted index will map individual words (after they've been preprocessed) to a list of documents in which that word appears.

## Deliverables 

- [ ] Full Python Implementation of the data structures and experiments. 
  - [ ] The code I am providing includes type hints to help you comprehend the code more quickly.  The code you add is not required to use type hints, although I recommend it for clarity. 
- [ ] Raw data collected in your experiments.  The raw data should be in one or more csv files and added to the `timing_data` folder of your repository.
- [ ] An analysis report in PDF saved in the `report` folder of the repository.

