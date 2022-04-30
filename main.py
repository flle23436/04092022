# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def draw_giraffe():
    print("""\

                                           ._ o o
                                           \_`-)|_
                                        ,""       \ 
                                      ,"  ## |   ಠ ಠ. 
                                    ," ##   ,-\__    `.
                                  ,"       /     `--._;)
                                ,"     ## /
                              ,"   ##    /


                        """)


def draw_cat(name):
    print('                                   ')
    print('                                /- )')
    print('                           (  (')
    print('           A.-.A  .-""-.    )  )')
    print('         /,  ,\ \/       \ \/  /')
    print('        =\ \  t   ;=    /      /')
    print('           `--,\`  .""|      /')
    print('             || |   \ \ \ \   ')
    print('              ((,_|    ((,_\ ')
    print('-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^')
    print('  This is a lovely cat drew by', name)


def calculate_add(a, b):
    return a + b


def calculate_multiply(c, d):
    return c * d


def calculate_multiple_threenumber(a, b, c):
    return a * b * c


def draw_heart(name):
    print('      ♥LOVE♥ ' + str(name) + ' ♥LOVE♥           ')
    print('     ♥LOVE♥♥LOVE♥  ♥LOVE♥♥LOVE♥       ')
    print('   ♥LOVE♥♥LOVE♥♥LOVE♥♥LOVE♥♥LOVE♥    ')
    print('      ♥LOVE♥♥LOVE♥♥LOVE♥♥LOVE♥       ')
    print('         ♥LOVE♥♥LOVE♥♥LOVE♥          ')
    print('            ♥LOVE♥♥LOVE♥              ')
    print('              ♥LOVE♥                  ')
    print('                 ♥                    ')


def divide_by_zero():
    number1 = 99
    number2 = 0

    try:
        return number1 * 1.0 / number2
    except ZeroDivisionError:
        print("The divisor cannot be zero")


def calculate_divide(a, b):
    return a / b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(divide_by_zero())

