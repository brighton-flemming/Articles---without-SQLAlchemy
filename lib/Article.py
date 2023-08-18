from Magazine import magazine1, magazine2, magazine3

class Article :
    def __init__(self, id, title, author, magazine) :
        self.id = id
        self._title = title
        self._author = author
        self._magazine = magazine
        Article.article.append(self)
    
    def title(self):
        return self._title
    
    def author(self):
        return self._author
    
    def magazine(self):
        return self._magazine
    
    def all(cls):
        return cls._articles
    

article1 = Article("author1", magazine1, "Introduction to ORM")
article2 = Article("author1", magazine2, "Advances in AI")
article3 = Article("author2", magazine3, "Exploring Quantum Computing")

print("Article 1's title:", article1())

all_articles = Article.all()
for article in all_articles:
    print("Article:", article.title(), "-Author:", article._author(), "-Magazine:", article._magazine())