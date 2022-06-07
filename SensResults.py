# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

str_to_find1 = "sensitivity"
str_to_find2 = "channel"
log_file = r"C:\Users\marcelguo\Desktop\Logs\log.txt"
result_file = r"C:\Users\marcelguo\Desktop\Results\result.txt"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    a = open(log_file, 'r')
    b = open(result_file, "w")

    for lines in a.readlines():
        if str_to_find1 in lines or str_to_find2 in lines:
            b.write(lines)

    a.close()
    b.close()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
