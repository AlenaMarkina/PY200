import random

from faker import Faker
from faker_food import FoodProvider


fake = Faker()
fake.add_provider(FoodProvider)


def fake_fruit(fake_obj):
    return fake_obj.fruit()


def fake_vegetable(fake_obj):
    return fake_obj.fruit()


tasks = [fake_fruit(fake), fake_vegetable(fake)]


def gen_food():
    # food_dict = {name: food_name, price: 20.00, rating: 5.0}

    random_idx = random.randint(0, 1)

    while True:
        food_dict = {"name": tasks[random_idx],
                     "price": round(random.uniform(40, 4000), 2),
                     "rating": round(random.uniform(0, 5), 2)}
        yield food_dict


if __name__ == '__main__':
    print(next(gen_food()))
