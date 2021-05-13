from connect_db import connection

def insertUser(name, password, email):

    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO `people` (`name`, `pass`, `email`) VALUES ("{}", "{}", "{}")'.format(name, password, email))
        connection.commit()

    return { "name" : name, "pass" : password, "email" : email }