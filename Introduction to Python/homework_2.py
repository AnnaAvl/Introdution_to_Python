import re
import numpy as numpy


def main():
    """ Task 1.1
    Write a Python program to calculate the length of a string without using the `len` function.
    """

    arr_1 = input("Please, input a string: ")
    cnt = 0
    for i in arr_1:
        cnt += 1
    print("The length of your string is: " + str(cnt))

    """ Task 1.2
    Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
    """

    arr_2 = input("Please, input a string: ").lower()  # brought the string to the lower case to ignore case of letters
    letters_2 = ""
    chars_2 = ""
    res_2 = ""
    for i in arr_2:
        if letters_2.find(i) == -1 and i.isalpha():
            # add the symbol to the list if it's letter and doesn't repeat itself
            letters_2 += i
        elif chars_2.find(i) == -1 and not i.isalpha():
            # add the symbol to the list if it isn't letter and doesn't repeat itself
            chars_2 += i
    letters_2 += chars_2
    for j in letters_2:
        res_2 += ("'" + j + "': " + str(arr_2.count(j)) + ", ")
    print(res_2[:-2])  # cut off the last comma and space

    """ Task 1.3
    Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in 
    sorted form.
    """

    arr_3 = input("Please, input a sequence: ").replace(",", " ")  # replace "," with " " in the entered line
    arr_3 = re.split(" +", arr_3)  # divide the string by the n-th number of spaces into words
    if arr_3[:-1] == "":
        arr_3.remove("")  # if the last element is empty, delete it
    res_3 = arr_3[0]
    for i in arr_3:
        if res_3.find(i) == -1:
            res_3 += (" " + i)
    print(sorted(re.split(" +", res_3)))

    """ Task 1.4
    Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
    """

    num_4 = int(input("Please, input a number: "))
    res_4 = list()

    for i in range(1, num_4 + 1):
        if num_4 % i == 0:
            res_4.append(i)
    print("The divisors of that number: " + str(res_4)[1:-1])

    """ Task 1.5
    Write a Python program to sort a dictionary by key.
    """

    dict_5 = {1: "python", 7: "list", 4: "tuple", 2: "hash", 5: "program"}

    for key in sorted(dict_5):
        print("%s: %s" % (key, dict_5[key]))

    """ Task 1.6
    Write a Python program to print all unique values of all dictionaries in a list.
    """

    list_6 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
              {"VIII": "S007"}]
    res_6 = ""

    for i_dict in list_6:
        for key in i_dict:
            if res_6.find(i_dict[key]) == -1:
                res_6 += (i_dict[key] + ", ")
    print(res_6[:-2])

    """ Task 1.7
    Write a Python program to convert a given tuple of positive integers into an integer. 
    """

    tuple_7 = (1, 2, 3, 4)
    res_7 = ""
    for i in tuple_7:
        res_7 += str(i)
    print(res_7)

    """ Task 1.8
    Write a program which makes a pretty print of a part of the multiplication table.
    """
    print("Enter parameters")
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    height = int(b - a + 2)
    width = int(d - c + 2)
    res_8 = numpy.zeros((height, width))
    for i in range(1, height):
        res_8[i][0] = a
        a += 1
    for i in range(1, width):
        res_8[0][i] = c
        c += 1
    for i in range(1, height):
        for j in range(1, width):
            res_8[i][j] = res_8[i][0] * res_8[0][j]
    res_8 = str(res_8)
    index = int(res_8.index("0"))
    res_8 = res_8[:index] + "*" + res_8[index + 1:]
    res_8 = " " + res_8.replace("[", "").replace("]", "").replace(".", "")
    print(res_8)


if __name__ == "__main__":
    main()
