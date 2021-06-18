import pymysql.cursors

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'learning',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)


cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS `people` (`id` int(11) PRIMARY KEY AUTO_INCREMENT, `name` varchar(255), `pass` varchar(255), `email` varchar(255))')