def careful_divide(a: float, b: float) -> int:
    try:
        print(type(a))
        print(type(b))
        return a / b
    except ZeroDivisionError:
        raise ValueError("잘못된 입력")


x, y = 5, 2
result = careful_divide(x, y)

print(result)
