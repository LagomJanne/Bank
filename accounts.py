import os
from random import randint
import json
from os.path import exists
import sqlite3
import gui
import random



accounts = []

con = sqlite3.connect("Bnank.db")
cur = con.cursor()




class account:
    def __init__(self, acc_num : str, f_name : str, s_name : str, pin : str, balance : float):
        self.accNum = acc_num
        self.f_name = f_name
        self.s_name = s_name
        self.pin = pin
        self.balance = balance


def gen_accNum():
    a = random.randint(10000000, 99999999)
    return a

def load():
    result = cur.execute("SELECT * FROM Account")
    accounts = result.fetchall()
    print(accounts)

def save(Fname, Sname, pin):
    acc = gen_accNum()
    new_acc = cur.execute("""INSERT INTO Account (acc_num, f_name, s_name, pin, balance) VALUES('acc', "Fname", "Sname", "pass", "0") """)
    con.commit()
    load()



save()




