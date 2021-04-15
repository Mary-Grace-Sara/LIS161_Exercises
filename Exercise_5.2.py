count = 0
sum = 0
maximum = None
minimum = None

while True:
    user_input = input("Enter a number: ")
    if user_input == "done" or user_input == "Done" or user_input == "DONE":
        break
    try:
        float_input = float(user_input)
    except:
        print("Invalid input, please enter numeric data")
        continue

    count = count + 1
    sum = sum + float_input

    if maximum is None:
        maximum = float_input
    elif float_input > maximum :
        maximum = float_input

    if minimum is None:
        minimum = float_input
    elif float_input < minimum :
        minimum = float_input

print("\nCount:", count, "\nTotal:", sum, "\nMaximum:", maximum, "\nMinimum:", minimum)
