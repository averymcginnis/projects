# Day of the Week Calcultor
# Input a date and the program will return the day of the week.
# Works for dates between 1701 and 2099
# Credit to Math Magic by Scott Flansburg

import datetime

# Tell the user how the program works
print('\n----------------------------------------------\n'
    'Enter a month, day, and year of a date between\n'
    '1701 and 2099 and the program will tell you\n'
    'what day of the week the date occurred on.\n'
    '----------------------------------------------\n')

def calculateDay(month,day,year):
    # Record the significant values for each month
    SV = {'january':0,'february':3,'march':3,'april':6,'may':1,
      'june':4,'july':6,'august':2,'september':5,'october':0,
      'november':3,'december':5}

    # Record the values for each day of the week    
    daysOfWeek = {'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,
              'Thursday':4,'Friday':5,'Saturday':6}
    dayList = list(daysOfWeek.keys())
    numList = list(daysOfWeek.values())

    # Get the last two digits of the year
    yearString = str(year)
    yearDigits = yearString[2:]
    yearDigits = int(yearDigits)

    # Divide the year by 4, discard the remainder
    divideByFour = yearDigits//4

    # Get the significant value
    sigValue = SV[month]

    # Perform the "calendar equation"
    dayNum = (divideByFour + yearDigits + day + sigValue) % 7

# Make century/leap year adjustments.
    # Leap year
    if month == 'january' or month == 'february':
        if year % 4 == 0:
            dayNum = dayNum - 1
        if dayNum == -1:
            dayNum = 6

    # 1700's
    if year > 1699 and year < 1800:
        dayNum = dayNum + 4
        if dayNum > 6:
            dayNum = dayNum % 7
    # 1800's
    if year > 1799 and year < 1900:
        dayNum = dayNum + 2
        if dayNum > 6:
            dayNum = dayNum % 7

    # 2000's 
    if year > 1999 and year < 2100:
        dayNum = dayNum - 1
        if dayNum == -1:
            dayNum = 6

    # Find the day of the week that corresponds to the number
    answer = dayList[numList.index(dayNum)]

    return answer

# -----------------------------------------------------------------

def getInput():
    # Create a lists of months 
    months = ['january','february','march','april','may','june',
        'july','august','september','october','november','december']

    # Get the date from the user
    m = input('Enter a month: ')
    m = m.lower()
    m = m.strip()
    try:
        d = int(input('Enter a day: '))
    except ValueError:
        d = 0
    try:
        y = int(input('Enter a year: '))
    except ValueError:
        y = 0

    # Check for valid dates
    if m not in months:
        print('\nENTER A VALID DATE\n')
        return None,None,None
    if d < 1 or d > 31:
        print('\nENTER A VALID DATE\n')
        return None,None,None
    if y < 1701 or y > 2099:
        print('\nENTER A DATE BETWEEN 1701 AND 2099\n')
        return None,None,None

    return m, d, y

# -----------------------------------------------------------------

def main():
    while True:
        # Get the input
        m,d,y = getInput()
        if m is None:
            continue

        # Run the function
        result = calculateDay(m,d,y)

        # Return the result
        months = ['january','february','march','april','may','june',
        'july','august','september','october','november','december']
        currentYear = str(datetime.date.today())
        currentYear = int(currentYear[0:4])
        if y < currentYear:
            print('\n' + m, str(d) + ', ' + str(y) + ' was a ' + result + '\n')
        if y > currentYear:
            print('\n' + m, str(d) + ', ' + str(y) + ' will be a ' + result + '\n')
        if y == currentYear:
            currentMonth = str(datetime.date.today())
            currentMonth = int(currentMonth[5:7])
            if (months.index(m) + 1) < currentMonth:
                print('\n' + m, str(d) + ', ' + str(y) + ' was a ' + result + '\n')
            if (months.index(m) + 1) > currentMonth:
                print('\n' + m, str(d) + ', ' + str(y) + ' will be a ' + result + '\n')
            if (months.index(m) + 1) == currentMonth:
                currentDay = str(datetime.date.today())
                currentDay = int(currentDay[8:10])
                if d < currentDay:
                    print('\n' + m, str(d) + ', ' + str(y) + ' was a ' + result + '\n')
                if d > currentDay:
                    print('\n' + m, str(d) + ', ' + str(y) + ' will be a ' + result + '\n')
                if d == currentDay:
                    print('\nThat\'s today! Just ask your friend dummy.\n')

main()
