# создал переменные словари и списки
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}
answers_true = []
answers_false = []
levels = {0: "Нулевой",
          1: "Так себе",
          2: "Можно лучше",
          3: "Норм",
          4: "Хорошо",
          5: "Отлично",
          }
count = 0
# вывод на экран пользователя
print("выберете уровень сложности.")
print("легкий, средний, сложный.")
# создал бесконечный цикл
while True:
    # создал условия при котором проверяется совпадает введенное слово со словами программы
    level = input().lower()
    if level in ["легкий", "средний", "сложный"]:
        # создал блоки проверяющие введенное пользователем слово
        if level == "легкий":
            # вывожу на экран информацию
            print(f"Выбран уровень сложности {level}, мы предложим 5 слов, подберите перевод. ")
            # создаю цикл который достает из словоря слова
            for k, v in words_easy.items():
                start = input("Нажмите Enter.")
                # записываем ответ пользователя
                answer = input(f"{k}, {len(v)} букв, начинается на \"{v[0]}\": ")
                # создал условие при котором правильный ответ записывается в один список а неправельный в другой
                if answer == v:
                    answers_true.append(k)
                    print(f"Верно, {k} — это {v}.")
                    count += 1
                else:
                    answers_false.append(k)
                    print(f"Неверно. {k} — это {v}.")
            # записываю списки в стринг
            ans_true_str = "\n".join(answers_true)
            ans_false_str = "\n".join(answers_false)
            # вывожу результат теста на консоль
            print(f"\nПравильно отвечены слова:\n{ans_true_str}")
            print(f"\nНеправильно отвечены слова:\n{ans_false_str}")
            print(f"\nВаш ранг:\n{levels[count]}")

        elif level == "средний":
            print(f"Выбран уровень сложности {level}, мы предложим 5 слов, подберите перевод. ")
            for k, v in words_medium.items():
                start = input("Нажмите Enter.")
                answer = input(f"{k}, {len(v)} букв, начинается на \"{v[0]}\": ")

                if answer == v:
                    answers_true.append(k)
                    print(f"Верно, {k} — это {v}.")
                    count += 1
                else:
                    answers_false.append(k)
                    print(f"Неверно. {k} — это {v}.")

            ans_true_str = "\n".join(answers_true)
            ans_false_str = "\n".join(answers_false)

            print(f"\nПравильно отвечены слова:\n{ans_true_str}")
            print(f"\nНеправильно отвечены слова:\n{ans_false_str}")
            print(f"\nВаш ранг:\n{levels[count]}")

        elif level == "сложный":
            print(f"Выбран уровень сложности {level}, мы предложим 5 слов, подберите перевод. ")
            for k, v in words_hard.items():
                start = input("Нажмите Enter.")
                answer = input(f"{k}, {len(v)} букв, начинается на \"{v[0]}\": ")

                if answer == v:
                    answers_true.append(k)
                    print(f"Верно, {k} — это {v}.")
                    count += 1
                else:
                    answers_false.append(k)
                    print(f"Неверно. {k} — это {v}.")

            ans_true_str = "\n".join(answers_true)
            ans_false_str = "\n".join(answers_false)

            print(f"\nПравильно отвечены слова:\n{ans_true_str}")
            print(f"\nНеправильно отвечены слова:\n{ans_false_str}")
            print(f"\nВаш ранг:\n{levels[count]}")
    # если не совпадает введенное слово с програмными словами отправляет пользователя обратно ввести сложность
    else:
        print("Не правильно введен уровень сложности попробуйте снова")







