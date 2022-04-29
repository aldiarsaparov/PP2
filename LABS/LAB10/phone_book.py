import psycopg2, csv
from config import data
config = psycopg2.connect(**data) 
current = config.cursor()

create_table = '''
CREATE TABLE phonebook(
    name varchar,
    number varchar
)
'''
insert = '''
INSERT INTO phonebook VALUES (%s,%s);

'''
select = ''' 
SELECT * FROM phonebook; 
 
''' 
update = '''
UPDATE phonebook SET number = %s WHERE name = %s;
'''
delete = '''
DELETE FROM phonebook WHERE name = %s;
'''
print("Type '1' to create the table, '2' to insert data, '3' to update data, '4' to delete data")
num = int(input())

if num == 1:
    current.execute(create_table)
elif num == 2:
    current.execute(insert, (input(),input()))
elif num == 3:
    current.execute(update,(input(),input()))
elif num == 4:
    current.execute(delete,[input()])

with open('phonebook.csv','r') as f:
    reader = csv.reader(f,delimiter = ',')
    for row in reader:
        current.execute(insert, row)

current.execute(select)
v = current.fetchall() # to recieve the data
print(v) 

current.close() 
config.commit() 
config.close()