from pymongo import MongoClient
#import certifi

global con
global db
global coll

def connectdb():
    global con
    global db
    global coll
    con=MongoClient("mongodb+srv://Username:password@cluster0.s8rga.mongodb.net/bloodreport?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)#, tls=True,tlsAllowInvalidCertificates=True
    db=con.bloodreport
    coll=db.testname

def testlist():
    global coll
    global db
    connectdb()
    db=con.bloodreport
    coll=db.testname
    list=coll.find({})
    return list

def savedata(data):
    connectdb()
    db=con.bloodreport
    coll=db.bloodlist
    coll.insert(data)

def fulldata():
    connectdb()
    db=con.bloodreport
    coll=db.bloodlist
    list=coll.find({})
    return list

def fulldata_cont():
    connectdb()
    db=con.bloodreport
    coll=db.contractor
    list=coll.find({})
    return list

def countall_list():
    connectdb()
    db=con.bloodreport
    coll=db.bloodlist
    count=coll.aggregate([{"$count":"total_doc"}])
    return count

def total_cost():
    connectdb()
    db=con.bloodreport
    coll=db.bloodlist
    total=coll.aggregate([{"$group": {"_id":"null","totalcost": { "$sum": "$test_price"}}}])
    #total=coll.aggregate([{"$group": {"_id": '$first_name',"test_price": { "$sum": '$test_price' }}}, {"$project": { "_id": "0","test_price": '$test_price' }}]);
    return total

def search_record(name):
    connectdb()
    db=con.bloodreport
    coll=db.bloodlist
    record=coll.find({"contr":name})
    return record

def deletecoll(cid):
    global coll
    connectdb()
    coll=db.bloodlist
    coll.delete_one({"cid":cid})
