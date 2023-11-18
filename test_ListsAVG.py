import unittest
from unittest.mock import patch, Mock
from ListsAVG import ListsAVG


def get_user_input():
    return input("Введите что-то: ")


class TESTListsAVG(unittest.TestCase):

    def setUp(self) -> None:
        self.avg = ListsAVG({1, 3, 4, 9, 10}, {6.8, 3.4, 10, 12})

    def test_check_collections(self):
        # avg1 = ListsAVG({1, 3, 4, 9, 10}, {6.8, 3.4, 10, 'r'})
        with self.assertRaises(ValueError) as warning:
            ListsAVG({1, 3, 4, 9, 10}, {6.8, 3.4, 10, 'r'})
        self.assertEqual('переданные вами коллекции данных должны'
                         ' содержать либо целые либо вещественные числа',
                         warning.exception.args[0])

        with self.assertRaises(ValueError) as warning:
            ListsAVG({1, 3, 4, 9, 10}, {})
        self.assertEqual('переданные данные не должны быть пустыми',
                         warning.exception.args[0])

        with self.assertRaises(ValueError) as warning:
            ListsAVG({}, {1, 3, 4, 9, 10})
        self.assertEqual('переданные данные не должны быть пустыми',
                         warning.exception.args[0])

    @patch('builtins.input', side_effect=['1', '5.7'])
    def test_add_values_1(self, mock_inputs):
        self.avg.add_values()
        self.assertEqual(self.avg.first_list, [1, 3, 4, 9, 10, 5.7])

    @patch('builtins.input', side_effect=['2', '5.7'])
    def test_add_values_2(self, mock_inputs):
        self.avg.add_values()
        self.assertEqual(self.avg.second_list, [10, 3.4, 12, 6.8, 5.7])

    @patch('builtins.input', side_effect=['1', 'y.7'])
    def test_add_values_3(self, mock_inputs):
        with self.assertRaises(ValueError):
            self.avg.add_values()

    @patch('builtins.input', side_effect=['2', 'p.q'])
    def test_add_values_4(self, mock_inputs):
        with self.assertRaises(ValueError):
            self.avg.add_values()

    @patch('builtins.input', side_effect=['1', '-100000'])
    def test_add_values_5(self, mock_inputs):
        self.avg.add_values()
        self.assertEqual(self.avg.first_list, [1, 3, 4, 9, 10, -100000])

    @patch('builtins.input', side_effect=['2', 'asdasd'])
    def test_add_values_6(self, mock_inputs):
        with self.assertRaises(ValueError):
            self.avg.add_values()

    @patch('builtins.input', side_effect=['1', 'asdasd'])
    def test_add_values_7(self, mock_inputs):
        with self.assertRaises(ValueError):
            self.avg.add_values()

    @patch('builtins.input', side_effect=['2', '1 2 5.6 4'])
    def test_add_values_8(self, mock_inputs):
        self.avg.add_values()
        self.assertEqual(self.avg.second_list, [10, 3.4, 12, 6.8, 1, 2, 5.6, 4])

    @patch('builtins.input', side_effect=['1', '1 2 3 4'])
    def test_add_values_9(self, mock_inputs):
        self.avg.add_values()
        self.assertEqual(self.avg.first_list, [1, 3, 4, 9, 10, 1, 2, 3, 4])

    @patch('builtins.input', side_effect=['2', '1 2 qwecdcqw 4'])
    def test_add_values_10(self, mock_inputs):
        with self.assertRaises(ValueError):
            self.avg.add_values()
            self.assertEqual('переданные вами коллекции данных '
                             'должны содержать либо целые либо вещественные числа')


    @patch('builtins.input', side_effect=['1', '1 ;lsadknaa 3 4'])
    def test_add_values_11(self, mock_inputs):
        with self.assertRaises(ValueError):
            self.avg.add_values()
            self.assertEqual('переданные вами коллекции данных '
                             'должны содержать либо целые либо вещественные числа')

    @patch('builtins.input', side_effect=['2', '1 2 m.4 4'])
    def test_add_values_12(self, mock_inputs):
        with self.assertRaises(ValueError):
            self.avg.add_values()
            self.assertEqual('переданные вами коллекции данных '
                             'должны содержать либо целые либо вещественные числа')


    @patch('builtins.input', side_effect=['1', '1 o.3 3 4'])
    def test_add_values_13(self, mock_inputs):
        with self.assertRaises(ValueError):
            self.avg.add_values()
            self.assertEqual('переданные вами коллекции данных '
                             'должны содержать либо целые либо вещественные числа')

    def test_add_values_second(self):
        with self.assertRaises(ValueError) as warning:
            mock_input = Mock(return_value='3')
            with unittest.mock.patch('builtins.input', mock_input):
                self.avg.add_values()
        self.assertEqual('Нужно было ввести либо цифру 1 либо 2',
        warning.exception.args[0])

        with self.assertRaises(ValueError) as warning:
            mock_input = Mock(return_value='sdfgssfdvgsgfd')
            with unittest.mock.patch('builtins.input', mock_input):
                self.avg.add_values()
        self.assertEqual('Нужно было ввести либо цифру 1 либо 2',
        warning.exception.args[0])

    def test_comparing_averages(self):
        self.assertEqual(self.avg.comparing_averages(), None)
        a = ListsAVG((1, 2, 3, 4), (1, 2, 3, 4))
        a.comparing_averages()

        a = ListsAVG((1, 2, 3), (1, 2, 3, 4))
        a.comparing_averages()

        a = ListsAVG((1, 2, 3, 90), (1, 2, 3, 4))
        a.comparing_averages()

if __name__ == '__main__':
    unittest.main()
