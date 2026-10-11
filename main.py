def ask_required(question, error_message):
    value = input(question).strip()
    while value == "":
        print(error_message)
        value = input(question).strip()

    return value

author = ask_required("Как тебя зовут? ", "Имя не может быть пустым. Пожалуйста, введите свое имя.")

city = ask_required("В каком городе ты живешь? ", "Город не может быть пустым. Пожалуйста, введите название города.")

news = ask_required("Что у тебя произошло за неделю? ", "Новость не может быть пустой. Пожалуйста, расскажи о своей неделе.")

print(f"Автор: {author}")
print(f"Город: {city}")
print(f"Новость: {news}")
