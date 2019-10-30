"""
basic parsing program for reading a text
"""

import numpy as np
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


def parse(text):
    tokens = []
    word = ""
    for i in text:
        if i.isspace():
            word = sanitize(word)
            if word != -1:
                tokens.append(word)
            word = ""
        else:
            word += i.lower()
    tokens = list(dict.fromkeys(tokens))
    return tokens


addr = ["./doc1.txt", "./doc2.txt"]
docs = []
tokens = []
for a in addr:
    file =open(a, "r")
    docs.append(file.read()+' ')

for d in docs:
    tokens.append(parse(d))

print(tokens)

index =[]

for i in range(0, len(tokens)):
    for j in range(0, len(tokens[i])):
        print(tokens[i][j])
        print(index)
        if tokens[i][j] in index:
            loc = index.index(tokens[i][j])
            index[loc] = index[loc].append(i+1)
        else:
            index.append(tokens[i][j])
            loc = index.index(tokens[i][j])
            index[loc] = index[loc].append(i+1)
for i in range(0, len(index)):
    print(index[i])

