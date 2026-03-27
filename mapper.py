#!/usr/bin/env python3
import sys
import os
import string

stopwords = set()
try:
    with open('stopwords.txt', 'r') as f:
        stopwords = set(word.strip().lower() for word in f)
except:
    pass

filepath = os.environ.get('mapreduce_map_input_file', 'unknown_doc.txt')
filename = os.path.basename(filepath)

for line in sys.stdin:
    line = line.translate(str.maketrans('', '', string.punctuation)).lower()
    words = line.strip().split()
    for word in words:
        if word and word not in stopwords:
            print("{}\t{}\t1".format(word, filename))
