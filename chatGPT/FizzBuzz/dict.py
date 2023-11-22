i = 15
fizzbuzz_dict = {3: "Fizz", 5: "Buzz", 15: "FizzBuzz"}
print(fizzbuzz_dict.get(15 * (i % 15 == 0) or 5 * (i % 5 == 0) or 3 * (i % 3 == 0), i))