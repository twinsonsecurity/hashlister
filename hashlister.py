#!/usr/bin/python3

import hashlib
from termcolor import colored, cprint
import os
import sys
import os.path
from os import path
import fnmatch


cprint("""
                 _     _ _     _            
  /\  /\__ _ ___| |__ | (_)___| |_ ___ _ __ 
 / /_/ / _` / __| '_ \| | / __| __/ _ \ '__|
/ __  / (_| \__ \ | | | | \__ \ ||  __/ |   
\/ /_/ \__,_|___/_| |_|_|_|___/\__\___|_|   
                                  v1 -RK
""", 'red')                                 

def ntlm(pw):
    return(hashlib.new('md4', pw.encode('utf-16le')).hexdigest())


pfile=input('Enter Filename of wordlist: ')
while True:
     #print ("\nOutput folder: "+current_dir)
     report = list(pfile)
     files_exist = path.exists(pfile)
     if (path.exists(pfile)) == False:
         cprint("Files don't exist. Please try again", 'red')
         files_exist = False
         sys.exit()
     else:
         files_exist = True

     if files_exist == True: 
         ofile=open(pfile, encoding = "ISO-8859-1")
         cprint("Warning! Any file that has the same name will be replaced.", 'yellow')
         fn=input("Enter name for new file: ") or pfile+'-hashed.txt'
         output=open(fn, "w")
         for line in ofile:
             if len(line)>0:
                 line=line.rstrip('\n')
                 #print(line)
                 #print(ntlm(line))
                 output.write(ntlm(line.rstrip('\r\n'))+('\n'))
         output.close()
         cprint("Hashlist Created",'green')
         break
