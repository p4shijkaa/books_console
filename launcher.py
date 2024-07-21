from main_logic import BookOperations


def main():
    books_operations = BookOperations()

    def first_choice():
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        while True:
            year = input("Введите год издания: ")
            if year.isdigit():
                year = int(year)
                break
            else:
                print("Ошибка: Введите корректный год (четыре цифры).")
        books_operations.add_book(title, author, year)

    def second_choice():
        while True:
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                break
            except ValueError:
                print("Ошибка: Введите целое число для ID книги.")
        books_operations.delete_book(book_id)

    def third_choice():
        search_term = input("Введите название, автора или год для поиска: ")
        results = books_operations.search_book(search_term)
        if results:
            print("Найдены книги:")
            for book in results:
                print(f'ID: {book.book_id}, Title: "{book.title}", Author: {book.author}, Year: {book.year}, Status: {book.status}')
        else:
            print("Книги не найдены.")

    def fourth_choice():
        print("Список книг в библиотеке:")
        books_operations.show_books()

    def fifth_choice():
        book_id = int(input("Введите ID книги для изменения статуса: "))
        new_status = input("Введите новый статус (в наличии/выдана): ")
        books_operations.change_status(book_id, new_status)

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        choice = input("Выберите опцию: ")

        choices_dict = {
            '1': first_choice,
            '2': second_choice,
            '3': third_choice,
            '4': fourth_choice,
            '5': fifth_choice
        }

        if choice == '6':
            print("Выход из программы.")
            break

        elif choice in choices_dict:
            choices_dict[choice]()

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
