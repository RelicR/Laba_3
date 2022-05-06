"""
Программа, которая читая текст из файла, выводит на экран предложения,
содержащие английские слова, переведя их (английские слова) в верхний регистр.
"""
import profile
import time


def laba2(text_name):
    try:
        with open(f"{text_name}.txt", "r", encoding="utf-8") as file:
            buffer_size, max_buffer_size = 1, 512
            work_buffer = ""
            en_flag, char_flag = False, False
            end_of_sentence = ['.', '!', '?']
            positive = 0
            print("\n-----Результат работы программы-----\n")
            buffer = file.read(buffer_size)
            if not buffer:
                print("Файл text.txt пустой.\nИзмените файл или добавьте не пустой файл text.txt в директорию проекта.\n")
            else:
                while buffer and len(work_buffer) < max_buffer_size:
                    if 'a' <= buffer <= 'z' or 'A' <= buffer <= 'Z':
                        work_buffer += buffer.upper()
                        en_flag, char_flag = True, True
                    elif buffer not in end_of_sentence:
                        work_buffer += buffer
                        char_flag = True
                    elif en_flag and char_flag:
                        print(work_buffer.strip())
                        en_flag, char_flag = False, False
                        work_buffer = ""
                        positive += 1
                    else:
                        en_flag, char_flag = False, False
                        work_buffer = ""
                    buffer = file.read(buffer_size)
                if len(work_buffer) >= max_buffer_size:
                    print("Превышен максимальный размер буфера\nИзмените файл или добавьте корректный файл в директорию")
                if positive == 0:
                    print("Ни одно предложение в файле не содержит латинских символов.")

    except FileNotFoundError:
        print("""Файл text.txt в директории проекта не обнаружен.
Добавьте файл в директорию или переименуйте существующий *.txt файл.""")


def laba3():
    tests = {"Тест 1": "\nФайл, текст длиной 4779 символов, содержащий как латиницу, так и кириллицу",
             "Тест 2": "\nФайл, текст длиной 4994 символа, содержащий только латиницу",
             "Тест 3": "\nФайл, текст длиной 5094 символа, содержащий только кирилицу",
             "Тест 4": "\nФайл, текст длиной 5097 символов, не имеющий знаков окончания предложения",
             "Тест 5": "\nПустой файл", "Тест 6": "\nФайла нет в директории проекта"}
    for i in range(1, 7):
        start = time.time()
        print(f"Тест {i}", tests[f"Тест {i}"], '\n')
        #profile.run(f"laba2('test{i}')")
        laba2(f"test{i}")
        print(time.time()-start)


choice = ''
while choice != '1' and choice != '2':
    choice = input("Выберете алгоритм работы программы\nВведите 1 для профилирования\nВведите 2 для запуска основной программы\n")
if choice == '1':
    laba3()
elif choice == '2':
    laba2("text")
