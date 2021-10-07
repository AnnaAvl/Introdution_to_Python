import math

""" Task 6.1
Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached.
Implement to methods: "increment" and "get"
"""


class Counter:

    def __init__(self, start=0, stop=math.inf):
        try:
            if start > stop:
                raise ImportError
        except ImportError:
            print("Start value must be less then stop")
        finally:
            self.start_value = start
            self.stop_value = stop
            self.current_value = start

    def cnt(self):
        print(f'Counter: {self.start_value, self.stop_value}!')

    def get(self):
        print(self.current_value)

    def increment(self):
        try:
            if self.current_value >= self.stop_value:
                raise ValueError
        except ValueError:
            print("Max value is reached")
            return
        self.current_value += 1


""" Task 6.2
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.
"""


class Dictionary:

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = dict()
        self.dictionary = dictionary
        self.changed_keys = list()  # contains data about changes in the dictionary

    def set_value(self, kye, value):
        # add value to dictionary
        self.dictionary.update({kye: value})
        self.changed_keys.append(kye)

    def get_history(self):
        print(self.changed_keys)


""" Task 6.3
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
"""


class Cipher:
    alphabet = "abcdefghijklmnopqrstuvwxyz "  # alphabet for comparison
    code_alphabet = ""  # new alphabet to encode

    def __init__(self, keyword: str):
        temp_alphabet = self.alphabet  # contains the remaining letters
        for i in keyword.lower():
            # add to new alphabet keyword then add the remaining letters
            self.code_alphabet += i
            index = temp_alphabet.index(i)
            temp_alphabet = temp_alphabet[:index] + temp_alphabet[index + 1:len(temp_alphabet)]
        self.code_alphabet += temp_alphabet

    def encode(self, message: str):
        encoded_message = ""
        for i in message:
            # encode the message keeping the case
            if i.isupper():
                i = i.lower()
                encoded_message += self.code_alphabet[self.alphabet.index(i)].upper()
            else:
                encoded_message += self.code_alphabet[self.alphabet.index(i)]
        print(encoded_message)

    def decode(self, message: str):
        decoded_message = ""
        for i in message:
            # decode the message keeping the case
            if i.isupper():
                i = i.lower()
                decoded_message += self.alphabet[self.code_alphabet.index(i)].upper()
            else:
                decoded_message += self.alphabet[self.code_alphabet.index(i)]
        print(decoded_message)


""" Task 6.4
Create hierarchy out of birds.
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.

Implement str() function call for each class.
"""


class Bird:
    def __init__(self, name: str):
        self.name = name

    def fly(self):
        print(self.name, " bird can fly")

    def walk(self):
        print(self.name, " bird can walk")


class FlyingBird(Bird):
    ration = "grains"

    def eat(self):
        print("It eats mostly", self.ration)


class NonFlyingBird(FlyingBird):
    def __init__(self, name: str, ration: str):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        import bcolors
        print(bcolors.ERR + "AttributeError: '" + self.name + "' object has no attribute 'fly'" + bcolors.ENDC)

    def swim(self):
        print(self.name, " bird can swim")


class SuperBird(NonFlyingBird, FlyingBird):

    def __init__(self, name: str, ration="fish"):
        super().__init__(name, ration)
        self.name = name


def inf(bird):
    ability = bird.name + " can "

    if hasattr(bird, "walk"):
        ability += "walk"
    if hasattr(bird, "fly"):
        ability += ", fly"
    if hasattr(bird, "swim"):
        ability += ", swim"
    print(ability)


""" Task 6.5
Implement singleton logic inside your custom class using a method to initialize class instance.
"""


class Sun(object):
    __instance = None

    @staticmethod
    def inst():
        if Sun.__instance is None:
            Sun.__instance = Sun()
        return Sun.__instance


""" Task 6.6
Implement a class Money to represent value and currency.
Implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition 
and subtraction).
"""


