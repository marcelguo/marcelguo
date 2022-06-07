# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

str_to_find1 = r"EARFCN:"
str_to_find2 = r"Target Tx Pwr:"
str_to_find3 = r"Sensitivity ="


log_file = r"C:\Users\RFLAB_Uranus\Desktop\New folder\1.4M_RT_Sens\P1_SIP1_RT_1.4M_SENS\QSPRlog.txt"
result_file = r"C:\Users\RFLAB_Uranus\Desktop\New folder\results\result.txt"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    a = open(log_file, 'r')
    b = open(result_file, "w")

    for lines in a.readlines():
        if str_to_find1 in lines:
            b.write('channel:' + lines)
        if str_to_find2 in lines:
            b.write(lines)
        if str_to_find3 in lines:
            b.write(lines+ '\n')
    a.close()
    b.close()
