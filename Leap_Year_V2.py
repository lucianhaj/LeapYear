def main():
    error = 0
    global x
    try:
        x = input("What is the input?")
    except NameError:
        print("Your input was not a valid year")
        main()
    except SyntaxError:
        print("Your year input contains invalid characters")
        main()
    else:

        if str(x).isdigit() == 1:
            if (x % 4 == 0) and (x % 100 == 0) and (x % 400 == 0):
                print (x, "is a leap year")
            elif (x % 4 == 0) and (not (x % 100 == 0)):
                print (x, "is a leap year")
            else:
                print (x, "is not a leap year")
        else:
            print("error")
main()