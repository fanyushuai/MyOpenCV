#-*- coding: UTF-8 -*-
'''
Created on 2018-1-24

@author: 土肥圆
'''
from pymongo import MongoClient
from bson.son import SON
import datetime  
   
client = MongoClient('localhost', 27017)

db = client['test']
#db.authenticate("testDba", "testDba")

def findOne(collectionName,_id):
    # 通过objectid来查找一个doc  
    collection = db[collectionName]  
   
    # 需要注意这里的obj_id是一个对象，不是一个str，使用str类型作为_id的值无法找到记录  
    # 可以通过ObjectId方法把str转成ObjectId类型  
    from bson.objectid import ObjectId  
    _id = ObjectId(_id)
    print collection.find_one({"_id": id})
    
def find(collectionName,params):
    collection = db[collectionName]
    if params == "":
        return SON(collection.find())
    else:
        return SON(collection.find(params))


if __name__ == '__main__':
    #findOne(db,'blogs','5a4f4252f1447e2f00b9953e');
    results = find('blogs',"{'author_name':'东门大官人'}");
    print(results.count())