
# from Magazine import Magazine
# from Article import Article
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



# magazine1 = Magazine(1, "Tech Magazine")
# magazine2 = Magazine(2, "Science Journal")
# magazine3 = Magazine(3, "Fashion Weekly", "Fashion")
# magazine4 = Magazine(4, "Motor Trend", "Automobile")


author1 = Author(1, "Phelix Dobberman")
author2 = Author(2, "Patrick Benjamin")
author3 = Author(2, "Patrick Benjamin")
author4 = Author(2, "Patrick Benjamin")


print("Author's name:", author1.name())
print("Author's name:", author2.name())
print("Author's name:", author3.name())
print("Author's name:", author4.name())
