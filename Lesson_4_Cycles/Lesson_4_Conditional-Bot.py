# We ask the user for a string, which we turn into a list:
line = str(input()).strip("!;?:,.()").lower().split()

# Set a ready-made list template:
answer = ["привет", "хай", "здарова", "добрый день", "добрый вечер", "здравствуйте"]

# With a "while" loop, we compare two lists for keywords:
while not set(answer) & set(line):

    # If there are no keywords then please enter the line again:

    print("Брат, я ничего не понимаю( ")
    line = str(input()).strip("!;?:,.()").lower().split()
else:

    # If there are such words, then we continue the execution of the program in the same way:

    print("Здравствуй, я бот с Украины! ")

# We repeat the above:

line_two = str(input()).strip("!;?:,.()").lower().split()

answer_two = ["как дела", "что делаешь", "как успехи", "чем занимаешься", "занят", "свободен"]

while not set(answer_two) & set(line_two):
    print("Брат, выражайся яснее ")
    line_two = str(input()).strip("!;?:,.()").lower().split()
else:
    print("Учусь программировать на Python! ")

line_three = str(input()).strip("!;?:,.()").lower().split()

answer_three = ["сериал", "кинотеатр", "фильм", "хобби", "делаю", "занимаюсь"]

while not set(answer_three) & set(line_three):
    print("Что, прости? ")
    line_three = str(input()).strip("!;?:,.()").lower().split()
else:
    if line_three.count("сериал") >= 1:
        print("Брат, я немного занят сейчас, но могу посоветовать тебе сериал 'The Sopranos' ")
    elif line_three.count("кинотеатр") >= 1:
        print("Брат, я немного занят сейчас, но могу посоветовать тебе сходить на 'Мавка: Лісова пісня' ")
    elif line_three.count("фильм") >= 1:
        print("Брат, я немного занят сейчас, но могу посоветовать тебе сходить на 'The Hateful Eight' ")
    elif line_three.count("хобби") >= 1:
        print("Брат, я немного занят сейчас, но могу посоветовать тебе такое хобби, как 'Warhammer' ")
    elif line_three.count("делаю") >= 1:
        print("Брат, я немного занят сейчас, давай потом ")
    else:
        print("Брат, я немного занят сейчас, но очень интересно! ")

print("Слушай, мне реально пора... \n")

line_four = str(input()).strip("!;?:,.()").lower().split()

answer_four = ["пока", "увидимся", "адьес", "гудбай", "поки", "свидимся"]

while not set(answer_four) & set(line_four):
    print("Я устал... Оставь меня в покое... ")
    line_four = str(input()).strip("!;?:,.()").lower().split()
else:
    exit(print("До встречи в сети. "))
