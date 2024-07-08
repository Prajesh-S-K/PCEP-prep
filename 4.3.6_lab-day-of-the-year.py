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
    # Your code from the previous lab.
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

def day_of_year(year, month, day):
    #
    # Write your new code here.
    if year<0 or month<0 or day<0 :
        return
    if day > days_in_month(year, month):
        return
    year_day=0
    for i in range(month):
        year_day +=days_in_month(year, i)
    return year_day+day
    #


#print(day_of_year(2000, 12, 31))

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_date = [2,4,8,16]
test_results = [33, 35, 8, 320]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    dy = test_date[i]
    print(yr, mo, dy, "->", end="")
    result = day_of_year(yr, mo,dy)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
