import sqlite3
import pandas as pd

def techRegister():
    conn = sqlite3.connect("database.db")


    df = pd.read_sql_query("SELECT * FROM tech_register", conn)


    df.to_excel("tech.xlsx", index=False)


    conn.close()



def nontechRegister():
    conn = sqlite3.connect("database.db")


    df = pd.read_sql_query("SELECT * FROM non_register", conn)


    df.to_excel("nontech.xlsx", index=False)


    conn.close()
techRegister()
nontechRegister()
