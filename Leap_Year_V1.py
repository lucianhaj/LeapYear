


def main():
    x = input("What is the input?")
    print ("you entered", x)

    if (x % 4 == 0) and (x % 100 == 0) and (x % 400 == 0):
        print (x, "is a leap year")
    elif (x % 4 == 0) and  (not(x % 100 == 0)):
         print (x, "is a leap year")
    else:
        print (x, "is not a leap year")



main()