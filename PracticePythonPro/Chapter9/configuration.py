import random
import json


FOODS = [
    "pizza",
    "burgers",
    "salad",
    "soup",
]


# 코드 작성 - 순환복잡도 3
# def random_food(request):
#     food = random.choice(FOODS)

#     if request.headers.get("Accept") == "application/json":
#         return json.dups({"food": food})
#     elif request.headers.get("Accept") == "application/xml":
#         return f"<response><food>{food}></food></response>"
#     else:
#         return food


# 첫번째 리팩터링 - 순환복잡도 1
# def random_food(request):
#     food = random.choice(FOODS)

#     formats = {
#         "application/json": json.dumps({"food": food}),
#         "application/xml": f"<response><food>{food}></food></response>",
#     }

#     return formats.get(request.headers.get("Acppet"), food)


# 두번째 리팩터링
def to_json(food):
    return json.dumps({"food": food})


def to_xml(food):
    return f"<response><food>{food}></food></response>"


def get_format_function(accept=None):
    formats = {
        "application/json": to_json,
        "application/xml": to_xml,
    }

    return formats.get(accept, lambda val: val)


def random_food(request):
    food = random.choice(FOODS)

    format_function = get_format_function(request.headers.get("Accpet"))
    return format_function(food)
