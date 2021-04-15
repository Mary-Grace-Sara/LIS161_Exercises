count = 0
sum = 0

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

print("\nCount:", count, "\nTotal:", sum, "\nAverage:", sum/count)
