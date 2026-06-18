import json
import os
from datetime import datetime

BOOKS_FILE = "books.json"

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def is_duplicate(books, author, title):
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            return True
    return False

def add_book(books):
    print("\n--- Добавление книги ---")
    
    author = input("Введите автора: ").strip()
    if not author:
        print("Автор не может быть пустым!")
        return
    
    title = input("Введите название: ").strip()
    if not title:
        print("Название не может быть пустым!")
        return
    
    if is_duplicate(books, author, title):
        print("Такая книга уже есть!")
        return
    
    try:
        rating = int(input("Введите оценку (1-5): "))
        if rating < 1 or rating > 5:
            print("Оценка должна быть от 1 до 5!")
            return
    except ValueError:
        print("Введите целое число!")
        return
    
    date = input("Введите дату (ГГГГ-ММ-ДД): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    })
    save_books(books)
    print("Книга добавлена!")

def show_all_books(books):
    print("\n--- Список книг ---")
    if not books:
        print("Библиотека пуста")
        return
    
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} - {book['title']}")
        print(f"   Оценка: {book['rating']}, Дата: {book['date']}")

def show_average_rating(books):
    if not books:
        print("Нет книг для расчета")
        return
    
    total = sum(book["rating"] for book in books)
    avg = total / len(books)
    print(f"\nСредняя оценка: {avg:.2f}")
    print(f"Всего книг: {len(books)}")

def show_author_stats(books):
    if not books:
        print("Нет книг для статистики")
        return
    
    stats = {}
    for book in books:
        author = book["author"]
        stats[author] = stats.get(author, 0) + 1
    
    print("\n--- Статистика по авторам ---")
    for author, count in sorted(stats.items()):
        print(f"{author}: {count} книг")

def delete_book(books):
    if not books:
        print("Библиотека пуста")
        return
    
    show_all_books(books)
    
    try:
        idx = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= idx < len(books):
            removed = books.pop(idx)
            save_books(books)
            print(f"Книга {removed['title']} удалена!")
        else:
            print("Неверный номер!")
    except ValueError:
        print("Введите число!")

def main():
    books = load_books()
    while True:
        print("\n--- Трекер прочитанных книг ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_all_books(books)
        elif choice == "3":
            show_average_rating(books)
        elif choice == "4":
            show_author_stats(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            save_books(books)
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
