from concurrent.futures import ThreadPoolExecutor, as_completed

def fizz_buzz_for_number(number):
    is_divisible_by_3 = number % 3 == 0
    is_divisible_by_5 = number % 5 == 0

    if is_divisible_by_3 and is_divisible_by_5:
        return "FizzBuzz"
    elif is_divisible_by_3:
        return "Fizz"
    elif is_divisible_by_5:
        return "Buzz"   
    else:
        return str(number)

def parallel_fizz_buzz(range_start, range_end, num_workers=10):
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        
        # Map each number to the fizz_buzz_for_number function
        future_to_num = {executor.submit(fizz_buzz_for_number, num): num for num in range(range_start, range_end + 1)}
        results = []

        for future in as_completed(future_to_num):
            results.append(future.result())

    # Sort results based on original number order
    return sorted(results, key=lambda x: int(x) if x.isdigit() else float('inf'))

results = parallel_fizz_buzz(1, 100)
print(results)
