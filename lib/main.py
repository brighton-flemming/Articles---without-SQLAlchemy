from Author import Author
from Magazine import Magazine
from Article import Article, article1, article2, article3, article4

def add_article(self, magazine, article, title):
        article = Article(self, magazine, title)
        self._articles.append(article)

author1 = Author(1, "Phelix Dobberman")
author2 = Author(2, "Patrick Benjamin")
author3 = Author(2, "Sheldon Cooper")
author4 = Author(2, "Fredrick Lumbard")

magazine1 = Magazine(1, "Tech Magazine", "Technology")
magazine2 = Magazine(2, "Science Journal", "Science")
magazine3 = Magazine(3, "Fashion Weekly", "Fashion")
magazine4 = Magazine(4, "Motor Trend", "Automobile")

magazine1.add_contributor(author1)
magazine2.add_contributor(author1)
magazine3.add_contributor(author2)
magazine4.add_contributor(author2)

article1 = Article("author1", 1, magazine1, "Introduction to ORM")
article2 = Article("author1", 2, magazine2, "Advances in AI")
article3 = Article("author2", 3, magazine3, "Exploring Quantum Computing")
article4 = Article("author2", 4, magazine4, "$300K 2025 Ford Mustang GTD Puts Europe's Best on Notice")

author1.add_article(article1)
author1.add_article(article4)
author2.add_article(article2)
author2.add_article(article3)

print("Author 1's articles:")
for article in author1.articles():
    print("-", article.title())

print("Author 2's articles:")
for magazine in author2.magazines():
    print("-", magazine.name())

print("Author 3's articles:")
for magazine in author3.magazines():
    print("-", magazine.name())

print("Author 4's articles:")
for magazine in author4.magazines():
    print("-", magazine.name())

all_magazines = Magazine.all()
for magazine in all_magazines:
    print("Magazine:", magazine.name(), "-Category:", magazine.category())

print("Contributors for Magazine 2: ")
for contributor in magazine2.contributors():
    print("-", contributor.name())

print("Contributors for Magazine 1: ")
for contributor in magazine1.contributors():
    print("-", contributor.name())

print("Contributors for Magazine 3: ")
for contributor in magazine3.contributors():
    print("-", contributor.name())

print("Contributors for Magazine 4: ")
for contributor in magazine2.contributors():
    print("-", contributor.name())

all_articles = Article.all()
for article in all_articles:
    print("Article:", article.title(), "-Author:", article.author(), "-Magazine:", article.magazine())
