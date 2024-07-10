from db.dbconnect import DBconnect 

db = DBconnect()

def select_query():
    try:

        cursor = db.get_cursor()

        query = """
            SELECT *
            FROM 
        """
        cursor.execute(query)

        row = cursor.fetchone()

        print(row)


    finally:
        db.close()

def main():

    print(asd)



if __name__ == "__main__":
    main()
