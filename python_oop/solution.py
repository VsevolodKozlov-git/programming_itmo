from random import randrange


class Node:
    def __init__(self, contained_object):
        self.contained_object = contained_object
        self.next = None

    def add_next_reference(self, ref):
        self.next = ref


class MyQueue:
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, element):
        current = Node(element)
        if self.head is None:
            self.head = current
        else:
            self.last.add_next_reference(current)
        self.last = current

    def remove(self):
        if self.head is None:
            raise Exception('queue is empty')
        head_obj = self.head.contained_object
        self.head = self.head.next
        return head_obj

    def clear(self):
        self.__init__()

    def make_array(self):
        if self.head is None:
            return []

        res = []
        current = self.head
        # using while as do until
        while True:
            res.append(current.contained_object)
            current = current.next
            if current is None:
                break
        return res


class Country:
    def __init__(self, name,  capital, population):
        self.name = name
        self.population = population
        self.capital = capital

    def __str__(self):
        return f'Country {self.name}: (population:{self.population} / capital:{self.capital})'


if __name__ == '__main__':
    # preparing of countries queue
    countries_queue = MyQueue()
    names_pool = ['Russia', 'French', 'Japan']
    capitals_pool = ['Oxenfurt', 'Novigrad', 'TIR NA LIA']
    # adding elements
    for i in range(3):
        country = Country(names_pool[i], capitals_pool[i], randrange(100, 1000))
        countries_queue.add(country)
    # output elements
    for i in range(3):
        print(countries_queue.remove())

    print('-' * 8)

    # preparing
    int_queue = MyQueue()
    numbers = [1, 2, 3]
    # adding
    for i in range(3):
        int_queue.add(numbers[i])
    # output
    for i in range(3):
        print(int_queue.remove())




