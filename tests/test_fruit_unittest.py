import unittest
from fruit import Fruit


class TestFruit(unittest.TestCase):
    @classmethod
    def setUpClass(self):  # it will run once
        self.plum = Fruit('plum', 16, 'purple', 2)

    # def setUp(self):  # it will run at the start of each test
    #     self.plum = Fruit('plum', 16, 'purple', 2)

    def test_request(self):  # method name must start with "test_"
        request = self.plum.request(4)
        self.assertEqual("I'd like 4 purple plums", request)  # it has own assert methods

    def test_request_wrong_units(self):
        request = self.plum.request(5)
        self.assertNotEqual("I'd like 4 purple plums", request)

    def test_pick_amount(self):
        n_apples_available = 10
        n_apples_to_pick = 9

        apple = Fruit('apple', n_apples_available, 'red', 2)  # this can go to setup...

        n_apples_picked = apple.pick_amount(n_apples_to_pick)

        self.assertEqual(n_apples_to_pick, n_apples_picked)

    def test_pick_amount_available(self):
        n_apples_available = 10
        n_apples_to_pick = 11

        apple = Fruit('apple', n_apples_available, 'red', 2)  # this can go to setup...

        n_apples_picked = apple.pick_amount(n_apples_to_pick)

        self.assertNotEqual(n_apples_to_pick, n_apples_picked)
        self.assertEqual(n_apples_available, n_apples_picked)

    def test_calculate_price(self):
        kiwi = Fruit('kiwi', 20, 'yellow', 5)

        price = kiwi.calculate_price(3)

        self.assertEqual(15, price)


if __name__ == '__main__':
    unittest.main()
