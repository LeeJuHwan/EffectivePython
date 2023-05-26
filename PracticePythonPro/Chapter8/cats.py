class BigCat:
    def eats(self):
        return ["rodents"]


class Lion(BigCat):
    def eats(self):
        return ["wildebeest"]
        # return super().eats() + ["wildebeest"]


class Tiger(BigCat):
    def eats(self):
        return ["water buffalo"]
        # return super().eats() + ["water buffalo"]


class Liger(Lion, Tiger):
    def eats(self):
        return super().eats() + ["rabbit",  "cow", "pig", "chicken"]


if __name__ == "__main__":
    lion = Lion()
    print("The lion eats", lion.eats())
    tiger = Tiger()
    print("The Tiger eats", tiger.eats())
    liger = Liger()
    print("The Liger eats", liger.eats())
