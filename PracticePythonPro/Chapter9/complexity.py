def has_long_words(sentence):
    """긴 단어를 찾는 함수"""
    if isinstance(sentence, str):
        sentence = sentence(" ")

    for word in sentence:
        if len(word) > 10:
            return True

    return False
