import psycopg2

def postgres_test():
    try:
        conn = psycopg2.connect("dbname='dbtest22' user='postgres' host='localhost' password='longvu123'")
        return print(conn)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return False
postgres_test()