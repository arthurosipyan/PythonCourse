import random
import re


def open_file():
    try:
        my_file = open('mydata2.txt', encoding='utf-8')
    except FileNotFoundError as ex:
        print("*** ERROR: File Not Found! ***")
        print(ex.args)

    else:
        print("File: ", my_file.read())
        my_file.close()
    finally:
        print("*** File closed. ***")


nums = list(range(1, 20))


def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def change_list(func, nums_list):
    new_list = []
    for i in nums_list:
        if func(i):
            new_list.append(i)
    return new_list


def anonymous_func():
    flip_list = []
    for i in range(1,101):
        flip_list += random.choice(['H', 'T'])

    print("Heads: ", flip_list.count('H'))
    print("Tails: ", flip_list.count('T'))


def list_comprehensions_exercise():
    print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])


def is_email(email_list):
    print("Email Matches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email_list)))


def main():
    choice = 0
    try:
        choice = int(input("Which exercise would you like to test?\n"
                           "1. Open File\n"
                           "2. Functions as Objects\n"
                           "3. Anonymous Functions\n"
                           "4. List Comprehensions\n"
                           "5. Valid Email with Regex\n"
                           "Exercise: "))
    except ValueError:
        print("ERROR: Please enter a number...\n")
        main()
    if choice == 1:
        open_file()
    elif choice == 2:
        print(change_list(is_it_odd, nums))
    elif choice == 3:
        anonymous_func()
    elif choice == 4:
        list_comprehensions_exercise()
    elif choice == 5:
        emails = "db@aol.com m@.com @apple.com db@.com"
        is_email(emails)


main()
