"""
    리스트에 가장 많은 정수가 무엇인지 판별하기.
"""
from collections import Counter, defaultdict


# 기능이 잘 작동할 수 있게 코드 구현하기.
def get_number_with_highest_count(counts):  # <1>
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = {}
    for number in numbers:  # <2>
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return get_number_with_highest_count(counts)


# 코드를 올바르게(리팩터링) 기존의 코드를 보다 더 명확하고 잘 조정된 방식으로 다시 구현하면서 일괄된 결과를 제공하기.
def get_number_with_highest_count(counts):
    """Using defaultdict"""
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = defaultdict(int)  # <2>
    for number in numbers:
        counts[number] += 1  # <3>

    return get_number_with_highest_count(counts)


# 간결하고 명확한 코드를 위한 두 번째 리팩터링
def get_number_with_highest_count(counts):
    """Using lambda"""
    return max(counts, key=lambda x: counts[x])


def most_frequent(numbers):
    """Using Counter"""
    counts = Counter(numbers)
    return get_number_with_highest_count(counts)


# Counter 만들어보기.
def custom_counter(list_param):
    count_dict = {i: list_param.count(i) for i in list_param}
    return max(count_dict, key=lambda x: count_dict[x])


if __name__ == "__main__":
    sample_data = [1, 1, 1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 2, 1, 29]

    print("Custom Counter:", custom_counter(sample_data))
    print("Count built-in function:", most_frequent(sample_data))
