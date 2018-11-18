import random
import ctypes
import os
def clear():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
def generate():
    hitcounter = 0
    generated = 0
    letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWZXY'
    clear = lambda: 
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("Loveless.codes | Random Google Mini Code Gen")
    amount = input('How many codes do you want to generate?\r\n')
    clear()
    for x in range(int(amount)):
        generatedCode = 'B-';
        remaining = int(amount) - x;
        ctypes.windll.kernel32.SetConsoleTitleW("Generated: [" + str(generated) + "] | Remaining: [" + str(remaining) + "]")
        for i in range(23):
            generatedCode += random.choice(letters)
        print(generatedCode)
        with open("codes.txt", "a") as saveCode:
            saveCode.write(generatedCode + "\n")
            generated += 1
    ctypes.windll.kernel32.SetConsoleTitleW("Finished! | Generated: [" + str(generated) + "]")
    print("Generated: " + str(generated) + "\r")
    print("Done \o/\r")
    input("Do you want to restart?\r\n")
