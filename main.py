# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def simpleforloop():
    primes = [2, 3, 5, 7]
    for prime in primes:
        print(prime)

def loopusingrange():
    for x in range(5):
        print(x)

def loopusingrange2():
    for x in range(3, 6):
        print(x)

def loopusingrangeskipcount():
    for x in range(3, 20, 3):
        print(x)

def whileloop():
    count = 0
    while count < 5:
        print(count)
        count += 1

def whileloop2():
    for x in range(10):
        # Check if x is even
        if x % 2 == 0:
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
    whileloopwithbreak()
