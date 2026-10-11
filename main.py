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
    
author = ask_required("Как тебя зовут? ", "Имя не может быть пустым. Пожалуйста, введите свое имя.")

city = ask_required("В каком городе ты живешь? ", "Город не может быть пустым. Пожалуйста, введите название города.")

news = ask_required("Что у тебя произошло за неделю? ", "Новость не может быть пустой. Пожалуйста, расскажи о своей неделе.")

post = {
    "author": author,
    "city": city,
    "news": news
} 

show_post(post)

