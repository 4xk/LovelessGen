from modules import codegen
import ctypes
import os
while True:
    clear = lambda: os.system('cls')
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("Loveless.codes | Discord: https://discord.gg/pWz6Mb8")
    module2load = input("Welcome to Loveless!\r\nWhich module would you like to load?\r\n\r\n1. Google Mini Code Gen\r\n\r\n")
    if "1" in module2load:
        codegen.generate()
    else:
        clear()
