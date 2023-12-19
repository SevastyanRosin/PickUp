import unittest
from your_program import (create_manufacturers, create_details, create_manufacturer_details,
                         get_one_to_many, get_many_to_many, task_a2, task_a3)

class TestYourProgram(unittest.TestCase):

    def setUp(self):
        self.details = create_details()
        self.manufacturers = create_manufacturers()
        self.manufacturer_details = create_manufacturer_details()
        self.one_to_many = get_one_to_many(self.details, self.manufacturers)
        self.many_to_many = get_many_to_many(self.one_to_many, self.manufacturer_details)

    def test_get_one_to_many(self):
        expected_result = [('болт', 173, 'Ява'), ('винт', 140, 'Волга'), ('штуцер', 97, 'ВАЗ'), ('шуруп', 201, 'Тройка')]
        self.assertEqual(get_one_to_many(self.details, self.manufacturers), expected_result)

    def test_task_a2(self):
        expected_result = [('Волга', 341), ('Тройка', 341), ('Ява', 173), ('ВАЗ', 97)]
        self.assertEqual(task_a2(self.one_to_many), expected_result)

    def test_task_a3(self):
        expected_result = {'Волга': ['винт', 'шуруп'], 'Ява': ['болт'], 'ВАЗ': ['штуцер']}
        self.assertEqual(task_a3(self.many_to_many), expected_result)

if __name__ == '__main__':
    unittest.main()