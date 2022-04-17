# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# text type*
def test_text_type():
    text = "Good afternoon"
    print(type(text))


# test numeric type()
def test_numeric_type():
    a = 4
    b = 5.2
    c = 1 + 2j
    print(type(a))
    print(type(b))
    print(type(c))


# test bool type
def test_bool_type():
    isvalid = True;
    notvalid = False;
    print(type(isvalid))
    print(type(notvalid))


# test sequence type
def test_sequence_type():
    test_list = ["apple", "banana", "cherry"]
    test_tuple = ("apple", "banana", "cherry")
    test_range = range(6)
    for i in range(6):
        print(i)
    print(test_list)
    print(test_tuple)
    print(test_range)


# test dictionary type
def test_dict_type():
    map = {"name": "John", "age": 36, "color": "red"}
    print(map["age"])


def divide_by_zero():
    number1 = 5
    number2 = 0
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("The divisor cannot be zero")


def fibonacci_number(number):
    counter = 0;
    n1 = 0;
    n2 = 1;
    while counter < number:
        print("The " + str(counter + 1) + "th term is " + str(n1))
        sumNumber = n1 + n2
        n1 = n2
        n2 = sumNumber
        counter = counter + 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_dict_type()
