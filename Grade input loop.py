while True:
    score = input("Enter score: ")
    if score == "done" or score == "Done" or score == "DONE":
        break
    try:
        grade = float(score)
    except:
        print("Error, please enter numeric input")
        continue

    if grade > 1.0:
        print("Error, please enter a number between 0.0 and 1.0")
        continue
    elif grade >= 0.9:
        print("A")
        continue
    elif grade >= 0.8:
        print("B")
        continue
    elif grade >= 0.7:
        print("C")
        continue
    elif grade >= 0.6:
        print("D")
        continue
    elif grade >= 0.0:
        print("F")
        continue
    else:
        print("Error, please enter a number between 0.0 and 1.0")
        continue
