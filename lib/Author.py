class Author :
    def __init__(self, id, name) :
        self.id = id
        self._name = name
        self.articles = []
    def add_article(self, article):
        self.articles.append(article)
    def name(self):
        return self._name

author1 = Author("John Doe")
author2 = Author("Patrick Benjamin")

print("Author's name:", author1.name())
print("Author's name:", author2.name())
