"""
프로그래머를 위한 파이썬 - 멤버 이름과 극단 이름을 입력 받아 문자열을 생성하기.
"""

# 1. 멤버들의 이름을 메세지 뒤에 소개 하는 코드
names = ["Larry", "Curly", "Moe"]
message = "The Three Stooges: "
for index, name in enumerate(names):
    if index > 0:
        message += ", "

    if index == len(names) - 1:
        message += "and "
    message += name
print(f"#1: {message}")


# 2. 멤버 라인업이 기존과 다르지만 라인업에 맞는 메시지를 작성 하는 코드.
names = ["Moe", "Larry", "Shemp"]
message = "The Three Stooges: "

for index, name in enumerate(names):
    if index > 0:
        message += ", "

    if index == len(names) - 1:
        message += "and "
    message += name
print(f"#2: {message}")


# 3. 위와 같이 라인업이 달라도, 반복되는 코드 사용을 줄이기 위한 도우미 함수
def introduce_stooges(names):
    function_in_message_variable = "The Three Stooges: "
    for index, name in enumerate(names):
        if index > 0:
            function_in_message_variable += ", "

        if index == len(names) - 1:
            function_in_message_variable += "and "
        function_in_message_variable += name
    print(f"#3: {function_in_message_variable}")


introduce_stooges(["Moe", "Larry", "Shemp"])
introduce_stooges(["Larry", "Curly", "Moe"])


# 4. 이번엔 극단명의 상수화를 제거하기 위한 도우미 함수의 인자값 추가
def introduce(title, names):
    message = f"{title}: "
    for index, name in enumerate(names):
        if index > 0:
            message += ", "
        if index == len(names) - 1:
            message += "and "
        message += name
    print(f"#4: {message}")


introduce("Teenage Mutant Ninja Turtles",
          ["Donatello", "Raphael", "Michelangelo", "Leonardo"])

introduce("The Chipmunks",
          ["Alvin", "Simon", "Thedore"])


# 5. 영어 문법에서 사용자를 나열 할 때 콤마와 옥스퍼드 콤마 표기법 분리
def join_names(names):
    name_string = ""

    for index, name in enumerate(names):
        if index > 0 and len(names) > 2:
            name_string += ", "
        if index > 0:
            name_string += " "
        if index == len(names) -1 and len(names) > 1:
            name_string += "and "
        name_string += name
    return name_string


def introduce(title, names):
    print(f"#5: {title}: {join_names(names)}")


introduce("Teenage Mutant Ninja Turtles",
          ["Donatello", "Raphael", "Michelangelo", "Leonardo"])

introduce("The Chipmunks",
          ["Alvin", "Simon", "Thedore"])
