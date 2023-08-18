class Magazine:
    def __init__(self, id, name):
       self.id = id
       self.name = name
       self.articles = []
       self.authors = []

    def add_article(self, article):
        self.articles.append(article)
    
    def add_article(self, author ):
        self.authors.append(author)