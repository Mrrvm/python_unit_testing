from fruit import Fruit
from walk import Walk

MARKET_DISTANCE = 30
GRAPE_NAME = 'grape'
GRAPE_COLOR = 'green'
GRAPES_IN_MARKET = 9
GRAPE_PRICE_PER_UNIT = 2
APPLE_NAME = 'apple'
APPLE_COLOR = 'red'
APPLES_IN_MARKET = 14
APPLE_PRICE_PER_UNIT = 1


class MakeFruitSalad:
    def __init__(self, my_location):
        self.my_location = my_location
        self.walk = Walk(self.my_location)
        self.grape = Fruit(GRAPE_NAME, GRAPES_IN_MARKET, GRAPE_COLOR, GRAPE_PRICE_PER_UNIT)
        self.apple = Fruit(APPLE_NAME, APPLES_IN_MARKET, APPLE_COLOR, APPLE_PRICE_PER_UNIT)

        self.n_grapes = 0
        self.n_apples = 0
        self.price = 0

    def get_ingredients(self, number_of_grapes, number_of_apples):

        # walk till market
        self.walk.walk_distance(MARKET_DISTANCE)

        # pick amount of grapes
        self.n_grapes = self.grape.pick_amount(number_of_grapes)
        # pick amount of apples
        self.n_apples = self.apple.pick_amount(number_of_apples)

        # request grapes
        print(self.grape.request(self.n_grapes))
        # request apples
        print(self.apple.request(self.n_apples))

        # calculate total price
        self.price = self.apple.calculate_price(self.n_apples) + self.grape.calculate_price(self.n_grapes)

        # walk back home
        self.walk.walk_distance(-MARKET_DISTANCE)
        return

    def join_ingredients(self):
        return

    def serve_salad(self):
        return


if __name__ == '__main__':
    fruit_salad = MakeFruitSalad(0)
    fruit_salad.get_ingredients(4, 5)
