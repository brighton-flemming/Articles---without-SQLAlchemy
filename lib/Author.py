class Author :
    def __init__(self, id, name) :
        self.id = id
        self._name = name
        self.articles = []
    def add_article(self, article):
        self.articles.append(article)
    def name(self):
        return self._name

author = Author("John Doe")

print("Author's name:", author.name())
