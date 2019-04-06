# Exercise 5

powerPrice = 1.7
# Yuan per kWh

def pluralFix(num, string):
    if num != 1 and num != 0:
        string += 's'
    return str(num) + string
usagePower = int(input("Please input the usage of power... >>>"))
powerFee = 1.7 * usagePower
print 'Power fee is', powerFee
print 'You need you pay', pluralFix(int(powerFee), ' "1 yuan" coin'),'and', pluralFix(int(round(10 * (powerFee - int(powerFee)))), ' "1 jiao" coin') + '.'
