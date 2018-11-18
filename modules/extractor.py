import ctypes
import re
import os
import sys
from codegen import clear
def extract():
    extracts = 0
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("Loveless.codes | Google Mini Extractor")
    if not os.path.exists("extracting.txt"):
        open("extracting.txt", mode='x').close()
        input('Please paste all your codes as such "link" in extracting.txt\r\n')
        clear()
        sys.exit(0)
    with open("extracting.txt", "r") as extract:
        for link in extract:
            b = re.search('.*promoCode=(.*?)$',link)
            extracted = b.group(1)
            print(extracted)
            with open("codes.txt", "a") as saveCode:
                saveCode.write(extracted + "\n")
                extracts += 1
    ctypes.windll.kernel32.SetConsoleTitleW("Finished! | Extracted: [" + str(extracts) + "]")
    print("\nExtracted: " + str(extracts) + "\r")
    print("Done \o/\r")
    input("Do you want to restart?\r\n")
