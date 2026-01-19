# This is how you work out whether if a particular year is a leap year. 
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder 
# - unless the year is also divisible by 400 with no remainder   


def is_leap_year(year):
    """Take an integer as a year and checks if it is a leap year and return a boolean"""
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 == 0 and year % 400 != 0:
            return False
        else: return True
    else: return False


def is_leap_year2(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else: return True
    else: return False
    

            
        
print(is_leap_year(2100))
print(is_leap_year2(2020))