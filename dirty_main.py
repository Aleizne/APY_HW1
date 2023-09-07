from main import *

# Декораторов до этой лекции еще не проходили, потому я попробовал применить "не совсем декоратор".


def timed_call(func):
    dt_now = datetime.datetime.now()
    print(dt_now)
    print(func)

if __name__ == '__main__':
    timed_call(get_employees("Vasya"))
    timed_call(calculate_salary(100))