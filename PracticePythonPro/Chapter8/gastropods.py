"""상속의 규칙과 예외"""
class Slug:
    def __init__(self, name):
        self.name = name

    def crawl(self):
        print("slime trail!")


class Snail(Slug):
    def __init__(self, name, shell_size):
        super().__init__(name)
        self.name = name
        self.shell_size = shell_size


def race(gastropod_one, gastropod_two):
    gastropod_one.crawl()
    gastropod_two.crawl()


race(Slug("Geoffey"), Slug("Romona"))
race(Snail("Geoffey"), Snail("Romona"))
