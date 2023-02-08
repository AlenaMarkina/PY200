import unittest
import coverage
from main import Pet


class TestPet(unittest.TestCase):

    def setUp(self):
        self.cat = Pet(type_of_animal="Кошка", energy=80, satiety=90, name="Dilma", pet_breed="Siberian cat")

    def tearDown(self) -> None:
        self.cat = None

    def test_get_price_of_pet_food(self):
        self.assertEqual(self.cat.get_price_of_pet_food(weight=0.3, price=800), 240)

        with self.assertRaises(TypeError):
            self.cat.get_price_of_pet_food(weight='0.3', price=800)

        with self.assertRaises(ValueError):
            self.cat.get_price_of_pet_food(weight=-1, price=800)

    def test_play(self):
        with self.assertRaises(TypeError):
            self.cat.play(energy_loss=30, satiety_loss="20")


if __name__ == '__main__':
    unittest.main()
