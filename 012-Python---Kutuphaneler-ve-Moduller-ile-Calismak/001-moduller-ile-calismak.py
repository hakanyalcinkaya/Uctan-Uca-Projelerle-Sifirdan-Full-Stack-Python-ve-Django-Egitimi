# from library import modul
# import library
# from library import * (hersey) :)
# from library inport modul as new_name
# from time import sleep
# import time
# from time import * # -> Lutfen bu sekilde kullanmayalim..
from time import sleep as time_sleep

def sleep(x):
    print("sleep:)")

users = [
    "Cigdem",
    "Aytug",
    "Derin",
    "Derya",
    "Berk",
]

for user in users:
    print(user)
    # sleep(3)
    # time.sleep(3)
    time_sleep(3)

