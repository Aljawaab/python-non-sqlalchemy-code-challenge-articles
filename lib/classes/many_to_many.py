class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        self.author.add_article(self)
        self.magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string.")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name  # Internal attribute for storing the name
        self._articles = []  # Store articles authored by this author
        self._magazines = set()  # Store magazines the author contributed to

    @property
    def name(self):
        """Return the author's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Prevent changing the author's name after instantiation."""
        if hasattr(self, '_name'):
            raise AttributeError("Author name cannot be changed after instantiation.")
        if not isinstance(value, str) or not value:
            raise ValueError("Author name must be a non-empty string.")
        self._name = value

    def add_article(self, article):
        """Add an article and the corresponding magazine to the author's data."""
        self._articles.append(article)
        self._magazines.add(article.magazine)

    def articles(self):
        """Return all articles authored by this author."""
        return self._articles

    def magazines(self):
        """Return a list of magazines the author has contributed to."""
        return list(self._magazines)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine name must be a string.")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if value == "":
            raise ValueError("Category cannot be empty.")
        self._category = value

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        authors = set()
        for article in self._articles:
            authors.add(article.author)
        return list(authors)

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self, min_articles=2):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count >= min_articles]