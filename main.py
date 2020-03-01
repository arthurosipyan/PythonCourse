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


def main():
    # open_file()
    print(change_list(is_it_odd, nums))


main()
