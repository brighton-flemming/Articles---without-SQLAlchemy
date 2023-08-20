

class Author :
    def __init__(self, id, name) :
        self.id = id
        self._name = name
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        unique_magazines = set()
        for article in self._articles:
            unique_magazines.add(article.magazine())
        return list(unique_magazines)


author1 = Author(1, "Phelix Dobberman")
author2 = Author(2, "Patrick Benjamin")
author3 = Author(2, "Patrick Benjamin")
author4 = Author(2, "Patrick Benjamin")


print("Author's name:", author1.name())
print("Author's name:", author2.name())
print("Author's name:", author3.name())
print("Author's name:", author4.name())
