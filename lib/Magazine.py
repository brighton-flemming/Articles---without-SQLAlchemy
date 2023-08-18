from Author import author1, author2
class Magazine:
    _magazines = []
    def __init__(self, id, name, category):
       self.id = id
       self._name = name
       self._category = category
       self._contributors = []
       Magazine._magazines.append(self)
 
    
    def name(self):
        return self._name
    
    def category(self):
        return self._category
    
    def add_contributor(self, author):
        self._contributors.append(author)

    def contributor(self):
        return self._contributors
    
    def all():
        return Magazine._magazines

magazine1 = Magazine(1, "Tech Magazine", "Technology")
magazine2 = Magazine(2, "Science Journal", "Science")
magazine3 = Magazine(3, "Fashion Weekly", "Fashion")
magazine4 = Magazine(4, "Motor Trend", "Automobile")

magazine1.add_contributor(author1)
magazine2.add_contributor(author2)
magazine3.add_contributor(author1)
magazine4.add_contributor(author2)



print("Magazine 2's name:", magazine2.name())
print("Magazine 2's category:", magazine2.category())

all_magazines = Magazine.all()
for magazine in all_magazines:
    print("Magazine:", magazine.name(), "-Category:", magazine.category())

print("Contributors for Magazine 2: ")
for contributor in magazine2.contributors():
    print("-", contributor.name())