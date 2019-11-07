"""
basic parsing program for reading a text
"""

import numpy as np
import math

def sanitize(word):
    #forbidden = ["a","an","as","but","or","and","for","is","was","be","the","so","at"]
    if word.endswith("\'s"):
        word = word[:len(word) - 2]
    if word.endswith('\'') or word.endswith('.') or word.endswith('?') or word.endswith('!') or word.endswith('\"') or word.endswith(','):
        word = word[:len(word)-1]
    if word[0] == '\'' or word[0]=='\"':
        word = word[1:]
    #if word in forbidden :
     #   return -1
    return word


def termfrequency(index, docs):
    tf = [None] * len(docs)
    #print(index)
    for d in range(0,len(docs)):
        words = docs[d].split()
        for w in range(0,len(words)):
            words[w] = sanitize(words[w].lower())
     #   print(words)
        tf[d] = []
        for i in range(0,len(index)):

            count = words.count(index[i])
            if count == 0:
                tf[d].append(0)
            else:
                log = 1 + math.log(count,10)

                tf[d].append(log)
    return tf

def docfrequency(count,N):
    idf = []

    for y in range(0,len(count[0])):
        df = 0
        for x in range(0,len(count)):
            if count[x][y] != 0:
                df += 1
        idf.append(round(math.log((N/df), 10),3))
    print(idf)
    return idf

def parse(text):
    tokens = text.split()
    for t in range(0, len(tokens)):
        tokens[t] = sanitize(tokens[t].lower())
    tokens = list(dict.fromkeys(tokens))
    print(tokens)
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

print(tokens)
index = []
for i in range(0, len(tokens)):
    for j in range(0, len(tokens[i])):
        if tokens[i][j] not in index:
            index.append(tokens[i][j])

tf = termfrequency(index, docs)
print(tf)
idf = docfrequency(tf,len(docs))