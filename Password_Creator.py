#! /usr/bin/env python3

import random
import string
import argparse
import threading

pass_list = []

def gen(length=8, lower=False, upper=False, sp=False, digits=False, ):
    pass_wd = ""
    if lower:
        pass_wd += string.ascii_lowercase

    if upper:
        pass_wd += string.ascii_uppercase
    
    if sp:
        pass_wd += string.punctuation
    
    if digits:
        pass_wd += string.digits
    
    try:
        pass_list.append("".join(random.choices(pass_wd,k=length)))
    except:
        return "somthing wrong"


if __name__ == "__main__":

    arg = argparse.ArgumentParser(description="for creating password")
    arg.add_argument('len',type=int,help="length of password")
    arg.add_argument("-l","--lower",help="for use lowercase", action="store_true")
    arg.add_argument("-u","--upper", help="For use uppercase",action="store_true")
    arg.add_argument("-d","--digit", help="For use number",action="store_true")
    arg.add_argument("-p","--punctuation", help="For use special charchter",action="store_true")
    argss = arg.parse_args()

    threads = []
    for i in range(4):
        th = threading.Thread(target=gen , args=(argss.len,argss.lower,argss.upper,argss.punctuation,argss.digit,))
        threads.append(th)
        th.start()

    for pw in threads:
        pw.join()

    print("-".join(pass_list))