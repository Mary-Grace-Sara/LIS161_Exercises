try:
    hour_num = float(input("Enter Hours: "))
    rate_num = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if hour_num > 40:
    reg = hour_num * rate_num
    num = (hour_num - 40.0) * (rate_num * 0.5)
    pay =  reg + num
else:
    pay = hour_num * rate_num

print("\nPay:", pay)
