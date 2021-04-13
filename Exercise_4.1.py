def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        num = (hours - 40.0) * (rate * 0.5)
        pay =  reg + num
    else:
        pay = hours * rate
    return pay

try:
    hour_num = float(input("Enter Hours: "))
    rate_num = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

pay = computepay(hour_num,rate_num)
print("\nPay:", pay)
