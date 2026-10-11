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

def create_post():
    author = ask_required("Как тебя зовут? ", "Имя не может быть пустым. Пожалуйста, введите свое имя.")
    city = ask_required("В каком городе ты живешь? ", "Город не может быть пустым. Пожалуйста, введите название города.")
    news = ask_required("Что у тебя произошло за неделю? ", "Новость не может быть пустой. Пожалуйста, расскажи о своей неделе.")

    return  {
        "author": author,
        "city": city,
        "news": news
    }
posts = []

while True:
    print("\nНа связи")
    print("1. Добавить новость")
    print("2. Показать новости")
    print("0. Выйти")

    choice = input("Выберите действие: ").strip()

    if choice == "1":
        post = create_post()
        posts.append(post)
        print("Новость успешно добавлена!")

    elif choice == "2":
        if not posts:
            print("Пока нет новостей. Добавьте первую новость!")
        else:
            for post in posts:
                show_post(post)
                print()

    elif choice == "0":
        print("До встречи!")
        break

    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 0.")




