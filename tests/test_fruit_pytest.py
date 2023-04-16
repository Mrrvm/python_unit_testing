from fruit import Fruit


class TestFruit: # class name must start with "test_"

    def test_request(self):  # method name must start with "test_"
        plum = Fruit('plum', 16, 'purple', 2)
        request = plum.request(4)
        assert "I'd like 4 purple plums" == request  # uses the built-in assert method

    def test_request_wrong_units(self):
        plum = Fruit('plum', 16, 'purple', 2)
        request = plum.request(5)
        assert "I'd like 4 purple plums" != request

    def test_pick_amount(self):
        n_apples_available = 10
        n_apples_to_pick = 9

        apple = Fruit('apple', n_apples_available, 'red', 2)  # this can go to setup...

        n_apples_picked = apple.pick_amount(n_apples_to_pick)

        assert n_apples_to_pick == n_apples_picked

    def test_pick_amount_available(self):
        n_apples_available = 10
        n_apples_to_pick = 11

        apple = Fruit('apple', n_apples_available, 'red', 2)  # this can go to setup...

        n_apples_picked = apple.pick_amount(n_apples_to_pick)

        assert n_apples_to_pick != n_apples_picked
        assert n_apples_available == n_apples_picked

    def test_calculate_price(self):
        kiwi = Fruit('kiwi', 20, 'yellow', 5)

        price = kiwi.calculate_price(3)

        assert 15 == price
