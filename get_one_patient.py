from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def get_one_patient(pt_id):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, name FROM patients INNER JOIN regimens ON patients.id = regimens.pt_id INNER JOIN drugs ON regimens.drug_id = drugs.id WHERE patients.id = " + pt_id)
        rows = cursor.fetchall()

        # print('Total Row(s):', cursor.rowcount)
        print('PATIENT: ', rows)
        return rows
        # for row in rows:
        #     print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


# if __name__ == '__main__':
#     query_with_fetchall()