class Money:
    # stores information about exchange rates
    exchange_rate_BYN = {
        "EUR": 0.34,
        "RUB": 28.89,
        "USD": 0.4,
        "JPY": 44.53
    }

    def __init__(self, count: float, currency="BYN"):
        self.count = float(count)
        self.currency = currency

    def exchange(self, out_curr: str):
        # method for transferring one currency to another
        if self.currency == out_curr:
            # if the currencies are the same
            return self.count
        # if the input or output currency is "BYN"
        if self.currency == "BYN":
            return round(self.count * (self.exchange_rate_BYN.get(out_curr)), 2)
        if out_curr == "BYN":
            return round(self.count / (self.exchange_rate_BYN.get(self.currency)), 2)
        # if the currencies are different from each other and none of them is "BYN"
        res = self.count / (self.exchange_rate_BYN.get(self.currency)) * (self.exchange_rate_BYN.get(out_curr))
        return round(res, 2)

    def __add__(self, other):
        # method for adding Money type objects
        if isinstance(other, Money):
            return str(self.exchange("BYN") + other.exchange("BYN")) + " BYN"
        raise ArithmeticError

    def __sub__(self, other):
        # method for subtracting Money type objects
        if isinstance(other, Money):
            return str(self.exchange("BYN") - other.exchange("BYN")) + " BYN"
        raise ArithmeticError

    def __mul__(self, other):
        # method for multiplying objects of the Money type or an object by a number
        if isinstance(other, Money):
            return str(round(self.exchange("BYN") * other.exchange("BYN"), 2)) + " BYN"
        elif isinstance(other, (int, float)):
            return str(round(self.exchange("BYN") * other, 2)) + " BYN"
        raise ArithmeticError

    def __truediv__(self, other):
        # method for multiplying objects of the Money type or an object by a number
        if isinstance(other, Money):
            return str(round(self.exchange("BYN") / other.exchange("BYN"), 2)) + " BYN"
        elif isinstance(other, (int, float)):
            return str(round(self.exchange("BYN") / other, 2)) + " BYN"
        raise ArithmeticError

    # methods for comparing objects of the Money type
    def __lt__(self, other):
        if isinstance(other, Money):
            if self.exchange("BYN") < other.exchange("BYN"):
                return True
            else:
                return False
        raise ArithmeticError

    def __le__(self, other):
        if isinstance(other, Money):
            if self.exchange("BYN") <= other.exchange("BYN"):
                return True
            else:
                return False
        raise ArithmeticError

    def __str__(self):
        # method for displaying information about an object of the Money type
        return str(self.count) + " " + self.currency


# # method for subtracting list of Money type objects
def summarize(*args: Money):
    cnt = 0
    for i in args:
        if i.currency != "BYN":
            cnt += i.exchange("BYN")
        else:
            cnt += i.count
    cnt = str(cnt) + " BYN"
    return cnt


""" Task 6.7

Implement a Pagination class helpful to arrange text on pages and list content on given page.
You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that
accepts the page number and return quantity of symbols on this page.

Optional: implement searching/filtering pages by characters/words and displaying pages with all the symbols on it.
If you're querying by symbol that appears on many pages or if you are querying by the word that is divided in two 
return an array of all the appearances.
"""


