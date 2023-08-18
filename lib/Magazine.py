class Magazine:
    _magazines = []
    def __init__(self, id, name, category):
       self.id = id
       self._name = name
       self._category = category
       Magazine._magazines.append(self)
       self.articles = []
       self.authors = []
    
    def name(self):
        return self._name
    
    def category(self):
        return self._category
    
    def all(cls):
        return cls._magazines

    def add_article(self, article):
        self.articles.append(article)
    
    def add_article(self, author ):
        self.authors.append(author)

magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Science Journal", "Science")
magazine3 = Magazine("Fashion Weekly", "Fashion")