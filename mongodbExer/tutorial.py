"""
reference: 
- https://qiita.com/ognek/items/a37dd1cd0e26e6adecaa
- http://momijiame.tumblr.com/post/116551855651/python-pymongo-%E3%81%A7-mongodb-%E3%82%92%E6%93%8D%E4%BD%9C%E3%81%99%E3%82%8B
"""
from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)
# MongoDBの中に"test_database"という名前のデータベースがなかった場合は、自動的に作成されます。
db = client.test_database
# you can also write
# db = client['test-database']

collection = db.test_collection

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

# add post
res_1 = collection.insert_one(post)
# refer one of element
print(collection.find_one())
print(collection.find_one({"author": "Mike"}))

new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]

res_2 = collection.insert_many(new_posts)

print("show all post")
for post in collection.find():
    print(post)

# delete collection
collection.drop()
# delete database named `test_database`
client.drop_database('test_database')
