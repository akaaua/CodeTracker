import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()


def _create_database():
    
    with conn:
        c.execute("CREATE TABLE code_tracker (project text, day integer, month integer, year integer)")


def _insert_project(project):
    
    with conn:
        c.execute("INSERT INTO code_tracker (project) values (:project)", {'project':project})
        return ("Inserido com sucesso")

def _insert_date(day, month, year):
    
     with conn:
         c.execute("UPDATE code_tracker SET day=:day, month=:month, year=:year WHERE project='CodeTracker'", {'day':day, 'month':month, 'year':year})

conn.commit()

