import datetime
from application.db.people import *
from application.salary import *




def main():
    print('Getting started with the program')
    today_date = datetime.date(2023, 6, 1)
    print(today_date)


if __name__ == '__main__':
    main()
    calculate_salary()
    get_employees()

