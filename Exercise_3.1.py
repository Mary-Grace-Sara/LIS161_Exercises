hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    reg = hours * rate
    num = (hours - 40.0) * (rate * 0.5)
    pay =  reg + num
else:
    pay = hours * rate

print("\nPay:", pay)
