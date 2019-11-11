
import math
import string
import json


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
            print("adding word: ", word)
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
        self.vec_len = 0;

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
        self.word_count = len( self.word_list )


    def read_doc_from_text(self, doc_text):
        # splits the text by lines
        lines = doc_text.split('\n');

        # for every line in the document
        for line in lines:
            # add it to the doc so we can reference it later
            self.doc += line + '\n';

        # make a list of every word we have in the document
        self.word_list = [ clean_word( word ) for word in self.doc.split()] ;

        # for every word we found
        self.word_count = len( self.word_list )

    # this builds the vector representation of the document
    def build_vector(self):
        global indexer, db;

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

    def set_title(self, title):
        self.name = title

    def set_vec_len(self, length):
        self.vec_len = length;

    # function to get the tf of a given word in this document
    def get_tf(self, search_word):
        # if we dont have a word list, make one
        if not self.word_list: self.build_vector();

        # get the number of occurances of this word in the word list
        num_of_occurances = 0
        for word in self.word_list:
            if word == search_word:
                num_of_occurances += 1;

        # return the frequency 1 + log( num_of_occurances )
        if num_of_occurances == 0:
            return 0.0
        else:
            return 1 + math.log10(num_of_occurances)

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

    def serialize(self):
        # builds the components for printing
        self.build_vector();
        self.build_inverse_index();

        return dict({
            'name':self.name,
            'text':self.doc,
            'word_list':self.word_list,
            'word_count':self.word_count,
            'vector':self.vector,
            'inverse_index':self.inverse_index
        })

class DocumentDatabase():
    def __init__(self):
        self.documents = [];

    def get_idf(self, search_word):
        doc_list = self.documents
        # gets the total number of documents
        total_num_of_docs = len(doc_list)
        num_of_docs_with_occurance = 0;

        # gets the total number of occurances in all the docs
        num_of_docs_with_occurance = sum( [ ( clean_word( search_word ) in doc.word_list) for doc in doc_list ] )

        # if there were any occurances
        if num_of_docs_with_occurance:
            # return log10 ( total / fraction  )
            return math.log10(total_num_of_docs / num_of_docs_with_occurance)

        # if there was no occurances
        else:
            # return 0
            return 0.0

    def get_tf_idf(self, document, search_word):
        tf = document.get_tf(search_word)
        idf = self.get_idf(search_word)
        return tf * idf

    def add_documents(self, list_of_docs):
        self.documents += list_of_docs

    def parse_document_by_text(self, lines_of_text):
        global indexer;
        return_document = document();

        lines = lines_of_text.split('\n')

        for line in lines:

            # adds the word to the indexer
            for word in line.split():
                indexer.add_word(word);

        # add the document object ot the list to return
        return_document.read_doc_from_text(lines_of_text);

        self.add_documents([return_document])
        return return_document

    def parse_documents(self, list_of_document_names):
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


        self.add_documents(return_documents)
        return return_documents

    def parse_document_object(self, doc_object_given):
        try:
            global indexer;
            return_document = document()
            return_document.set_title(doc_object_given['name'])


            # for every line in the doc
            for word in doc_object_given['text'].split():
                indexer.add_word(word);

            return_document.read_doc_from_text(doc_object_given['text']);
            self.add_documents( [return_document] )
            return "Success"
        except:
            return "error"


    def query_for_doc(self, query):
        # setting up query as document
        query_doc = document();
        query_doc.read_doc_from_text(query);
        query_doc.set_title("query")
        print(query_doc)
        scores = []

        # gets length of query
        q_len = self.get_len_of_doc_vec(query_doc);
        if q_len == 0:
            scores += [{
                'document': doc.serialize(),
                'score': ( 0 )
            } for doc in self.documents]

        else:
            for doc in self.documents:
                running = 0;

                for word in set(query_doc.word_list):
                    q_tf_idf = self.get_tf_idf(query_doc, word)
                    d_tf_idf = self.get_tf_idf(doc, word)

                    print( "{}:{} -> {} * {}".format(doc.name,word,q_tf_idf,d_tf_idf) )

                    running += (q_tf_idf * d_tf_idf)

                d_len = self.get_len_of_doc_vec(doc);


                scores.append({
                    'document': doc.serialize(),
                    'score': (running / ( q_len * d_len ) )
                })


        scores.sort(key = lambda el: el['score'], reverse=True);
        return json.dumps( scores );

    def get_len_of_doc_vec(self, doc):
        running = 0;
        for word in set(doc.word_list):
            tf_idf = self.get_tf_idf(doc, word)
            running += (tf_idf ** 2)

        return math.sqrt(running)

    def return_documents(self):
        docs = json.dumps( [ doc.serialize() for doc in self.documents ] )
        print("returning docs: ", docs)
        return docs

# initializes a word indexer.
indexer = word_indexer();

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

# db = DocumentDatabase();
#
# # reads the documents and builds our document objects
# parsed_documents = db.parse_documents(['./example_docs/doc1.txt','./example_docs/doc2.txt','./example_docs/doc3.txt'])
#
# # prints the full word index that we have made
# print(indexer)
#
# # prints each document object we have made
# for doc in parsed_documents:
#     print(doc)
#
# # printed idf for words that are in 3, 2, and 1 of the documents respectively
# # print( "idf for the word Somebody: " + str( db.get_idf("somebody") ) )
# # print( "idf for the word spaghetti: " + str( db.get_idf("spaghetti") ) )
# # print( "idf for the word die: " + str( db.get_idf("die") ) )
# # print( "tf-idf for the word Somebody in doc 1   : " + str( db.get_tf_idf(db.documents[0],"somebody") ) )
# # print( "tf-idf for the word spaghetti in doc 1  : " + str( db.get_tf_idf(db.documents[0],"spaghetti") ) )
# # print( "tf-idf for the word die in doc 1        : " + str( db.get_tf_idf(db.documents[0],"die") ) )
# # print( "tf-idf for the word Somebody in doc 2   : " + str( db.get_tf_idf(db.documents[1],"somebody") ) )
# # print( "tf-idf for the word spaghetti in doc 2  : " + str( db.get_tf_idf(db.documents[1],"spaghetti") ) )
# # print( "tf-idf for the word die in doc 2        : " + str( db.get_tf_idf(db.documents[1],"die") ) )
# # print( "tf-idf for the word Somebody in doc 3   : " + str( db.get_tf_idf(db.documents[2],"somebody") ) )
# # print( "tf-idf for the word spaghetti in doc 3  : " + str( db.get_tf_idf(db.documents[2],"spaghetti") ) )
# # print( "tf-idf for the word die in doc 3        : " + str( db.get_tf_idf(db.documents[2],"die") ) )
#
# print('\n')
#
# test = db.parse_document_by_text("the \n final \n count \n down \n somebody somebody die spaghetti");
# print(test);
#
#
# print(db.documents[1])
#
# results = db.query_for_doc("somebody spaghetti");
#
# for res in results:
#     print("result: ")
#     print(res['document'])
#     print("score: ", res['score'])
#     print('\n')
