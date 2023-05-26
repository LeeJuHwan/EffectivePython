"""
온라인 상점에 들어온 새로운 고객을 맞이하는 코드 - 캡슐화 중점
"""
from datetime import datetime


#1. 캡슐화를 적용 하기 전 클래스 코드.
class Greeter:
    def __init__(self, name):
        self.name = name

    def _day(self):
        return datetime.now().strftime("%A")

    def _part_of_day(self):
        now = datetime.now().hour
        if 0 > now < 12:
            return "morning"
        elif now <= 17:
            return "afternoon"
        else:
            return "evening"

    def greet(self, store):
        message = f"Hi, my name is {self.name}, and welcome to {store}!\nHow's your {self._day()} {self._part_of_day()} going?\nHere's a coupon for 20% off!"
        return message


# 2. 클래스의 캡슐화를 위해 클래스 외부에 함수 추출 후 클래스 생성 코드.
def day():
    return datetime.now().strftime("%A")


def part_of_day():
    now = datetime.now().hour
    if 0 > now < 12:
        return "morning"
    elif now <= 17:
        return "afternoon"
    else:
        return "evening"


class CapsuleGreeter:
    def __init__(self, name):
        self.name = name

    def greet(self, store):
        return f"Hi, my name is {self.name}, and welcome to {store}!\nHow's your {day()} {part_of_day()} going?\nHere's a coupon for 20% off!"


if __name__ == "__main__":
    c = CapsuleGreeter("juhwan")
    print(c.greet("Samsung"))
