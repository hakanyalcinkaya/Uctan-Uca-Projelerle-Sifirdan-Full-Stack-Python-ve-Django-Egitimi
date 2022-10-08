# Short If Kullanimi

from curses.ascii import isdigit


age = input("Yasinizi Giriniz: ")

# if age.isdigit():
#     age = int(age)
# else:
#     age = 0

age = int(age) if age.isdigit() else 0

# print("*" * 30)
# print(age)
# print("*" * 30)

print(f"{'*' * 30}\n{age:^30}\n{'*' * 30}")
