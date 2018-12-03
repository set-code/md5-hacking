import os
import sys
from colors import *
import hashlib
import mods

print("\n")
#202cb962ac59075b964b07152d234b70

md5f = hashlib.md5(open('Password_list','rb').read()).hexdigest()

sys.stdout.write(BOLD)
sys.stdout.write(GREEN)
print("********************************************************")
print("*                                                      *")
print("*                    HACKING MD5 HASH                  *")
print("*                                                      *")
print("********************************************************\n")
sys.stdout.write(RESET)

print(" Command: --c Create MD5 \n Command: --h Hacking MD5\n")
actions = input(" Command: ")
print("\n")
create_md5 = 0
hacking_md5 = 0

if actions == '--c':
    create_md5 = 1

if actions == '--h':
    hacking_md5 = 1


if hacking_md5 == 1:
    with open("Password_list") as file:
        Pass = [row.strip() for row in file]

    md5_hash = input(" Md5 hash: ")
    Pass_Count = len(Pass)
    print(" Found passwords: ", Pass_Count, "\n")

    print("========================================================\n")

    i = 0
    counts = 1
    while i < Pass_Count:

        s = str(Pass[i])
        m = hashlib.md5(s.encode('utf-8')).hexdigest()

        if m == md5_hash:

            print("\n")
            sys.stdout.write(GREEN)
            print(" Hacking MD5 GOODS!\n")
            print(" MD5 Hash: ", md5_hash, " \n Password: ", Pass[i], " OK ")
            password_hack = 1
            break
        else:
            password_hack = 0

        mods.get_pass_check(i, Pass_Count)
        i = i + 1

    if password_hack == 0:
        sys.stdout.write(RED)
        print("\n\n Could not find password...")

    sys.stdout.write(RESET)
    print("\n========================================================\n")


if create_md5 == 1:
    New_create_md5 = input(" String to MD5: ")
    s_create_md5 = str(New_create_md5)
    m = hashlib.md5(s_create_md5.encode('utf-8')).hexdigest()
    print("\n ========================================================\n")
    sys.stdout.write(GREEN)
    print(' Md5: ',m)
    sys.stdout.write(RESET)
    print("\n ========================================================\n")




#os.system('clear')
os.execl(sys.executable, sys.executable, *sys.argv)