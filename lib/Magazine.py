class Magazine:
    _magazines = []
    def __init__(self, id, name, category):
       self.id = id
       self._name = name
       self._category = category
       self._articles = []
       self._contributors = []
       Magazine._magazines.append(self)
 
    
    def name(self):
        return self._name
    
    def category(self):
        return self._category
    
    def add_contributor(self, author):
        self._contributors.append(author)

    def add_article(self, article):
        self._articles.append(article)

    
    def find_by_name(cls, name):
        for magazine in cls._magazines:
            if magazine._name == name:
               return magazine
        return None
    
    def article_titles(cls, name):
        magazine = cls.find_by_name(name)
        if magazine:
            return [article.title() for article in magazine._articles]
        return []
    
    def contributing_authors(self):
      author_count = {}
      for article in self._articles:
          author_id = article.author().id
          if author_id in author_count:
              author_count[author_id] += 1
          else:
              author_count[author_id] = 1
      authors = []
      for author_id, count in author_count.items():
          if count > 2:
              authors.append(author_id)
      return authors

    def contributors(self):
        return self._contributors
    
    def all():
        return Magazine._magazines

magazine1 = Magazine(1, "Tech Magazine", "Technology")
magazine2 = Magazine(2, "Science Journal", "Science")
magazine3 = Magazine(3, "Fashion Weekly", "Fashion")
magazine4 = Magazine(4, "Motor Trend", "Automobile")



print("Magazine 4's name:", magazine4.name())
print("Magazine 4's category:", magazine4.category())

print("Magazine 3's name:", magazine3.name())
print("Magazine 3's category:", magazine3.category())

print("Magazine 1's name:", magazine1.name())
print("Magazine 1's category:", magazine1.category())

print("Magazine 2's name:", magazine2.name())
print("Magazine 2's category:", magazine2.category())

all_magazines = Magazine.all()
for magazine in all_magazines:
    print("Magazine:", magazine.name(), "-Category:", magazine.category())

print("Contributors for Magazine 2: ")
for contributor in magazine2.contributors():
    print("-", contributor.name())

print("Contributors for Magazine 3: ")
for contributor in magazine3.contributors():
    print("-", contributor.name())

print("Contributors for Magazine 4: ")
for contributor in magazine2.contributors():
    print("-", contributor.name())

print("Contributors for Magazine 1: ")
for contributor in magazine1.contributors():
    print("-", contributor.name())