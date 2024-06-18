# find the year is leap year or not
# if leap year return True else False

# solution

year = int(input())

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
    
print(is_leap(year))