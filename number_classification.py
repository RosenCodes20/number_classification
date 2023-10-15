numbers = input().split(", ")


def positive():
    return ", ".join([num for num in numbers if int(num) >= 0])


def negative():
    return ", ".join([num for num in numbers if int(num) < 0])


def even():
    return ", ".join([num for num in numbers if int(num) % 2 == 0])


def odd():
    return ", ".join([num for num in numbers if int(num) % 2 != 0])


print(f"Positive: {positive()}")
print(f"Negative: {negative()}")
print(f"Even: {even()}")
print(f"Odd: {odd()}")
