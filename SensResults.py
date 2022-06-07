# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

str_Channel = r"EARFCN:"
str_Pwr = r"Target Tx Pwr:"
str_Sens_result = r"Sensitivity ="
Band_name = {'18607': 'B2L',
             '18900': 'B2M',
             '19193': 'B2H',
             '19207': 'B3L',
             '19575': 'B3M',
             '19943': 'B3H',
             '19957': 'B4L',
             '20175': 'B4M',
             '20393': 'B4H',
             '20407': 'B5L',
             '20525': 'B5M',
             '20643': 'B5H',
             '21457': 'B8L',
             '21625': 'B8M',
             '21793': 'B8H',
             '23017': 'B12L',
             '23095': 'B12M',
             '23173': 'B12H',
             '131979': 'B66L',
             '132322': 'B66M',
             '132665': 'B66H'
             }

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
        if str_Channel in lines:
            for channel in Band_name:
                lines.replace(str_Channel,Band_name[channel])
            b.write(lines)
        if str_Pwr in lines:
            b.write(lines)
        if str_Sens_result in lines:
            b.write(lines + '\n')
    a.close()
    b.close()
