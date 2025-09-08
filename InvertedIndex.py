import re
from collections import defaultdict


# Function to preprocess text (Lowercasing, removing punctuation)
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # remove punctuation
    return text.split()  # split into words


# Function to build the inverted index
def build_inverted_index(documents):
    index = defaultdict(set)
    for doc_id, content in documents.items():  # for each document
        tokens = preprocess(content)
        for token in tokens:
            index[token].add(doc_id)
    return index


# Function to print the inverted index in alphabetical order
def print_inverted_index(index):
    print("\n--- Inverted Index ---")
    for term in sorted(index.keys()):
        print(f"{term} --> {sorted(index[term])}")


# Function to retrieve documents based on query
# Finds documents that contain all query terms
def retrieve_documents(query, index):
    tokens = preprocess(query)
    result_docs = None

    for token in tokens:
        if token not in index:
            return set()  # If any token not found, return empty set
        if result_docs is None:
            result_docs = index[token]
        else:
            result_docs = result_docs.intersection(index[token])

    return result_docs if result_docs else set()


# Main program
if __name__ == "__main__":
    # Sample input documents
    documents = {
        1: "Data structures and algorithms are important for coding interviews.",
        2: "Inverted index is used in document retrieval systems.",
        3: "Python is widely used for data science and machine learning.",
        4: "Algorithms can be implemented in Python, Java, or C++.",
        5: "Retrieval of documents using inverted files is efficient."
    }

    # Step 1: Build index
    inverted_index = build_inverted_index(documents)

    # Step 2: Print the inverted index
    print_inverted_index(inverted_index)

    # Step 3: Get user query and perform retrieval
    query = input("\nEnter your search query: ")
    matched_docs = retrieve_documents(query, inverted_index)

    # Step 4: Print matched documents
    if matched_docs:
        print("\n--- Documents Matching Your Query ---")
        for doc_id in sorted(matched_docs):
            print(f"Doc {doc_id}: {documents[doc_id]}")
    else:
        print("\nNo documents matched your query.")