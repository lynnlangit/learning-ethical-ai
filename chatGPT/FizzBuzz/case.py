# requires python3.10 or better

def fizz_buzz_match_case():
    for number in range(1, 101):
        is_divisible_by_3 = number % 3 == 0
        is_divisible_by_5 = number % 5 == 0

        match (is_divisible_by_3, is_divisible_by_5):
            case (True, True):
                print("FizzBuzz")
            case (True, False):
                print("Fizz")
            case (False, True):
                print("Buzz")
            case _:
                print(number)

# Call the function to display the output
fizz_buzz_match_case()



