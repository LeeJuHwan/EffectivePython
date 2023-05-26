"""
문단을 문장과 토큰으로 나누기
"""
import re


# 1. 문단을 문장과 토큰으로 나누기
product_review = """This is a fine milk, but the product line appears to be limited
in avaliable colors. I could only find white."""

# sentence_pattern = re.compile(r"(.*?\.)(\s|$)", re.DOTALL)
# matches = sentence_pattern.findall(product_review)
# sentences = [match[0] for match in matches]

# word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
# for sentence in sentences:
#     matches = word_pattern.findall(sentence)
#     words = [match[0] for match in matches]
#     print(words)


# 2. 리팩터링된 문장 파싱
def get_matches_for_pattern(pattern, string):
    matches = pattern.findall(string)
    return [match[0] for match in matches]


sentence_pattern = re.compile(r"(.*?\.)(\s|$)", re.DOTALL)
sentences = get_matches_for_pattern(
    sentence_pattern, product_review
    )

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    words = get_matches_for_pattern(
        word_pattern, sentence
    )
    print(words)
