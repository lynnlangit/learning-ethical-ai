def fizz_buzz_if():
    for number in range(1, 101):
        is_divisible_by_3 = number % 3 == 0
        is_divisible_by_5 = number % 5 == 0
        #change to if statement
        if is_divisible_by_3 and is_divisible_by_5:
            print("FizzBuzz")
        elif is_divisible_by_3:
            print("Fizz")
        elif is_divisible_by_5:
            print("Buzz")
        else:
            print(number)

# Call the function to display the output
fizz_buzz_if()



