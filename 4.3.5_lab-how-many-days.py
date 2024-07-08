def is_year_leap(year):
    #
    # Your code from the previous LAB.
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False
    #

def days_in_month(year, month):
    #
    # Write your new code here.
    if month >12 :
        return
    if month <=0:
        return 0
    
    
    month_days=[31]*12
    thirty_days=[3,5,8,10]
    
    for i in range(12):
        if i==1:
            if is_year_leap(year):
                month_days[i]=29
                continue
            month_days[i]=28
            continue
        if i in thirty_days:
            month_days[i]=30
            continue
        
    return month_days[month-1]
    #

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
