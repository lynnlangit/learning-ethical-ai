import unittest
import asyncio
from FizzBuzz import async_fizz_buzz  

class TestAsyncFizzBuzz(unittest.IsolatedAsyncioTestCase):
    async def test_fizz(self):
        results = await async_fizz_buzz(1, 100)
        # Test for the first multiple of 3 that's not a multiple of 5
        self.assertEqual(results[2], "Fizz")

    async def test_buzz(self):
        results = await async_fizz_buzz(1, 100)
        # Test for the first multiple of 5 that's not a multiple of 3
        self.assertEqual(results[4], "Buzz")

    async def test_fizzbuzz(self):
        results = await async_fizz_buzz(1, 100)
        # Test for the first multiple of both 3 and 5
        self.assertEqual(results[14], "FizzBuzz")

    async def test_number(self):
        results = await async_fizz_buzz(1, 100)
        # Test for a number that's not a multiple of 3 or 5
        self.assertEqual(results[0], "1")

if __name__ == '__main__':
    unittest.main()
