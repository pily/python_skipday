import datetime

import holidays

kr_holidays = holidays.Korea()

def isweekend(day):

    num_day = int(datetime.datetime.weekday(day))
    if  num_day == 5 or num_day == 6:
        result = True
    else:
        result = False

    return result

def shiftday(day):
    shiftday = day + datetime.timedelta(days=1)
    return shiftday

def korday(day):
    kordaystr = ['월','화','수','목','금','토','일']
    return kordaystr[day] + '요일'

def timestamp(day):
    return "[" + str(day) + " " + korday(datetime.datetime.weekday(day)) + "]"

def skipday(day):
    
    print(timestamp(day) + " 입력 받은 날짜")

    day = shiftday(day)
    print(timestamp(day) + " 다음 날짜로 변경 합니다.")
    while True:
        while True:
            if isweekend(day):
                print(timestamp(day) + " 주말로 판단하여 하루 미룹니다. (" +korday(datetime.datetime.weekday(day))+ ")")
                day = shiftday(day)

                pass_check1 = 0
                pass_check2 = 0
                
            else:
                pass_check1 = 1
                break

        while True:
            isholiday = day in kr_holidays
            if isholiday:
                print(timestamp(day) + " 공휴일로 판단하여 하루 미룹니다. (" + kr_holidays.get(day) + ")" )
                day = shiftday(day)

                pass_check1 = 0
                pass_check2 = 0

            else:
                pass_check2 = 1
                break
            
        if pass_check1 == 1 and pass_check2 == 1 :
            break

    return day


day = datetime.datetime.now()
#strday = '2021-02-27'
#day = datetime.datetime.strptime(strday, '%Y-%m-%d')

day = skipday(day)
print(timestamp(day) + " 지정된 날짜")