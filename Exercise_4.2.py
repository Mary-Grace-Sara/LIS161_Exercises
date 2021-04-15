def computegrade(score):
    if score > 1.0:
        return "Error, please enter a number between 0.0 and 1.0"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score >= 0.0:
        return "F"
    else:
        return "Error, please enter a number between 0.0 and 1.0"

input_score = input("Enter score: ")
try:
    grade = float(input_score)
except:
    print("Error, please enter numeric input")
    exit()

str_grade = computegrade(grade)
print(str_grade)
