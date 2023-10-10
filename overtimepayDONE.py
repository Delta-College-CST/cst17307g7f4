# This program prompts the user for an employee's work time
# and pay rate.  It determines the weekly gross pay considering
# time-and-a half for hours over the base 40 hour work week.

BASE_HOURS = 40.0

def calcGrossPay(hours,rate):
    if hours <= BASE_HOURS:
        pay = hoursWorked * rate
    else:
        pay = rate * BASE_HOURS + (hours - BASE_HOURS) * 1.5 * rate
    return pay

# Prompt for worker input
hoursWorked = float(input("Enter hours worked: "))
payRate     = float(input("Enter pay rate: "))

# Calculate gross pay for week
grossPay = calcGrossPay(hoursWorked,payRate)

# Report payroll summary
print ("PAYROLL")
print ("Pay rate: $%6.2f per hour" % (payRate))
print ("Hours Worked:",hoursWorked,"hours")
print ("Paycheck: $%7.2f" % (grossPay))
