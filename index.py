from bs4 import BeautifulSoup
from collections import Counter
from parse_document import Parse
from nltk.stem import PorterStemmer
from postings import Postings

stemmer = PorterStemmer()

def buildIndex(documents):
    index = {}
    docNum = -1

    for document in documents:
        docNum = docNum + 1
        tokens = Parse(document)
        stemmedTokens = [stemmer.stem(t.lower()) for t in tokens]

        counts = Counter(stemmedTokens)
        for token, freq in counts.items():
            tempPost = Postings(docNum, freq)

            if token not in index:
                index[token] = [tempPost]
            else:
                index[token].append(tempPost)
    return index
