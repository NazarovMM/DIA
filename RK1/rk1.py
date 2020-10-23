from operator import itemgetter


class Book:
    """Книга"""

    def __init__(self, id, title, autor, price, store_id):
        self.id = id
        self.title = title
        self.autor = autor
        self.price = price
        self.store_id = store_id


class Store:
    """Книжный магазин"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookStore:
    """'Книги книжного магазина' для реализации связи многие-ко-многим"""

    def __init__(self, store_id, book_id):
        self.store_id = store_id
        self.book_id = book_id


# Книжные магазины
stores = [
    Store(1, 'Читай-город'),
    Store(2, 'Книжный лабиринт'),
    Store(3, 'Московский Дом Книг'),
]

# Книги
books = [
    Book(1, 'Война и мир Том 1-2', 'Толстой', 110, 1),
    Book(2, 'Фицджеральд', 'Скотт', 138, 2),
    Book(3, '451 по Фаренгейту', 'Брэдбери', 217, 3),
    Book(4, '1984', 'Оруэлл', 196, 1),
    Book(5, 'Мы', 'Замятин', 138, 2),
    Book(6, 'Война и мир Том 3-4', 'Толстой', 119, 3),
]

store_book = [
    BookStore(1, 1),
    BookStore(2, 2),
    BookStore(3, 3),
    BookStore(1, 4),
    BookStore(2, 5),
    BookStore(3, 6)
]


def main():
    """Основная функция"""

    one_to_many = [(b.title, b.price, s.name)
                   for s in stores
                   for b in books
                   if b.store_id == s.id]

    many_to_many_temp = [(s.name, bs.store_id, bs.book_id)
                         for s in stores
                         for bs in store_book
                         if s.id == bs.store_id]

    many_to_many = [(b.title, store_name)
                    for store_name, store_id, book_id in many_to_many_temp
                    for b in books if b.id == book_id]

    print('Задание А1')
    res_11 = list(filter(lambda x: x[0].startswith('В'), one_to_many))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []

    for s in stores:
        s_books = list(filter(lambda i: i[2] == s.name, one_to_many))
        if len(s_books) > 0:
            s_price = [price for _, price, _ in s_books]
            s_price_min = min(s_price)
            res_12_unsorted.append((s.name, s_price_min))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=False)
    print(res_12)

    print('\nЗадание А3')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)


if __name__ == '__main__':
    main()
