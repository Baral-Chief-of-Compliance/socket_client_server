from datetime import date, timedelta
import datetime

def start_of_week():

    today = date.today()
    isoWeekDay = today.isoweekday()

    if isoWeekDay == 1:
        start_of_week = (today).strftime("%d.%m.%Y")
    elif isoWeekDay == 2:
        start_of_week = (today - timedelta(days = 1)).strftime("%d.%m.%Y")
    elif isoWeekDay == 3:
        start_of_week = (today - timedelta(days = 2)).strftime("%d.%m.%Y")
    elif isoWeekDay == 4:
        start_of_week = (today - timedelta(days = 3)).strftime("%d.%m.%Y")
    elif isoWeekDay == 5:
        start_of_week = (today - timedelta(days = 4)).strftime("%d.%m.%Y")
    elif isoWeekDay == 6:
        start_of_week = (today - timedelta(days = 5)).strftime("%d.%m.%Y")
    elif isoWeekDay == 7:
        start_of_week = (today - timedelta(days = 6)).strftime("%d.%m.%Y")


    return str(start_of_week)


def end_of_week():

        today = date.today()
        isoWeekDay = today.isoweekday()

        if isoWeekDay == 1:
            end_of_week = (today + timedelta(days = 6)).strftime("%d.%m.%Y")
        elif isoWeekDay == 2:
            end_of_week = (today + timedelta(days = 5)).strftime("%d.%m.%Y")
        elif isoWeekDay == 3:
            end_of_week = (today + timedelta(days = 4)).strftime("%d.%m.%Y")
        elif isoWeekDay == 4:
            end_of_week = (today + timedelta(days = 3)).strftime("%d.%m.%Y")
        elif isoWeekDay == 5:
            end_of_week = (today + timedelta(days = 2)).strftime("%d.%m.%Y")
        elif isoWeekDay == 6:
            end_of_week = (today + timedelta(days = 1)).strftime("%d.%m.%Y")
        elif isoWeekDay == 7:
            end_of_week = (today).strftime("%d.%m.%Y")

        return str(end_of_week)


def start_of_next_week():

    today = date.today()
    isoWeekDay = today.isoweekday()

    if isoWeekDay == 1:
        start_of_week = today
    elif isoWeekDay == 2:
        start_of_week = today - timedelta(days = 1)
    elif isoWeekDay == 3:
        start_of_week = today - timedelta(days = 2)
    elif isoWeekDay == 4:
        start_of_week = today - timedelta(days = 3)
    elif isoWeekDay == 5:
        start_of_week = today - timedelta(days = 4)
    elif isoWeekDay == 6:
        start_of_week = today - timedelta(days = 5)
    elif isoWeekDay == 7:
        start_of_week = today - timedelta(days = 6)

    return str(start_of_week+timedelta(days = 7))


def end_of_next_week():

        today = date.today()
        isoWeekDay = today.isoweekday()

        if isoWeekDay == 1:
            end_of_week = today + timedelta(days = 6)
        elif isoWeekDay == 2:
            end_of_week = today + timedelta(days = 5)
        elif isoWeekDay == 3:
            end_of_week = today + timedelta(days = 4)
        elif isoWeekDay == 4:
            end_of_week = today + timedelta(days = 3)
        elif isoWeekDay == 5:
            end_of_week = today + timedelta(days = 2)
        elif isoWeekDay == 6:
            end_of_week = today + timedelta(days = 1)
        elif isoWeekDay == 7:
            end_of_week = today

        return str(end_of_week+timedelta(days = 7))

def chek_time():
    date = datetime.datetime.today()
    return date.strftime('%H:%M')

def crate_str():
    sw = start_of_week()
    ew = end_of_week()
    stroka = sw+'-'+ew
    return stroka
