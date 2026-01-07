import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_if(self):
        expected_output = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", 
            "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz", 
            # ... continue this list up to 100
        ]
        self.assertEqual(fizz_buzz_if(), expected_output)

if __name__ == "__main__":
    unittest.main()