#!/usr/bin/env python3
import sys

current_word = None
current_doc = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    try:
        word, doc, count = line.split('\t')
        count = int(count)
    except ValueError:
        continue

    if current_word == word and current_doc == doc:
        current_count += count
    else:
        if current_word:
            print("{}\t{}\t{}".format(current_word, current_doc, current_count))
        current_word = word
        current_doc = doc
        current_count = count

if current_word:
    print("{}\t{}\t{}".format(current_word, current_doc, current_count))
