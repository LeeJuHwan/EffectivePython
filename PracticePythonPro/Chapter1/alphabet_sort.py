"""
프로그래머를 위한 파이썬 - 미국 주의 수도를 알파벳순으로 정렬하기.

책에서 설명하는 리팩터링 과정
1. 구현이 가능한 코드 작성
2. 반복되는 내용 제거를 위한 도우미 함수 작성
3. 간결하고 재사용성이 가능한 코드 작성
-------------------------------
4. 과연 나였더라면 같은 상황에서 어떻게 코드를 작성 할 것인가?
"""

# 1. 구현이 가능한 코드 작성
us_capitals_by_state = {
    "Alabama": "Montgomery",
    "Alask": "Juneau",
}
capitals = us_capitals_by_state.values()
print(f"#1: {sorted(capitals)}")


# 2. 반복되는 내용 제거를 위한 도우미 함수 작성
def get_united_stats_capitals():
    _us_capitals_by_state = {
        "Alabama": "Montgomery",
        "Alask": "Juneau",
    }
    _capitals = _us_capitals_by_state.values()
    return sorted(_capitals)


print(f"#2: {get_united_stats_capitals()}")


# 3. 간결하고 재사용성이 가능한 코드 작성
US_CAPITALS_BY_STATE = {
    "Alabama": "Montgomery",
    "Alask": "Juneau",
}
US_CAPITALS = sorted(US_CAPITALS_BY_STATE.values())
print(f"#3: {US_CAPITALS}")


# 4. 만약 나였더라면 사용 했을 방법
copy_us_capitals_by_state = {
    "Alabama": "Montgomery",
    "Alask": "Juneau",
}

print(f"#4: {sorted(list(copy_us_capitals_by_state.values()))}")
