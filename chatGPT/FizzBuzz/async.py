import asyncio

async def fizz_buzz_for_number(number):

    # Sim placeholer for async I/O op (e.g., an HTTP request)
    await asyncio.sleep(0.01)  
    
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

async def async_fizz_buzz(range_start, range_end):
    tasks = [fizz_buzz_for_number(number) for number in range(range_start, range_end + 1)]
    completed, _ = await asyncio.wait(tasks)
    results = [task.result() for task in completed]
    return sorted(results, key=lambda x: int(x) if x.isdigit() else float('inf'))

async def main():
    results = await async_fizz_buzz(1, 100)
    print(results)

asyncio.run(main())
