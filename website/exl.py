import sqlite3
import pandas as pd
import os



class ecxle():
    def techRegister():
        # Get all files in the /test directory
        files = os.listdir('/website')

        # Filter them by the file type
        python_files = [f for f in files if f.endswith('.db')]
        conn = sqlite3.connect(python_files)


        df = pd.read_sql_query("SELECT * FROM tech_register", conn)


        df.to_excel("tech.xlsx", index=False)


        conn.close()



    def nontechRegister():
        conn = sqlite3.connect("/website/database.db")


        df = pd.read_sql_query("SELECT * FROM non_register", conn)


        df.to_excel("nontech.xlsx", index=False)


        conn.close()
e=ecxle()
e.techRegister()