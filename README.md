#  Inverted Index with Python  

 A simple yet powerful Python implementation of an **Inverted Index** – the fundamental data structure behind modern **search engines** and **document retrieval systems**.  

---

##  What is an Inverted Index?  
An **inverted index** maps words (tokens) to the list of documents that contain them.  
This makes searching much faster compared to scanning entire documents sequentially.  

Think of it as the **index at the back of a book** – you look up a keyword and directly find the relevant pages.  

---

##  Features  
-  **Preprocessing**: Lowercasing + punctuation removal + tokenization.  
-  **Index Building**: Efficiently maps tokens to document IDs using `defaultdict(set)`.  
-  **Query Retrieval**: Supports multi-term queries (returns documents containing **all** terms).  
-  **Alphabetical Index Display**: Easily inspect how terms map to documents.  
-  **Interactive Mode**: Search your query against sample documents.  

---

##  Tech Stack  
- **Python**   
- **Regex (`re`)** for text preprocessing  
- **Collections (`defaultdict`)** for efficient storage  

---

##  How It Works  
1. Define your document collection (sample docs provided).  
2. Build the inverted index.  
3. Input a search query.  
4. Instantly retrieve relevant documents.  

---

##  Example  

**Sample Documents:**  
```
1: Data structures and algorithms are important for coding interviews.  
2: Inverted index is used in document retrieval systems.  
3: Python is widely used for data science and machine learning.  
4: Algorithms can be implemented in Python, Java, or C++.  
5: Retrieval of documents using inverted files is efficient.  
```  

**Query:**  
```
Enter your search query: python algorithms
```  

**Output:**  
```
--- Documents Matching Your Query ---  
Doc 4: Algorithms can be implemented in Python, Java, or C++.  
```  

---

##  Why This Project?  
This project is a **learning-friendly implementation** of search engine fundamentals.  
It’s ideal for:  
- Students exploring **Information Retrieval**.  
- Beginners in **Data Structures & Algorithms**.  
- Anyone curious about **how Google Search works under the hood**.  

---

##  Future Enhancements  
- Phrase search (multi-word exact matches).  
- Ranking results with TF-IDF.  
- Support for larger datasets & file input.  
- Performance optimizations using advanced data structures.  

---

##  Author  
Developed as a **hands-on exploration of Information Retrieval concepts** using Python.  
