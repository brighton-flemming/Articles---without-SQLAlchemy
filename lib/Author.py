
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


# article1 = Article("author1", magazine1, "Introduction to ORM")
# article2 = Article("author1", magazine2, "Advances in AI")
# article3 = Article("author2", magazine3, "Exploring Quantum Computing")
# article4 = Article("author2", magazine4, "$300K 2025 Ford Mustang GTD Puts Europe's Best on Notice")

# author1.add_article(article1)
# author1.add_article(article4)
# author2.add_article(article2)
# author2.add_article(article3)

# print("Author 1's articles:")
# for article in author1.articles():
#     print("-", article.title())

# print("Author 1's articles:")
# for magazine in author1.magazines():
#     print("-", magazine.name())



print("Author's name:", author1.name())
print("Author's name:", author2.name())
