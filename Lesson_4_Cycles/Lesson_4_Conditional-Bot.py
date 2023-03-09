line = str(input())
line_s = line.strip("!;?:,.()")

answer = ["привет", "хай", "здарова", "добрый день", "добрый вечер", "здравствуйте"]

if line_s.lower() in answer:
    print("Здравствуй, я бот с Украины!")
else:
    print("Брат, я ничего не понимаю(")

line_two = str(input())
line_two_s = line_two.strip("!;?:,.()")

answer_two = ["как дела", "что делаешь", "здарова", "чем занимаешься", "занят", "свободен"]

if line_two_s.lower() in answer_two:
    print("Учусь программировать на Python!")
else:
    print("Брат, выражайся яснее")

line_three = str(input())
line_three_s = line_three.strip("!;?:,.()")

answer_three = ["сериал", "кинотеатр", "фильм", "хобби", "делаю", "занимаюсь"]

if line_three_s.lower() in answer_three:
    print(f'Брат, я немного занят сейчас, но могу посоветовать тебе, {} это как раз соответствует твоим интересам.')
else:
    print("Что, простите?")


