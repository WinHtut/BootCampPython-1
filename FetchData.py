import pymongo
class DatabaseClass():
    def __init__(self,toSerachName):
        self.connection = pymongo.MongoClient("localhost", 27017)
        self.database = self.connection["MyFristDb"]
        self.collection = self.database["My_col1"]
        self.toSerachName = toSerachName
    def databaseMethod(self):
        toReturn =''
        try:
            myQuery = {'name': self.toSerachName}
            data = self.collection.find(myQuery)
            print("type",type(data))


            for z in data:

                if z['name'] == self.toSerachName:

                    findingData = self.collection.find(myQuery)
                    for i in findingData:
                        toReturn = i['Hobby']


            return toReturn

        except Exception as err:
            print(err)

if __name__ == "__main__":
    db  = DatabaseClass('development')
    data=db.databaseMethod()
    print(data)

