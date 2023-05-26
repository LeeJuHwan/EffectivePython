"""
함수형 패러다임
"""
from functools import reduce, partial

# 함수형 프로그래밍 코드.
squares = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
should = reduce(lambda x, y: x and y, [True, True, False])
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])


print(f"함수형 코드: {list(squares)}")
print(f"함수형 코드: {should}")
print(f"함수형 코드: {list(evens)}")

# 그러나, 파이썬에서 선호하는 방식
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
should = all([True, True, False])
evens = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]

print(f"파이썬 방식: {list(squares)}")
print(f"파이썬 방식: {should}")
print(f"파이썬 방식: {list(evens)}")


# partial을 이용 하여 기존 함수에 있는 인자를 수정 하기.
def pow(x, power=1):
    return x ** power


square = partial(pow, power=2)
cube = partial(pow, power=3)

