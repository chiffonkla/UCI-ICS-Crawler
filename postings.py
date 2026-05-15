class Postings:
    def __init__(self, docID, frequency, fields="none"):
        self.docid = docID
        self.frequency = frequency
        self.fields = fields