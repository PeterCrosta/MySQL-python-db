from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_patient(first_name, last_name):
    query = "INSERT INTO patients(first_name,last_name) " \
            "VALUES(%s,%s)"
    args = (first_name, last_name)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

# def main():
#    insert_patient('Manami','Ueda')

# if __name__ == '__main__':
#     main()