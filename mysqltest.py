import pymysql


def conn_sql():
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user='root',
                           password='test123456',
                           charset='utf8',
                           db='my_login'
                           )
    return conn


def insert_sql(sql, conn, data):
    cursor = conn.cursor()
    try:
        cursor.execute(sql, data)
        cursor.commit()
    except Exception as e:
        print("插入失败", e)
        conn.rollback()


def update_sql(sql, conn, data):
    cursor = conn.cursor()
    try:
        cursor.execute(sql, data)
        cursor.commit()
    except Exception as e:
        print("修改失败", e)
        conn.rollback()


def delete_sql(sql, conn, data):
    cursor = conn.cursor()
    try:
        cursor.execute(sql, data)
        cursor.commit()
    except Exception as e:
        print("删除失败", e)
        conn.rollback()


def select_sql(sql, conn, data):
    cursor = conn.cursor()
    cursor.execute(sql, data)
    ret = cursor.fetchall(sql)
    return ret
