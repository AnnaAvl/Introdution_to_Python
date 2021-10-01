import re


def function_1(st):
    # replace "\'" with a new symbol, which shouldn't be in the string to replace our symbols correctly
    st = st.replace("\'", "%temp%").replace("\"", "\'").replace("%temp%", "\"")
    return st


def check_palindrome(st):
    st = st.lower()
    i = 0
    j = len(st) - 1
    # check the symbols that are in the mirror positions until we get to the middle
    while j - i > 0:
        # if they're different, the word isn't a palindrome
        if st[i] != st[j]:
            return "The string isn't a palindrome"
        i += 1
        j -= 1
    return "The string is a palindrome"


def split_function(st, letter):
    split_st = list()
    for i in range(st.count(letter)):
        num = (st.index(letter))
        # if the letter isn't first, make a split
        if st[:num] != "":
            split_st.append(st[:num])
            st = st[num + 1:len(st)]
    # add the last piece
    split_st.append(st)
    return split_st


def split_by_index(st: str, indexes: list[int]):
    split_st = list()
    previous_index = 0
    for i in indexes:
        # check index, it should be positive, less than the length of the string and greater than the previous index
        if 0 <= i < len(st) and i > previous_index:
            split_st.append(st[previous_index:i])
            previous_index = i
    # make all splits and add the last piece
    split_st.append(st[previous_index:len(st)])
    return split_st


def split_number(num: int):
    list_of_numbers = list[int]()
    # to have each element of number, make it a string
    for i in str(num):
        list_of_numbers.append(int(i))
    return tuple(list_of_numbers)


def get_longest_word(st: str):
    length = 0
    st = st.split()
    for i in st:
        # looking for the max length
        if len(i) > length:
            length = len(i)
    for i in st:
        # looking for the first world with the max length
        if len(i) == length:
            return i


def function_7(lst: list[int]):
    final_lst = list[int]()
    for i in lst:
        num = 1
        for j in lst:
            # multiply all elements except n-th one
            if i != j:
                num = num * j
        final_lst.append(num)
    return final_lst


def get_pairs(lst: list):
    if len(lst) <= 1:
        return None
    final_lst = list()
    for i in range(len(lst) - 1):
        final_lst.append((lst[i], lst[i + 1]))
    return final_lst


def test_1(strings: list):
    letters = ""
    res = ""
    # for each string
    for i in strings:
        # for each element
        for j in i:
            # condition not to check the element again
            if letters.find(j) == -1:
                c = 0
                letters += j
                # check if it contains in each string
                for s in strings:
                    if s.find(j) == -1:
                        c += 1
                # add letter if condition is met
                if c == 0:
                    res += j
    if res == "":
        return None
    return sorted(list(res))


def test_2(strings: list):
    res = ""
    for i in strings:
        for j in i:
            # condition to not repeat the element again
            if res.find(j) == -1:
                # add all element which used in strings
                res += j
    if res == "":
        return None
    return sorted(list(res))


def test_3(strings: list):
    letters = ""
    res = ""
    for i in strings:
        for j in i:
            if letters.find(j) == -1:
                c = 0
                letters += j
                for s in strings:
                    if s.find(j) != -1:
                        c += 1
                # check whether the element was used in at least two lines
                if c >= 2:
                    res += j
    if res == "":
        return None
    return sorted(list(res))


def test_4(strings: list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in strings:
        for j in i:
            # check whether the element (bring to the lower case) is in alphabet
            if alphabet.find(str.lower(j)) != -1:
                index = alphabet.index(str.lower(j))
                # if find it, cut it out
                alphabet = alphabet[:index] + alphabet[index + 1:len(alphabet)]
    if alphabet == "":
        return None
    return list(alphabet)


def generate_dict(num: int):
    dictionary = {a: a ** 2 for a in range(1, num + 1)}
    return dictionary


def combine_dicts(*args):
    d = dict()
    for i in args:
        for key, value in i.items():
            if key in d:
                d[key] += value
            else:
                d.update({key: value})

    return d


def main():
    """ Task 4.1
    Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.
    """
    print(function_1(input("Please, enter a string: ")))
    """ Task 4.2
    Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited. 
    """
    print(check_palindrome(input("Please, enter a string to check if it's a palindrome: ")))
    """ Task 4.3
    Implement a function which works the same as `str.split` method
    """
    print(split_function(input("Please, enter a string: "), input("Please, enter a symbol to split the string: ")))
    """ Task 4.4
    Implement a function which splits the string by indexes. Wrong indexes must be ignored.
    """
    print(split_by_index(input("Please, enter a string: "),
                         [int(item) for item in
                          re.split(",+", input("Please, enter sequence of numbers separated by commas: "))]))
    """ Task 4.5
    Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple of a given integer's digits.
    """
    print(split_number(int(input("Please, enter a number: "))))
    """ Task 4.6
    Implement a function which returns the longest word in the given string. The word can contain any symbols except
    whitespaces. If there are multiple longest words in the string with a same length return
    the word that occurs first.
    """
    print(get_longest_word(input("Please, enter a string: ")))
    """ Task 4.7
    Implement a function `foo(List[int]) -> List[int]` which, given a list of
    integers, return a new list such that each element at index `i` of the new list
    is the product of all the numbers in the original array except the one at `i`.
    """
    print(function_7([int(item) for item in
                      re.split(",+", input("Please, enter sequence of numbers separated by commas: "))]))
    """ Task 4.8
    Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
    of tuples containing pairs of elements. Pairs should be formed as in the
    example. If there is only one element in the list return `None` instead.
    """
    print(get_pairs([int(item) for item in
                     re.split(",+", input("Please, enter sequence separated by commas: "))]))
    """ Task 4.9
    Implement a bunch of functions which receive a changeable number of strings and return next parameters:
    1) characters that appear in all strings
    2) characters that appear in at least one string
    3) characters that appear at least in two strings
    4) characters of alphabet, that were not used in any string
        Note: use `string.ascii_lowercase` for list of alphabet letters
    """
    print("Please, enter a changeable number of strings(each string starts from a new line). "
          "When you finish, press 'Enter' twice: ")
    strings = list(iter(input, ''))
    print(test_1(strings))
    print(test_2(strings))
    print(test_3(strings))
    print(test_4(strings))
    """ Task 4.10
    Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the
    value is the square of that number.
    """
    print(generate_dict(int(input("Please, enter a number: "))))
    """ Task 4.11
    Implement a function, that receives changeable number of dictionaries and combines
    them into one dictionary. Dict values should be summarized in case of identical keys
    """
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))


if __name__ == "__main__":
    main()
