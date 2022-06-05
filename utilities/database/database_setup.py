import pymongo

myclient = pymongo.MongoClient("mongodb+srv://rj:rj336699@cluster0.slpu1.mongodb.net/?retryWrites=true&w=majority")


mydb = myclient["asitro"]
mydb2 = myclient["lucifer"]
mycol = mydb["user"]