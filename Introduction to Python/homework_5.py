from collections import Counter

import re


def sort_names(f_input, f_output):
    with open(f_input) as f_input:
        names_list = f_input.readlines()
    names_list = [x.strip() for x in names_list]
    f_input.close()
    names_list = sorted(names_list)
    names_list = map(lambda x: x + '\n', names_list)
    f_output = open(f_output, 'w')
    f_output.writelines(names_list)
    f_output.close()


def most_common_words(f_input, amount: int):
    f_input = open(f_input, "r")
    lines = [x.strip() for x in f_input.readlines()]
    words = list()
    for line in lines:
        for x in re.split(r"\W+", line.lower()):
            if x != "":
                words.append(x)
    lst_words = dict(Counter(words))
    most_common = list()
    max_cnt = max(lst_words.values())
    while amount > 0:
        for word, cnt in lst_words.items():
            if cnt == max_cnt:
                most_common.append(word)
                lst_words.pop(word, cnt)
                max_cnt = max(lst_words.values())
                amount -= 1
                break
    f_input.close()
    return most_common


def get_top_performers(f_input, number_of_top_students: int):
    f_input = open(f_input, "r")
    lines = [x.strip().split(",") for x in f_input.readlines()]
    names = list()
    marks = [0.0] * len(lines)
    lines.pop(0)
    for i in range(len(lines)):
        marks[i] = float(lines[i][2])
    while number_of_top_students > 0:
        max_mark = max(marks)
        for i in range(len(lines)):
            if float(lines[i][2]) == max_mark:
                names.append(lines[i][0])
                lines.pop(i)
                marks.pop(i)
                number_of_top_students -= 1
                break
    f_input.close()
    return names


def sorted_by_age(f_input):
    f_input = open(f_input, "r")
    lines = [x.strip().split(",") for x in f_input.readlines()]
    lines.pop(0)
    ages = [0] * len(lines)
    for i in range(len(lines)):
        ages[i] = int(lines[i][1])
    f_output = open("data/sorted_students.csv", 'w')
    while lines:
        max_age = max(ages)
        for i in range(len(lines)):
            if int(lines[i][1]) == max_age:
                f_output.writelines(",".join(lines[i]) + "\n")
                lines.pop(i)
                ages.pop(i)
                break
    f_input.close()
    f_output.close()


a = "I am global variable!"


def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    return inner_function()


def enclosing_function_modified():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)

    return inner_function()


def enclosing_function_modified_2():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)

    return inner_function()


def remember_result(function):
    last_result = None

    def wrapper(*args):
        nonlocal last_result
        print(f"Last result = '{last_result}'")
        last_result = function(*args)

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result


def call_once(function):
    cached_result = None

    def wrapper(*args):
        nonlocal cached_result
        if cached_result is None:
            cached_result = function(*args)
        return cached_result

    return wrapper


@call_once
def sum_of_numbers(variable_1, variable_2):
    return variable_1 + variable_2


def main():
    """ Task 4.1
    Open file in data folder. Sort the names and write them to a new file. Each name should start with a new line."""
    # data/unsorted_names.txt
    # data/sorted_names.txt

    sort_names(input("Please, enter a path to the input file: "), input("Please, enter a path to the output file: "))

    """ Task 4.2
    Implement a function which search for most common words in the file."""
    # data/lorem_ipsum.txt

    print(most_common_words(input("Please, enter a path to the file: "),
                            int(input("Please, enter a number of words to output: "))))

    """ Task 4.3
    1) Implement a function which receives file path and returns names of top performer students
    
    2) Implement a function which receives the file path with students info and writes CSV student information to the new
     file in descending order of age.
    """
    # data/students.csv

    print(get_top_performers(input("Please, enter a path to the file: "),
                             int(input("Please, enter a number of words to output: "))))
    sorted_by_age(input("Please, enter a path to the file: "))

    """ Task 4.4
    Look through file `modules/legb.py`.
    1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
    2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
    2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
    """
    enclosing_function()
    enclosing_function_modified()
    enclosing_function_modified_2()

    """ Task 4.5
    Implement a decorator which remembers last result of function it decorates and prints it before next call.
    """
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)

    """ Task 4.6
    Implement a decorator which runs a function or method once and caches the result.
    All consecutive calls to this function should return cached result no matter the arguments.
    """
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))


if __name__ == "__main__":
    main()
