from bs4 import BeautifulSoup
from postings import Postings
from nltk import PorterStemmer

stemmer = PorterStemmer()

def buildIndex(documents):
    index = {}
    docNum = 0

    for document in documents:
        docNum = docNum + 1
        tokens = Parse(document)
        stemmedTokens = [stemmer.stem(t.lower()) for t in tokens]

        uniqueStemmedTokens = set(stemmedTokens)
        for token in uniqueStemmedTokens:
            freq = tokens.count(token)
            tempPost = Postings(docNum, freq)

            if token not in index:
                index[token] = [tempPost]
            else:
                index[token].append(tempPost)
    return index

