
import math
import string


class word_indexer():
    # constructor
    def __init__(self):
        self.word_list = set()
        self.word_count = 0

    # adds a word to our indexer if we haven't seen it
    def add_word(self, word):

        # gets the clean version of the word given
        word = clean_word( word )

        # if we haven't seen the word
        if word not in self.word_list:

            # add the clean version of the word to our set
            self.word_list.add( clean_word(word) );

            # increase word count by one
            self.word_count += 1;

    # returns the word list for use elsewhere
    def return_word_list(self):
        return self.word_list

    # used for print()
    def __repr__(self):
        # makes the output string
        output = ""
        output += "Word List:\n"
        output += "Word Count: " + str(self.word_count) + '\n'
        output += "Words: " + str(self.word_list) + '\n'

        # returns the output string
        return output

class document():
    # constructor of the document class
    def __init__(self, name=""):
        self.vector = [];
        self.inverse_index = {}
        self.name = name[ name.rfind('/') + 1 : ];
        self.word_count = 0;
        self.doc = "";
        self.word_list = []

        # if a document was passed, read the document
        if name:
            self.read_doc(name)

    # function to read a given document
    def read_doc(self, doc_title ):
        # opens the document specified
        with open(doc_title, 'r') as file:

            # for every line in the document
            for line in file:

                # add it to the doc so we can reference it later
                self.doc += line;

        # make a list of every word we have in the document
        self.word_list = [ clean_word( word ) for word in self.doc.split()] ;

        # for every word we found
        for word in self.word_list:

            # add 1 to the word count
            self.word_count += 1;


    # this builds the vector representation of the document
    def build_vector(self):
        global indexer;

        # clears vector
        self.vector = [0] * indexer.word_count

        # build word list for the document
        self.word_list = [ clean_word( word ) for word in self.doc.split()] ;

        # for every word in the indexer
        for index, word in enumerate(indexer.word_list):

            # sets that position in the vector to the number of occurances
            self.vector[index] = self.get_tf( word );

    # this builds the inverse index representation of the document
    def build_inverse_index(self):
        self.inverse_index = {}

        # for every word in our word list
        for index,word in enumerate(self.word_list):

            # if we already have the word in the inverse matrix
            if word in self.inverse_index.keys():

                # append the location to that word
                self.inverse_index[word].append(index)

            # if this is a new word
            else:

                # make a list to store all the locations of that word
                self.inverse_index[word] = [index]

    # function to get the tf of a given word in this document
    def get_tf(self, search_word):
        # if we dont have a word list, make one
        if not self.word_list: self.build_vector();

        # get the number of occurances of this word in the word list
        num_of_occurances = 0
        for word in self.word_list:
            if word == search_word:
                num_of_occurances += 1;

        # return the number of occurances
        return num_of_occurances

    # function used for print()
    def __repr__(self):
        # builds the components for printing
        self.build_vector();
        self.build_inverse_index();

        # makes print string
        output = "";
        output += "Document:\n"
        output += "Title: " + str(self.name) + '\n'
        output += "Word Count: " + str(self.word_count) + '\n'
        output += "Vectorized: " + str(self.vector) + '\n'
        output += "Inverse index: " + str(self.inverse_index) + '\n'

        # returns print string
        return output

def get_idf(doc_list, search_word):
    # gets the total number of documents
    total_num_of_docs = len(doc_list)
    num_of_docs_with_occurance = 0;

    # for every document
    for doc in doc_list:

        # if the search word is in the doc
        if search_word in doc.word_list:

            # occurances++
            num_of_docs_with_occurance += 1;

    # if there were any occurances
    if num_of_docs_with_occurance:

        # return 1 + log10 ( total / fraction  )
        return math.log10(total_num_of_docs / num_of_docs_with_occurance) + 1

    # if there was no occurances
    else:

        # return 1 + 0
        return 1

def clean_word(word):
    # word -> lowercase
    word = word.lower()

    # for every character in the word
    for char in word:

        # if the character is a punctuation
        if char in string.punctuation:

            # remove it from the word
            word = word.replace(char,'');

    # return clean word
    return word;

def parse_documents(list_of_document_names):
    global indexer;
    return_documents = []

    # for every doc in the list
    for doc in list_of_document_names:

        # create a new document object
        doc_object = document(doc);

        # opens the doc
        with open(doc, 'r') as doc_reader:

            # for every line in the doc
            for line in doc_reader:

                # adds the word to the indexer
                for word in line.split():
                    indexer.add_word(word);

                # prints the line
                print("read line: " + str(line) );

            # add the document object ot the list to return
            return_documents.append(doc_object)

    return return_documents


# initializes a word indexer.
indexer = word_indexer();

# reads the documents and builds our document objects
# parsed_documents = parse_documents(['./example_docs/doc1.txt','./example_docs/doc2.txt','./example_docs/doc3.txt'])
parsed_documents = parse_documents(['./example_docs/example1.txt','./example_docs/example2.txt'])

# prints the full word index that we have made
print(indexer)

# prints each document object we have made
for doc in parsed_documents:
    print(doc)

# printed idf for words that are in 3, 2, and 1 of the documents respectively
# print( "idf for the word Somebody: " + str( get_idf(parsed_documents,"Somebody") ) )
# print( "idf for the word spaghetti: " + str( get_idf(parsed_documents,"spaghetti") ) )
# print( "idf for the word house: " + str( get_idf(parsed_documents,"house") ) )
