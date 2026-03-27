# The Digital Librarian: Distributed Reverse Indexing

![Apache Hadoop](https://img.shields.io/badge/Apache%20Hadoop-66CC00?style=for-the-badge&logo=apachehadoop&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Project Overview
In the era of Big Data, searching through massive unstructured text corpora efficiently requires robust distributed solutions. "The Digital Librarian" is a **Distributed Reverse Indexing System**—the core foundational architecture behind modern search engines. 

By leveraging **Apache Hadoop** and **Docker**, this system ingests raw documents, distributes the workload across a cluster using the **MapReduce** paradigm, and generates a highly optimized inverted index. This index maps every unique term to its corresponding source documents, enabling rapid search and retrieval operations at scale.

## Architecture & Workflow
This project goes beyond a basic MapReduce implementation by introducing network optimization and text sanitization:

1. **Text Preprocessing:** Utilizes a `stopwords.txt` filter to remove non-informative words, ensuring the final index is dense and meaningful.
2. **Mapper Phase (`mapper.py`):** Parses documents, tokenizes text, and emits intermediate key-value pairs: `(Word, Document_ID)`.
3. **Combiner Optimization (`combiner.py`):** Acts as a local reducer. It pre-aggregates data on the mapper node before the shuffle phase, drastically reducing network bandwidth and optimizing cluster performance.
4. **Reducer Phase (`reducer.py`):** Aggregates the final word counts globally and formats the distributed reverse index.

## Repository Structure
```text
.
├── book1.txt               # Sample large text corpus 1
├── book2.txt               # Sample large text corpus 2
├── mapper.py               # Tokenizes text and removes punctuation/stop-words
├── combiner.py             # Performs local aggregation to optimize network shuffle
├── reducer.py              # Aggregates final word counts and formats output
├── stopwords.txt           # List of words to filter out during mapping
├── docker-compose.yml      # Dockerized Hadoop cluster environment setup
├── report (1).pdf          # Detailed technical project report
└── README.md               # Project documentation
