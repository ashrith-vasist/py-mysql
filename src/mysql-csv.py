import mysql.connector
def mysql_to_csv():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    port= 3306,
    database="testing"
    )
    mycursor = mydb.cursor()
    mycursor.execute("show tables;")
    table_name=mycursor.fetchall()
    print(table_name)
    def convertTuple(tup):
        # initialize an empty string
        str1 = ''
        for item in tup:
            str1 = str1 + item
        return str1

    def export(header,rows,table_name_str):
    
        f=open(table_name_str+'.csv','w')
        f.write(','.join(header)+'\n')
        for row in rows:
            f.write(','.join(str(r) for r in row)+'\n')
        f.close()
        print(str(len(rows))+'rows written successfully to '+f.name)


    for x in table_name:
        mycursor.execute("select * from "+convertTuple(x))
        header=[row[0] for row in mycursor.description]
        rows=mycursor.fetchall()
        export(header,rows,convertTuple(x))

mysql_to_csv()









