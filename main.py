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

print("выберете уровень сложности.")
print("легкий, средний, сложный.")

while True:

    level = input()
    if level in ["легкий", "средний", "сложный"]:
        if level == "легкий":
            print(f"Выбран уровень сложности {level}, мы предложим 5 слов, подберите перевод. ")
            for k, v in words_easy.items():
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

    else:
        print("Не правильно введен уровень сложности попробуйте снова")







