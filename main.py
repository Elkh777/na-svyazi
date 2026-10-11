import json
from pathlib import Path
from datetime import datetime

POSTS_FILE = Path(__file__).resolve().parent / "posts.json"

def ask_required(question, error_message):
    value = input(question).strip()
    while value == "":
        print(error_message)
        value = input(question).strip()

    return value

def show_post(post):
    print(f"Автор: {post['author']}")
    print(f"Город: {post['city']}")
    print(f"Новость: {post['news']}")
    print(f"Дата: {post.get('created_at', 'Дата неизвестна')}")

def create_post():
    author = ask_required("Как тебя зовут? ", "Имя не может быть пустым. Пожалуйста, введите свое имя.")
    city = ask_required("В каком городе ты живешь? ", "Город не может быть пустым. Пожалуйста, введите название города.")
    news = ask_required("Что у тебя произошло за неделю? ", "Новость не может быть пустой. Пожалуйста, расскажи о своей неделе.")

    return  {
        "author": author,
        "city": city,
        "news": news,
        "created_at": datetime.now().isoformat(timespec='seconds')
    }

def save_posts(posts):
    with POSTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)

def load_posts():
    if not POSTS_FILE.exists():
        return []
    with POSTS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def show_posts_by_author(posts, author):
    found = False 

    for post in posts: 
        if post['author'].casefold() == author.casefold():
            show_post(post)
            print()
            found = True

    if not found:
        print(f"Пока нет новостей от автора '{author}'.")

def main():
    try:
        posts = load_posts()
    except json.JSONDecodeError:
        print(f"Не удалось прочитать {POSTS_FILE.name}: неверный формат JSON.")
        print("Проверь файл.")
        return

    while True:
        print("\nНа связи")
        print("1. Добавить новость")
        print("2. Показать новости")
        print("3. Показать новости по автору")
        print("0. Выйти")

        choice = input("Выберите действие: ").strip()
        print()

        if choice == "1":
            post = create_post()
            posts.append(post)
            save_posts(posts)
            print("Новость успешно добавлена!")

        elif choice == "2":
            if not posts:
                print("Пока нет новостей. Добавьте первую новость!")
            else:
                for post in posts:
                    show_post(post)
                    print()

        elif choice == "3":
            author = ask_required("Введите имя автора: ", "Имя автора не может быть     пустым. Пожалуйста, введите имя автора.")
            show_posts_by_author(posts, author)

        elif choice == "0":
            print("До встречи!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 0.")

if __name__ == "__main__":
    main()
