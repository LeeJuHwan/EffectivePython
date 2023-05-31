import warnings
warnings.warn("Do not use this anymore!", DeprecationWarning)


class Book:
    def __init__(self, data):
        self.title = data["title"]
        self.subtitle = data["subtitle"]
        self.author = Author(self.author_data)

    @property
    def author_for_display(self):
        return self.author.for_display

    @property
    def author_for_citation(self):
        return self.author.for_citation


class Author:
    def __init__(self, author_data: dict):
        self.first_name = author_data["first_name"]
        self.last_name = author_data["last_name"]

    @property
    def for_display(self):
        return f"{self.author_data['first_name']}, {self.author_data['last_name']}"

    @property
    def for_citation(self):
        return f"{self.author_data['last_name']}, {self.author_data['first_name'][0]}"
