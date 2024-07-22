import json
import os


class Book:
    def __init__(self, book_id, title, author, year, status) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return f'ID: {self.book_id}, Title: "{self.title}", Author: {self.author}, Year: {self.year}, Status: {self.status}'

    def convert_to_dict(self) -> dict:
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
        }


class BookOperations:
    def __init__(self, filename='books.json') -> None:
        self.filename = filename
        self.books = {}
        self.next_id = 1
        self.load_books()

    # Проверка существования json файла и его загрузка
    def load_books(self) -> None:
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.books = {item['book_id']: Book(**item) for item in data}
                if self.books:
                    self.next_id = max(self.books.keys()) + 1

    # Сохранение данных в json файл
    def save_books(self) -> None:
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.convert_to_dict() for book in self.books.values()], file, ensure_ascii=False, indent=4)

    # Добавление пользователем книги
    def add_book(self, title, author, year) -> None:
        book = Book(self.next_id, title, author, year, status='в наличии')
        self.books[self.next_id] = book
        self.next_id += 1
        self.save_books()
        print(f'Книга "{title}" добавлена!')

    # Удаление пользователем книги
    def delete_book(self, book_id) -> None:
        if book_id in self.books:
            deleted_book = self.books.pop(book_id)
            self.save_books()
            print(f'Книга "{deleted_book.title}" удалена!')
        else:
            print('Ошибка: Книга с таким ID не найдена.')

    # Поиск книги по одному из параметров
    def search_book(self, search_param) -> list[Book]:
        results = [
            book for book in self.books.values()
            if search_param.lower() in book.title.lower() or
            search_param.lower() in book.author.lower() or
            search_param == str(book.year)
        ]
        return results

    # Показ всех книг
    def show_books(self) -> None:
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books.values():
                print(book)

    # Изменение статуса книги
    def change_status(self, book_id, new_status) -> None:
        if book_id in self.books:
            if new_status in ['в наличии', 'выдана']:
                self.books[book_id].status = new_status
                self.save_books()
                print(f'Статус книги "{self.books[book_id].title}" изменен на "{new_status}".')
            else:
                print('Ошибка: Неверный статус. Статус может быть "в наличии" или "выдана".')
        else:
            print('Ошибка: Книга с таким ID не найдена.')
