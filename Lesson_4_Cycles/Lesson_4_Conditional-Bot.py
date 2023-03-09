line = str(input())
line_s = line.strip("!;?:,.()").lower().split()

answer = ["привет", "хай", "здарова", "добрый день", "добрый вечер", "здравствуйте"]

if set(answer) & set(line_s):
    print("Здравствуй, я бот с Украины! ")
else:
    print("Брат, я ничего не понимаю( ")

line_two = str(input())
line_two_s = line_two.strip("!;?:,.()").lower().split()

answer_two = ["как дела", "что делаешь", "как успехи", "чем занимаешься", "занят", "свободен"]

if set(answer_two) & set(line_two_s):
    print("Учусь программировать на Python! ")
else:
    print("Брат, выражайся яснее ")

line_three = str(input())
line_three_s = line_three.strip("!;?:,.()").lower().split()

answer_three = ["сериал", "кинотеатр", "фильм", "хобби", "делаю", "занимаюсь"]

if set(answer_three) & set(line_three_s):
    if line_three_s.count("сериал") >= 1:
        print("Брат, я немного занят сейчас, но могу посоветовать тебе сериал 'The Sopranos' ")
    elif line_three_s.count("кинотеатр") >= 1:
        print("Брат, я немного занят сейчас, но могу посоветовать тебе сходить на 'Мавка: Лісова пісня' ")
    elif line_three_s.count("фильм") >= 1:
        print("Брат, я немного занят сейчас, но могу посоветовать тебе сходить на 'The Hateful Eight' ")
    elif line_three_s.count("хобби") >= 1:
        print("Брат, я немного занят сейчас, но могу посоветовать тебе такое хобби, как 'Warhammer' ")
    elif line_three_s.count("кинотеатр") >= 1:
        print("Брат, я немного занят сейчас, давай потом ")
    else:
        print("Брат, я немного занят сейчас, но очень интересно! ")
else:
    print("Что, прости? ")

line_four = str(input())
line_four_s = line_four.strip("!;?:,.()").lower().split()

answer_four = ["пока", "до завтра", "до свидания", "увидимся", "до встречи", "спокойной ночи"]

if set(answer_four) & set(line_four_s):
    print("До встречи в сети! ")
else:
    print("Все равно ничего не понял... ")

exit()