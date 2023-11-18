

class ListsAVG:
    def __init__(self, first_list, second_list):
        # я добавил *для переупаковки передаваемых коллекций в формат списка для удобности

        if self.__check_collections([*first_list]):
            self.first_list = [*first_list]

        if self.__check_collections([*second_list]):
            self.second_list = [*second_list]

        print("P.S."
              "\nДанная программа обладает возможностью добавления элементов к переданным "
              "в инициализатор коллекциям с помощью метода \"add_values\""
              "\nИ конечно же сравнивания их средних значений с помощью метода \"comparing_averages\""
              "\n")

    @classmethod
    def __check_collections(cls, collection):
        # В этом методе проверяются передаваемые списки на наличие в них значений и на содержание только цифр
        if len(collection) == 0:
            raise ValueError('переданные данные не должны быть пустыми')

        if not all(isinstance(element, (int, float)) for element in collection):
            raise ValueError('переданные вами коллекции данных должны содержать либо целые либо вещественные числа')
        return True

    @staticmethod
    def __parse_arguments(args):
        # Этот метод автоматичски распознает вещественные и целые числа и возвращает список состоящий
        # из этих значений
        converted_values = []
        for value in args:
            try:
                converted_values.append(int(value))
            except ValueError:
                try:
                    converted_values.append(float(value))
                except ValueError:
                    converted_values.append(value)
        return converted_values

    def add_values(self):
        print(f'В какой список вы хотите добавить значения?'
              f'\nЕсли в {self.first_list}, то введите цифру 1'
              f'\nЕсли же в {self.second_list}, то введите цифру 2')

        user_choice = input()

        if user_choice == '1':
            second_input = input('Если вы хотите ввести 1 значение, введите цифру,'
                                 'если же несколько, то передайте их в 1 строку через пробел \n')
            if " " not in second_input:
                if '.' in second_input:
                    try:
                        self.first_list.append(float(second_input))
                    except:
                        raise ValueError(
                            'переданное вами данные должны быть либо целым либо вещественным чисом')
                    return
                else:
                    try:
                        self.first_list.append(int(second_input))
                    except:
                        raise ValueError(
                            'переданное вами данные должны быть либо целым либо вещественным чисом')
            else:
                user_list = self.__parse_arguments(second_input.split())
                if self.__check_collections(user_list):
                    self.first_list = self.first_list + user_list

        elif user_choice == '2':
            second_input = input('Если вы хотите ввести 1 значение, введите цифру,'
                                 'если же несколько, то передайте их в 1 строку через пробел \n')
            print(second_input)
            if " " not in second_input:
                if '.' in second_input:
                    try:
                        self.second_list.append(float(second_input))
                    except:
                        raise ValueError(
                            'переданное вами данные должны быть либо целым либо вещественным чисом')
                    return
                else:
                    try:
                        self.second_list.append(int(second_input))
                    except:
                        raise ValueError(
                            'переданное вами данные должны быть либо целым либо вещественным чисом')
            else:
                user_list = self.__parse_arguments(second_input.split())
                if self.__check_collections(user_list):
                    self.second_list = self.second_list + user_list
        else:
            raise ValueError(
                'Нужно было ввести либо цифру 1 либо 2')

    def comparing_averages(self):
        print(f'1 список:{self.first_list}, 2 список:{self.second_list}')
        print(f'Средние значения: {sum(self.first_list) / len(self.first_list)} | '
              f'{sum(self.second_list) / len(self.second_list)}')

        if sum(self.first_list) / len(self.first_list) > sum(self.second_list) / len(self.second_list):
            print("Первый список имеет большее среднее значение")
        if sum(self.first_list) / len(self.first_list) < sum(self.second_list) / len(self.second_list):
            print("Второй список имеет большее среднее значение")
        if sum(self.first_list) / len(self.first_list) == sum(self.second_list) / len(self.second_list):
            print("Средние значения равны")


# la = ListsAVG({1, 4, 6, 9}, {2, 3, 4, 5})
# print(la.__dict__)
# la.add_values()
# print(la.__dict__)
# la.comparing_averages()
