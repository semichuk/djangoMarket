def select_from_db(connection, query):
    cursor = connection.cursor()
    result = None
   # try:
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    #except Error as e:
    #    print(f"The error '{e}' occurred")
