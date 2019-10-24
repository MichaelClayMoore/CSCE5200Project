"""
basic parsing program for reading a text
"""
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


text = "Zorian sighed and continued pondering the advanced spell formula questions in front of him. As if the original 60 question test hadn’t been enough! Worse, Nora took a page out of Ilsa’s book and decided to test him on knowledge that he technically shouldn’t even have, because the additional questions had nothing to do with second year curriculum. Thankfully, he had actually read all 12 of her ‘recommended’ books over the course of several previous restarts, so he wasn’t completely stumped while looking at the piece of paper in front of him."
text += ' '
word = ""
tokens = []
for i in text:

    if i.isspace() :
        word = sanitize(word)
        if word != -1:
             tokens.append(word)
        word = ""
    else:
        word += i.lower()
tokens= list(dict.fromkeys(tokens))
for t in tokens:
    print(t)
