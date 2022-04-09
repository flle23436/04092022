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


def calculate_add():
    a = 6;
    b = 9;
    return a + b


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
    number1 = 5
    number2 = 0
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("The divisor cannot be zero")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #draw_heart('Winston')
    divide_by_zero()
