import json
import os


class Book:
    def __init__(self, book_id, title, author, year, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f'ID: {self.book_id}, Title: "{self.title}", Author: {self.author}, Year: {self.year}, Status: {self.status}'

    def convert_to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
        }


class BookOperations:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = {}
        self.next_id = 1
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.books = {item['book_id']: Book(**item) for item in data}
                if self.books:
                    self.next_id = max(self.books.keys()) + 1

    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.convert_to_dict() for book in self.books.values()], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        book = Book(self.next_id, title, author, year, status='в наличии')
        self.books[self.next_id] = book
        self.next_id += 1
        self.save_books()
        print(f'Книга "{title}" добавлена!')

    def delete_book(self, book_id):
        if book_id in self.books:
            deleted_book = self.books.pop(book_id)
            self.save_books()
            print(f'Книга "{deleted_book.title}" удалена!')
        else:
            print('Ошибка: Книга с таким ID не найдена.')

    def search_book(self, search_param):
        results = [
            book for book in self.books.values()
            if search_param.lower() in book.title.lower() or
            search_param.lower() in book.author.lower() or
            search_param == str(book.year)
        ]
        return results

    def show_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books.values():
                print(book)

    def change_status(self, book_id, new_status):
        if book_id in self.books:
            if new_status in ['в наличии', 'выдана']:
                self.books[book_id].status = new_status
                self.save_books()
                print(f'Статус книги "{self.books[book_id].title}" изменен на "{new_status}".')
            else:
                print('Ошибка: Неверный статус. Статус может быть "в наличии" или "выдана".')
        else:
            print('Ошибка: Книга с таким ID не найдена.')
