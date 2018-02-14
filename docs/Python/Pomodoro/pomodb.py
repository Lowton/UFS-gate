import config, pomolog
import sqlite3

#sqlite
def record_to_bd(start_time, end_time, task):
    conn = sqlite3.connect(config.dbfile)
    duration = end_time - start_time
    data = (start_time, end_time, duration, task)
    conn.execute("insert into Tasks values (?, ?, ?, ?)", data) # Insert a row of data
    conn.commit() # Save (commit) the changes
    conn.close()
