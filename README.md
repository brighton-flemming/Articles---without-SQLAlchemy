# Articles---without-SQLAlchemy

# Magazine Article Management System
This project implements a simple Magazine Article Management System using Python classes. It allows you to define and interact with Authors, Magazines, and Articles, demonstrating object relationships, associations, and aggregate methods.

# Features
Define and manage Authors, Magazines, and Articles.
Establish relationships between Authors and Articles, and between Magazines and Articles.
Retrieve information about Authors, Magazines, and Articles.
Implement aggregate methods to gather data from related objects.
Getting Started
# Prerequisites
Python 3.x
No additional dependencies required.
# Installation
Clone this repository:
Copy code
git clone git@github.com:brighton-flemming/Articles---without-SQLAlchemy.git
cd Articles---without-SQLAlchemy
# Usage
Define Authors, Magazines, and Articles by creating instances of the respective classes.
Associate Authors with Articles and Magazines with Articles using the appropriate methods.
Utilize the defined methods to retrieve information about Authors, Magazines, and Articles.
# Classes and Methods
 # ~Author Class
Author.__init__(id, name): Initialize an Author with an ID and name.
Author.add_article(magazine, title): Associate an Article with the Author.
Author.name(): Get the name of the Author.
Author.articles(): Get a list of Articles written by the Author.
Author.topic_areas(): Get a unique list of categories of magazines the Author has contributed to.

# ~Magazine Class
Magazine.__init__(id, name, category): Initialize a Magazine with an ID, name, and category.
Magazine.find_by_name(name): Find the first magazine with a given name.
Magazine.article_titles(): Get a list of article titles for a magazine.
Magazine.contributing_authors(): Get a list of authors who have written more than 2 articles for the magazine.
Magazine.name(): Get the name of the Magazine.
Magazine.category(): Get the category of the Magazine.
Magazine.add_contributor(author): Associate an Author with the Magazine.

# ~Article Class
Article.__init__(author, id, magazine, title): Initialize an Article with an Author, ID, Magazine, and title.
Article.title(): Get the title of the Article.
Article.author(): Get the Author of the Article.
Article.magazine(): Get the Magazine of the Article.
Article.all(): Get a list of all Article instances.
# Examples
Check the provided code files main.py, Author.py, Magazine.py, and Article.py for usage examples.

# Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

