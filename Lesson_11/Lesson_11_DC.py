# We create a function in which we write a text file split into a list:
def word_processing(f_handler) -> list:
    lines = list()
    for line in f_handler.readlines():
        # Returning values with a capital letter:
        lines.append(line.strip().capitalize())
    return lines


if __name__ == '__main__':
    # Calling the file handler for reading:
    f = open('Shakespeare_Sonnet_#1.txt', 'r', encoding='utf-8')

    print("Эта программа читает текстовый файл и создает из строк список.")
    print(word_processing(f))
    f.close()
