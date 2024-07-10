import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS organizations (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            name TEXT,
            url TEXT,
            salary_from INTEGER,
            salary_to INTEGER,
            city TEXT,
            experience TEXT,
            organization_id INTEGER REFERENCES organizations(id)
        )
        """
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_organizations():
    organizations = [
        ('Company A',),
        ('Company B',),
        ('Company C',),
        ('Company D',),
        ('Company E',),
        ('Company F',),
        ('Company G',),
        ('Company H',),
        ('Company I',),
        ('Company J',)
    ]
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany("INSERT INTO organizations (name) VALUES (%s)", organizations)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
    insert_organizations()
