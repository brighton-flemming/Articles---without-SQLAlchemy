class Author :
    def __init__(self, id, name) :
        self.id = id
        self.name = name
        self.articles = []
    def add_article(self, article):
        self.articles.append(article)