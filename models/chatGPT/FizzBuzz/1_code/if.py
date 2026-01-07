def fizz_buzz_if():
    result = []
    for number in range(1, 101):
        is_divisible_by_3 = number % 3 == 0
        is_divisible_by_5 = number % 5 == 0
        if is_divisible_by_3 and is_divisible_by_5:
            result.append("FizzBuzz")
        elif is_divisible_by_3:
            result.append("Fizz")
        elif is_divisible_by_5:
            result.append("Buzz")
        else:
            result.append(str(number))
    return result



