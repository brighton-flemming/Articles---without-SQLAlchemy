class Magazine:
    _magazines = []
    def __init__(self, id, name, category):
       self.id = id
       self._name = name
       self._category = category
       Magazine._magazines.append(self)
 
    
    def name(self):
        return self._name
    
    def category(self):
        return self._category
    
    def all():
        return Magazine._magazines

magazine1 = Magazine(1, "Tech Magazine", "Technology")
magazine2 = Magazine(2, "Science Journal", "Science")
magazine3 = Magazine(3, "Fashion Weekly", "Fashion")
magazine4 = Magazine(4, "Motor Trend", "Automobile")


print("Magazine 2's name:", magazine2.name())
print("Magazine 2's category:", magazine2.category())

all_magazines = Magazine.all()
for magazine in all_magazines:
    print("Magazine:", magazine.name(), "-Category:", magazine.category())