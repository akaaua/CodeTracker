import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()


def _create_database():
    
    with conn:
        c.execute("CREATE TABLE IF NOT EXISTS ct_projects (id INTEGER PRIMARY KEY AUTOINCREMENT, project text)")
        c.execute("CREATE TABLE IF NOT EXISTS ct_dates (id INTEGER PRIMARY KEY AUTOINCREMENT, day integer, month integer, year integer, projectid INTEGER, FOREIGN KEY(projectid) REFERENCES ct_projects(id))")


def _insert_project(project):
    
    with conn:
        c.execute("INSERT INTO ct_projects values (NULL, :project)", {'project':project})
    return ("Inserido com sucesso")

def _insert_date(day, month, year, projectid):
    
     with conn:
         c.execute("INSERT INTO ct_dates values (NULL, :day, :month, :year, :projectid)", {'day':day, 'month':month, 'year':year, 'projectid':projectid})
    
     return ('Data Inserida Com Sucesso')

def _check_if_exists(project):

    test = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=':table_name'", {'table_name':project})

    if test > 0:
        return True
    else:
        return False

def _get_projectid(project):
    
    c.execute("select id FROM ct_projects WHERE project = :project", {'project':project})
    return c.fetchone()

def _get_projects(project):
    
    c.execute("select project FROM ct_projects WHERE project = :project", {'project':project})
    return c.fetchone()

def _get_dates():
    
    c.execute("select * FROM ct_dates")
    return c.fetchall()

def _get_projects_and_dates():

    c.execute("select project, day, month, year FROM ct_projects, ct_dates WHERE ct_dates.id = ct_projects.id")    
    return c.fetchall()

conn.commit()

