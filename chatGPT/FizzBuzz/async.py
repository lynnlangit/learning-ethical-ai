import asyncio

async def fizz_buzz_for_number(number):
    # Simulate an I/O operation (e.g., an HTTP request)
    await asyncio.sleep(0.01)  # Sleep is just a placeholder for an actual async I/O operation
    
    is_divisible_by_3 = number % 3 == 0
    is_divisible_by_5 = number % 5 == 0

    match (is_divisible_by_3, is_divisible_by_5):
        case (True, True):
            return "FizzBuzz"
        case (True, False):
            return "Fizz"
        case (False, True):
            return "Buzz"
        case _:
            return str(number)

async def async_fizz_buzz(range_start, range_end):
    tasks = [fizz_buzz_for_number(number) for number in range(range_start, range_end + 1)]
    completed, _ = await asyncio.wait(tasks)
    results = [task.result() for task in completed]
    return sorted(results, key=lambda x: int(x) if x.isdigit() else float('inf'))

# Run the async FizzBuzz function
async def main():
    results = await async_fizz_buzz(1, 100)
    print(results)

asyncio.run(main())