class Pagination:
    def __init__(self, text: str, chars_on_page: int):
        if chars_on_page <= 0:
            # the number of characters on the page must be greater than 0
            raise AttributeError("'chars_on_page' attribute must be positive and greater than 0")
        self.text = text
        self.chars_on_page = chars_on_page

    def pages_count(self):
        # returns the number of pages
        return math.ceil(len(self.text) / self.chars_on_page)

    def item_count(self):
        return len(self.text)

    def count_items_on_page(self, page_num):
        # returns the number of characters per page
        if page_num + 1 < self.pages_count():
            # if the page is not the last one returns the specified number of characters on the page
            return self.chars_on_page
        elif page_num + 1 == self.pages_count():
            # else returns the current number of elements
            return len(self.text) % self.chars_on_page
        # if the page number is larger than the existing one, raise an exception
        raise Exception("Invalid index. Page is missing.")

    def split_into_pages(self):
        # divide text into pages
        lst = list()
        n = self.chars_on_page
        [lst.append(self.text[i:i + n]) for i in range(0, len(self.text), n)]
        return lst

    def find_page(self, symbols: str):
        # finds pages containing the specified substring
        lst_pages = list()
        cnt = self.text.count(symbols)
        ind = 0
        while cnt > 0:
            page = math.trunc((self.text.find(symbols, ind) + 1) / self.chars_on_page)
            if len(symbols) > self.chars_on_page:
                # if the substring is contained on several pages, return all
                end_page = math.trunc((self.text.find(symbols, ind) + len(symbols) - 1) / self.chars_on_page)
                while page < end_page + 1:
                    if page not in lst_pages:
                        lst_pages.append(page)
                    page += 1
            elif page not in lst_pages:
                lst_pages.append(page)
            cnt -= 1
            ind = self.text.find(symbols, ind) + 1
        if len(lst_pages) == 0:
            # if the text does not contain substring, raise an exception
            raise Exception("'" + symbols + "' is missing on the pages")
        return lst_pages

    def display_page(self, page_num=None):
        # returns the specified page
        if page_num is None:
            # if the page number is not specified, returns all
            return self.split_into_pages()
        elif isinstance(page_num, int) and 0 <= page_num < self.pages_count():
            return self.split_into_pages()[page_num]
        # if the page number is specified incorrectly, it raises an error
        elif isinstance(page_num, int) and page_num >= self.pages_count():
            raise AttributeError("page_num must be less than number of pages")
        raise AttributeError("page_num must be int and 0 or greater than 0")


def main():
    """ Task 6.1 """
    c = Counter(start=42)
    c.increment()
    c.get()
    c = Counter()
    c.increment()
    c.get()
    c.increment()
    c.get()
    c = Counter(start=42, stop=43)
    c.increment()
    c.get()
    c.increment()
    c.get()

    """ Task 6.2 """
    d = Dictionary({"Ann": 2, "Kate": 3})
    d.set_value("Bob", 2)
    d.get_history()
    d.set_value("Polly", 5)
    d.get_history()

    """ Task 6.3 """
    cipher = Cipher("crypto")
    cipher.encode("Hello world")
    cipher.decode("Fjedhc dn atidsn")

    """ Task 6.4 """
    b = Bird("Any")
    b.walk()

    c = FlyingBird("Canary")
    inf(c)
    c.eat()

    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    p.fly()
    p.eat()

    s = SuperBird("Gull")
    inf(s)
    s.eat()

    """ Task 6.5 """
    p = Sun.inst()
    f = Sun.inst()
    print(p is f)

    """ Task 6.6 """
    m = Money(10, "EUR")
    m_1 = Money(10, "BYN")
    m_2 = Money(15)
    print(m_1)
    print(m.exchange("BYN"))
    print(summarize(m, m_1))
    print(m + m_1)
    print(m - m_1)
    print(m * m_1)
    print(m * 3)
    print(m / m_1)
    print(m_1 / 5)
    print(m < m_1)
    print(m <= m_1)
    print(m > m_1)
    print(m >= m_1)
    print(m == m_1)
    print(m != m_1)

    """ Task 6.7 """
    pages = Pagination('Your beautiful text', 5)
    print(pages.pages_count())
    print(pages.item_count())
    # print(pages.count_items_on_page(4))
    # print(pages.split_into_pages())
    print(pages.find_page("Your"))
    print(pages.find_page("e"))
    print(pages.find_page("beautiful"))
    # print(pages.find_page('great'))
    print(pages.display_page())
    print(pages.display_page(0))
    # print(pages.display_page(10))
    # print(pages.display_page("Your"))


if __name__ == "__main__":
    main()
