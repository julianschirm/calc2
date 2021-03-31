import os
try:
    print("SchirmTec Calculator Pro 1.1")
    print("-----------------------------")
    summe = eval(input())
    print(("=") +(str(summe)))
    print(" ")
    os.system('python3 D:\Bin\calc.py')
except NameError:
    print("syntax error")
    os.system('python3 D:\Bin\calc.py')
except KeyboardInterrupt:
    os.system("cls")
    print("Auf Wiedersehen")
