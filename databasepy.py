import pymongo

connection  = pymongo.MongoClient("localhost",27017)
database =connection["MyFristDb"]
collection = database["My_col1"]

data = [
        {'name':'SuThiri' , 'age':27 , 'Hobby':'Coding'},
        {'name':'nyeineiphyu' , 'age':27 , 'Hobby':'Networing and Lazy'},
        {'name':'thitthitnyein' , 'age':27 , 'Hobby':'Reading and Question'},
        {'name':'students' , 'age':27 , 'Hobby':'Networking'}

        ]

if __name__ == "__main__":
    try:
        collection.insert_many(data)
        print("Data are successfully inserted!")
    except Exception as err:
        print(err)

