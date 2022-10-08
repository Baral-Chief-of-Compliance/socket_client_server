from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta
import for_date as fd


def timetable_on_week():
    with open("time_table.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_tables = soup.find_all(class_ = "table table-bordered table-striped table-3")
    all_tables.pop(6)

    result = ""

    for item in all_tables:
        day_titel = item.find(class_="title")
        subjects_title = item.find_all("tr")
        subjects_title.pop(0)

        result = result + "----" + day_titel.text + "----\n"
        for subject in subjects_title:
            subjects_td = subject.find_all("td")
            i = 0
            for subject_td in subjects_td:
                i+=1
                if i == 1:
                    result = result + subject_td.text + ") "
                else:
                    result = result + subject_td.text + " "
            result = result + "\n"
        result = result + "----------------" + "\n\n"

    return (result)



def timetable_on_today():

    with open("time_table.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_tables = soup.find_all(class_ = "table table-bordered table-striped table-3")
    all_tables.pop(6)

    result = ""

    today = date.today()
    isoWeekDay = today.isoweekday()
    i=1

    for item in all_tables:
        if isoWeekDay == i:
            day_titel = item.find(class_="title")
            subjects_title = item.find_all("tr")

            subjects_title.pop(0)

            result = result + "----" + day_titel.text + "----\n"
            for subject in subjects_title:
                subjects_td = subject.find_all("td")
                i = 0
                for subject_td in subjects_td:
                    i+=1
                    if i == 1:
                        result = result + subject_td.text + ") "
                    else:
                        result = result + subject_td.text + " "
                result = result + "\n"
            result = result + "----------------" + "\n\n"
        i+=1

    return (result)


# def timetable_next_week():
#     with open("next_week.html") as file:
#         src = file.read()
#
#     soup = BeautifulSoup(src, "lxml")
#
#     all_tables = soup.find_all(class_ = "table table-bordered table-striped table-3")
#     all_tables.pop(6)
#
#     result = ""
#
#     next_day = date.today() + timedelta(days = 7)
#     isoWeekDay = next_day.isoweekday()
#     i=1
#
#     for item in all_tables:
#         if isoWeekDay == i:
#             day_titel = item.find(class_="title")
#             subjects_title = item.find_all("tr")
#
#             subjects_title.pop(0)
#
#             result = result + "----" + day_titel.text + "----\n"
#             for subject in subjects_title:
#                 subjects_td = subject.find_all("td")
#                 i = 0
#                 for subject_td in subjects_td:
#                     i+=1
#                     if i == 1:
#                         result = result + subject_td.text + ") "
#                     else:
#                         result = result + subject_td.text + " "
#                 result = result + "\n"
#             result = result + "----------------" + "\n\n"
#         i+=1
#
#     return (result)
