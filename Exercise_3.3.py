score = input("Enter score: ")
try:
    grade = float(score)
    if grade > 1.0:
        print("Error, please enter a number between 0.0 and 1.0")
    elif grade >= 0.9:
        print("A")
    elif grade >= 0.8:
            print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    elif grade >= 0.0:
        print("F")
    else:
        print("Error, please enter a number between 0.0 and 1.0")
except:
    print("Error, please enter numeric input")
