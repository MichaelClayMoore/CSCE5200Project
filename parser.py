"""
basic parsing program for reading a text
"""

import numpy as np
import math

def sanitize(word):
    forbidden = ["a","an","as","but","or","and","for","is","was","be","the","so","at"]
    if word.endswith("\'s"):
        word = word[:len(word) - 2]
    if word.endswith('\'') or word.endswith('.') or word.endswith('?') or word.endswith('!') or word.endswith('\"') or word.endswith(','):
        word = word[:len(word)-1]
    if word[0] == '\'' or word[0]=='\"':
        word = word[1:]
    if word in forbidden :
        return -1
    return word


def wordcount(tokens, text):
    words = text.split()
    count = []
    for i in tokens:
        count.append(words.count(i))
    return count

def parse(text):
    tokens = text.split()

    for t in range(0, len(tokens)):
        tokens[t] = sanitize(tokens[t].lower())
    tokens = list(dict.fromkeys(tokens))
    print(tokens)
    if -1 in tokens:
        tokens.remove(-1)
    return tokens



addr = ["./example_docs/doc1.txt", "./example_docs/doc2.txt","./example_docs/doc3.txt"]
docs = []
tokens = []
counts = []
tf = []
for a in addr:
    file =open(a, "r")
    docs.append(file.read())

for d in range(0, len(docs)):
    tokens.append(parse(docs[d]))
    counts.append(wordcount(tokens[d], docs[d]))
print(counts)

index =[]
x = [""]
for i in range(0, len(tokens)):
    for j in range(0, len(tokens[i])):
        if tokens[i][j] in index:
            loc = index.index(tokens[i][j])
            x[loc] = x[loc] + " " + str(i+1)
        else:
            index.append(tokens[i][j])
            x.append("")
            loc = index.index(tokens[i][j])
            x[loc] = x[loc] + " " + str(i+1)
for i in range(0, len(index)):
    print(index[i], x[i], len(x[i]))
