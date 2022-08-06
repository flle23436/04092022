# This is a sample Python script.

def printoddoreven(number):
    if number % 2 == 0:
        print("n is even")
    else:
        print("n is odd")

def comparenumber(number1, number2):
    if number1 == number2:
        print("Both are Equal")
    elif number1 > number2:
        print("number1 is greater than number2")
    else:
        print("number1 is smaller than number2")

def whatismygrade(grade):
    if grade >= 80:
        print("Congratulations, you have earned an A")
    elif grade >= 65:
        print("Good job, you have earned a B. Keep going")
    elif grade >= 50:
        print("You have earned a C. There is much room to improve.")
    else:
       print("Sorry. You failed")

def numbers_to_strings(argument):
        switcher = {
            0: "zero",
            1: "one",
            2: "two",
        }

        # get() method of dictionary data type returns
        # value of passed argument if it is present
        # in dictionary otherwise second argument will
        # be assigned as default value of passed argument
        return switcher.get(argument, "nothing")

def whatistheday(day):
   match day:
      case 1:
         return "It is Monday"
      case 2:
          return "It is Tuesday"
      case 3:
          return "It is Wednesday"




    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print(whatistheday(0))
