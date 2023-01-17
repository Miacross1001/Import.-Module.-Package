from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import requests

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now())
    response = requests.get('https://pypi.org/search/?q=&o=&c=Development+Status+%3A%3A+2+-+Pre-Alpha')
    print(response.text[0:200])
