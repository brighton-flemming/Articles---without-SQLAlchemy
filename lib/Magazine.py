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

    def contributors(self):
        return self._contributors
    
    def all():
        return Magazine._magazines

magazine1 = Magazine(1, "Tech Magazine", "Technology")
magazine2 = Magazine(2, "Science Journal", "Science")
magazine3 = Magazine(3, "Fashion Weekly", "Fashion")
magazine4 = Magazine(4, "Motor Trend", "Automobile")

# from Author import Author

# author1 = Author(1, "Phelix Dobberman")
# author2 = Author(2, "Patrick Benjamin")

# magazine1.add_contributor(author1)
# magazine2.add_contributor(author1)
# magazine3.add_contributor(author2)
# magazine4.add_contributor(author2)

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