import unittest

class FizzBuzz():
    def __init__(self, n):
        self.n = n

    def count_fizz(self):
        counter = self.n / 3
        return counter

    def count_buzz(self):
        counter = self.n / 5
        return counter

class FizzBuzzKataTest(unittest.TestCase):
    def test_all(self):
        cases = {
            1: (0, 0),
            3: (1, 0),
            5: (1, 1),
            6: (2, 1),
            9: (3, 1),
            10: (3, 2),
            15: (5, 3)
            }
        for N, fizz_buzz in cases.items():
            fizz, buzz = fizz_buzz
            game = FizzBuzz(N)
            self.assertEqual(fizz, game.count_fizz())
            self.assertEqual(buzz, game.count_buzz())

if __name__ == "__main__":
    unittest.main()
