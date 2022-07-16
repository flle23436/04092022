# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def simpleforloop():
    composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for composite in composites:
        print(composite)

def loopusingrange():
    for x in range(5):
        print(x)

def loopusingrange2():
    for x in range(4, 20):
        print(x)

def loopusingrangeskipcount():
    for x in range(3, 20, 3):
        print(x)

def whileloop():
    count = 0
    while count <= 5:
        print(count)
        count += 1

def whileloop2():
    for x in range(30):
        # Check if x is divisible by 5
        if x % 5 == 0:
          print(x)

def infiniteloop():
    count=0
    while True:
        print(count)
        count +=1

def whileloopwithbreak():
    count = 0
    while True:
        print(count)
        count += 1
        if count >= 5:
            break
    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
   simpleforloop()
