class Bird:
    def fly(self):
        print("Flying!")


class Hummingbird(Bird):
    def fly(self):
        print("zzzzzooommm!")


class Penguin(Bird):
    """클래스를 상속 받았지만, 날지 못하는 경우 일 때 오버라이딩을 적용하는 예시 클래스."""
    def fly(self):
        print("no can do.")
