hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    real_hours = float(hours)
    real_rate = float(rate)
except:
    print('Error, please enter a numeric input')
    quit()
if real_hours > 40:
    print('Overtime')
    real_hours = ((real_hours - 40) * 1.5 + 40)
else:
    print('Regular')
pay = real_hours * real_rate
print('Pay:', pay)