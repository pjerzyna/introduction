import unittest
from animal import Ability

class AbilityTestCase(unittest.TestCase):
    """testing my ability class"""

    def test_attack(self):
        my_animal = Ability("tested_animal")
        a = my_animal.attack()
        self.assertEqual(7, a)
        

if __name__ == '__main__':
    unittest.main()

#No animals were harmed ;)