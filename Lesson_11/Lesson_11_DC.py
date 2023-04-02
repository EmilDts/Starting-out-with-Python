def word_processing(f_handler) -> list:
    lines = list()
    for line in f_handler.readlines():
        lines.append(line.strip())
    return lines


if __name__ == '__main__':
    f = open('Shakespeare_Sonnet_#1.txt', 'r', encoding='utf-8')

    print("Эта программа читает текстовый файл и создает из строк список.")
    print(word_processing(f))
    f.close()
