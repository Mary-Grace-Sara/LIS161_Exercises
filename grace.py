str = "X-DSPAM-Confidence: 0.8475"
meow = str.find(":")
print(meow)
num = str[meow+2:]
print(num)
fnum = float(num)
print(fnum)
print(fnum + 56.32)
